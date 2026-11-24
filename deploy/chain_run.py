"""鏈式一致性：S01 用角色參考圖，S02–S04 用前一鏡末幀當第一張參考圖。"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import requests

BASE = "http://127.0.0.1:35350"
PID = "0355f16150"
H = {"Content-Type": "application/json", "X-Requested-With": "fetch"}


def post(path: str, payload: dict, timeout: int = 300) -> dict:
    r = requests.post(BASE + path, headers=H, json=payload, timeout=timeout)
    try:
        return r.json()
    except ValueError:
        return {"error": f"HTTP {r.status_code}: {r.text[:200]}"}


def wait_job(jid: str, timeout: int = 900) -> dict:
    t0 = time.time()
    while time.time() - t0 < timeout:
        j = requests.get(f"{BASE}/api/jobs/{jid}", timeout=30).json()["job"]
        if j["state"] in ("succeeded", "error", "failed"):
            return j
        time.sleep(8)
    return {"state": "timeout"}


def main() -> int:
    shots = ["S01", "S02", "S03", "S04"]
    for sid in shots:
        payload = {"chain": True} if sid != "S01" else {}
        img = post(f"/api/projects/{PID}/shots/{sid}/image", payload)
        if img.get("error"):
            print(f"{sid} image ERROR: {img['error'][:160]}", flush=True)
            return 1
        print(f"{sid} image: {img.get('image_url')}", flush=True)

        vid = post(f"/api/projects/{PID}/shots/{sid}/video", {"provider": "minimax", "duration": 6})
        if vid.get("error"):
            print(f"{sid} video ERROR: {vid['error'][:160]}", flush=True)
            return 1
        jid = vid["job"]["id"]
        print(f"{sid} job {jid} task {vid['job'].get('task_id')}", flush=True)
        done = wait_job(jid)
        print(f"{sid} -> {done['state']} {done.get('video') or done.get('message','')[:80]}", flush=True)
        if done["state"] != "succeeded":
            return 1

    # 拼接（無旁白、環境音）
    out = Path("/Users/sky/REACH-AI-Vidio-Studio/exports")
    work = Path("/tmp/chain")
    work.mkdir(parents=True, exist_ok=True)
    media = Path("/Users/sky/REACH-AI-Vidio-Studio/data/media") / PID
    plan = requests.get(f"{BASE}/api/projects/{PID}", timeout=30).json()["plan"]
    clips = [s["video"] for s in plan["shots"] if s.get("video")]
    print("clips:", clips, flush=True)
    for i, f in enumerate(clips, start=1):
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(media / f), "-t", "6",
            "-vf", "scale=1280:720:force_original_aspect_ratio=decrease:flags=lanczos,"
                   "pad=1280:720:(ow-iw)/2:(oh-ih)/2,fps=24,format=yuv420p,setsar=1",
            "-af", "aresample=48000,aformat=channel_layouts=stereo",
            "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-c:a", "aac", "-b:a", "192k",
            str(work / f"0{i}.mp4"),
        ], check=True)
    (work / "list.txt").write_text(
        "".join(f"file '{work / f'0{i}.mp4'}'\n" for i in range(1, len(clips) + 1)), encoding="utf-8")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", str(work / "list.txt"), "-c", "copy", str(work / "cat.mp4")], check=True)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                    "anoisesrc=color=pink:sample_rate=48000:duration=24",
                    "-af", "highpass=f=200,lowpass=f=3200,volume=0.12", "-c:a", "aac", "-b:a", "128k",
                    str(work / "crowd.m4a")], check=True)
    final = out / "nightmarket-chain-24s.mp4"
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(work / "cat.mp4"),
        "-i", str(work / "crowd.m4a"), "-filter_complex",
        "[0:a]volume=1.0[sfx];[1:a]volume=1.0[bed];[sfx][bed]amix=inputs=2:duration=first:normalize=0,"
        "loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=out:st=22.8:d=1.2[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", str(final),
    ], check=True)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", "3", "-i", str(final),
                    "-frames:v", "1", str(out / "nightmarket-chain-cover.png")], check=True)
    print("FINAL", final, final.stat().st_size // 1024, "KB", flush=True)
    print("CHAIN-DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
