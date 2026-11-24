"""第二支：15 秒三段拼接（T2V 5s → I2V 5s → I2V 5s），含旁白與環境音。"""
from __future__ import annotations

import base64
import json
import os
import subprocess
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]  # 專案根目錄（macOS／Linux 皆可）
ENV = ROOT / ".env"
WORK = Path("/tmp/film2")
WORK.mkdir(parents=True, exist_ok=True)
EXPORTS = ROOT / "exports"
EXPORTS.mkdir(exist_ok=True)

for line in ENV.read_text().splitlines():
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1)
        os.environ.setdefault(k, v)

KEY = os.environ["MINIMAX_API_KEY"]
BASE = os.environ["MINIMAX_BASE_URL"].rstrip("/")
H = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}
RES = "768P"

SEG1_PROMPT = (
    "cinematic wide shot, rainy neon alley at night, a young woman in a beige trench coat stands still "
    "as a paper crane rises from a puddle and dissolves into drifting points of light, reflections on wet "
    "pavement, slow camera push in, film grain"
)
SEG2_PROMPT = (
    "the drifting points of light gather into a glowing paper bird that circles around the woman, "
    "she turns her head following it, rain streaks through the neon glow, slow orbit camera"
)
SEG3_PROMPT = (
    "the woman slowly raises her hand and the glowing bird lands in her palm, its light spreading over "
    "her face and the wet street, camera pushes in to a close-up, rain keeps falling"
)
NARRATION = "紙鶴化成了光。她伸手，光落在掌心，像一場沒有結束的雨。"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def create(model: str, prompt: str, duration: int, first_frame: Path | None = None) -> str:
    payload = {"model": model, "prompt": prompt, "duration": duration, "resolution": RES}
    if first_frame is not None:
        payload["first_frame_image"] = "data:image/jpeg;base64," + base64.b64encode(first_frame.read_bytes()).decode()
    r = requests.post(f"{BASE}/video_generation", headers=H, json=payload, timeout=120)
    body = r.json()
    code = (body.get("base_resp") or {}).get("status_code")
    if code != 0:
        raise RuntimeError(f"create failed: {body}")
    return body["task_id"]


def wait(task_id: str, timeout: int = 600) -> None:
    t0 = time.time()
    while time.time() - t0 < timeout:
        r = requests.get(f"{BASE}/query/video_generation", headers=H, params={"task_id": task_id}, timeout=30)
        status = r.json().get("status")
        print(f"  [{int(time.time()-t0)}s] {status}", flush=True)
        if status == "Success":
            return
        if status in ("Fail", "Failed"):
            raise RuntimeError(f"task failed: {r.text[:200]}")
        time.sleep(8)
    raise TimeoutError(task_id)


def download(task_id: str, dest: Path) -> Path:
    q = requests.get(f"{BASE}/query/video_generation", headers=H, params={"task_id": task_id}, timeout=30).json()
    info = requests.get(f"{BASE}/files/retrieve", headers=H, params={"file_id": q["file_id"]}, timeout=30).json()
    url = (info.get("file") or {}).get("download_url")
    data = requests.get(url, timeout=300).content
    dest.write_bytes(data)
    print(f"  saved {dest.name} {len(data)//1024} KB", flush=True)
    return dest


def last_frame(video: Path, out: Path) -> Path:
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-sseof", "-0.1", "-i", str(video),
         "-frames:v", "1", "-q:v", "2", str(out)])
    return out


def gen_segment(name: str, model: str, prompt: str, first: Path | None = None, duration: int = 5) -> Path:
    out = WORK / f"{name}.mp4"
    if out.is_file() and out.stat().st_size > 100_000:
        print(f"{name}: reuse", flush=True)
        return out
    print(f"{name}: creating ({model})", flush=True)
    tid = create(model, prompt, duration, first)
    print(f"  task {tid}", flush=True)
    wait(tid)
    return download(tid, out)


def tts(text: str, dest: Path) -> Path:
    r = requests.post(f"{BASE}/t2a_v2", headers=H, json={
        "model": "speech-2.5-hd-preview", "text": text, "stream": False,
        "voice_setting": {"voice_id": "female-yujie", "speed": 0.95, "vol": 1.0, "pitch": 0},
        "audio_setting": {"sample_rate": 32000, "bitrate": 128000, "format": "mp3", "channel": 1},
    }, timeout=180)
    audio_hex = (r.json().get("data") or {}).get("audio") or ""
    dest.write_bytes(bytes.fromhex(audio_hex))
    print(f"  tts {dest.name} {dest.stat().st_size//1024} KB", flush=True)
    return dest


def main() -> int:
    seg1 = gen_segment("seg1", "T2V-01", SEG1_PROMPT)
    f1 = last_frame(seg1, WORK / "last1.jpg")
    seg2 = gen_segment("seg2", "MiniMax-Hailuo-02", SEG2_PROMPT, f1, duration=6)
    f2 = last_frame(seg2, WORK / "last2.jpg")
    seg3 = gen_segment("seg3", "MiniMax-Hailuo-02", SEG3_PROMPT, f2, duration=6)

    # 正規化（去掉每段第 1 幀避免接點重複）→ 1920x1080@24
    norm = []
    for i, seg in enumerate((seg1, seg2, seg3), start=1):
        dst = WORK / f"n{i}.mp4"
        vf = "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=24,format=yuv420p,setsar=1"
        pre = [] if i == 1 else ["-vf", "trim=start_frame=1," + vf]
        if i == 1:
            run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(seg), "-vf", vf, "-an",
                 "-c:v", "libx264", "-preset", "fast", "-crf", "18", str(dst)])
        else:
            run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(seg), *pre, "-an",
                 "-c:v", "libx264", "-preset", "fast", "-crf", "18", str(dst)])
        norm.append(dst)

    (WORK / "list.txt").write_text("".join(f"file '{p}'\n" for p in norm), encoding="utf-8")
    silent = EXPORTS / "film2-silent.mp4"
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
         "-i", str(WORK / "list.txt"), "-c", "copy", "-movflags", "+faststart", str(silent)])
    raw_dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                    "-of", "default=noprint_wrappers=1:nokey=1", str(silent)],
                                   capture_output=True, text=True, check=True).stdout.strip())
    dur = f"{min(raw_dur, 15.0):.3f}"
    if raw_dur > 15.0:
        trimmed = WORK / "trimmed.mp4"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(silent),
             "-t", dur, "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-an", str(trimmed)])
        silent = trimmed

    voice = tts(NARRATION, WORK / "vo.mp3")
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi",
         "-i", f"anoisesrc=color=pink:sample_rate=48000:duration={dur}",
         "-af", "highpass=f=350,lowpass=f=7000,volume=0.11", "-c:a", "aac", "-b:a", "128k", str(WORK / "rain.m4a")])
    final = EXPORTS / "film2-1080p.mp4"
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(silent), "-i", str(voice),
         "-i", str(WORK / "rain.m4a"), "-filter_complex",
         f"[1:a]adelay=600|600,volume=1.6[vo];[2:a]volume=0.9[amb];"
         f"[vo][amb]amix=inputs=2:duration=longest:normalize=0,apad,atrim=0:{dur},loudnorm=I=-16:TP=-1.5:LRA=11[a]",
         "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", str(final)])
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", "2", "-i", str(final),
         "-frames:v", "1", str(EXPORTS / "film2-cover.png")])
    print("FINAL", final, dur, final.stat().st_size // 1024, "KB", flush=True)
    print("FILM2-DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
