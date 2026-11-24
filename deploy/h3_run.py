"""MiniMax-H3 fused-turbo 測試：繞過 SLA / ChunkFF 自訂節點。"""
import json, time, urllib.request, uuid
BASE = "http://127.0.0.1:8188"
PROMPT = (
    "integrated_multimodal_description: A young woman holding a transparent umbrella walks slowly "
    "through a neon-lit rainy alley at night, reflections ripple on wet pavement, cinematic medium shot.\n"
    "overall_soundscape: steady rain, distant traffic hum, soft footsteps in puddles.\n"
    "non_diegetic_music: warm ambient synth pads, slow tempo."
)
W, H, LEN = 512, 288, 90  # 3.75s @24fps（先求跑通，成功再放大）

wf = {
    "127": {"class_type": "UNETLoader", "inputs": {
        "unet_name": "minimax_h3_fused_refdelta_r1024_turbo8_mystic07_int8_convrot.safetensors",
        "weight_dtype": "default"}},
    "142": {"class_type": "MiniMaxH3SigmaShift", "inputs": {
        "model": ["127", 0], "shift_video": 12.0, "shift_audio": 3.0}},
    "124": {"class_type": "BasicScheduler", "inputs": {
        "model": ["142", 0], "scheduler": "simple", "steps": 4, "denoise": 1.0}},
    "126": {"class_type": "BasicGuider", "inputs": {"model": ["142", 0], "conditioning": ["131", 0]}},
    "128": {"class_type": "CLIPLoader", "inputs": {
        "clip_name": "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", "type": "minimax"}},
    "119": {"class_type": "VAELoader", "inputs": {"vae_name": "minimax_h3_video_vae_int8_convrot.safetensors"}},
    "120": {"class_type": "VAELoader", "inputs": {"vae_name": "minimax_h3_audio_vae_fp32.safetensors"}},
    "131": {"class_type": "MiniMaxH3ImageToVideo", "inputs": {
        "clip": ["128", 0], "vae": ["119", 0], "prompt": PROMPT,
        "width": W, "height": H, "length": LEN}},
    "129": {"class_type": "RandomNoise", "inputs": {"noise_seed": 42}},
    "135": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "res_multistep"}},
    "125": {"class_type": "SamplerCustomAdvanced", "inputs": {
        "noise": ["129", 0], "guider": ["126", 0], "sampler": ["135", 0],
        "sigmas": ["124", 0], "latent_image": ["131", 1]}},
    "122": {"class_type": "VAEDecode", "inputs": {"samples": ["125", 0], "vae": ["119", 0]}},
    "121": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["125", 0], "vae": ["120", 0]}},
    "130": {"class_type": "CreateVideo", "inputs": {"images": ["122", 0], "audio": ["121", 0], "fps": 24}},
    "92": {"class_type": "SaveVideo", "inputs": {
        "video": ["130", 0], "filename_prefix": "video/h3_fused_test", "format": "auto"}},
}


def main() -> int:
    req = urllib.request.Request(
        BASE + "/prompt",
        data=json.dumps({"prompt": wf, "client_id": uuid.uuid4().hex}).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        pid = json.loads(urllib.request.urlopen(req, timeout=60).read())["prompt_id"]
    except urllib.error.HTTPError as exc:
        print("SUBMIT-FAIL", exc.code)
        print(exc.read().decode()[:1200])
        return 1
    print("prompt_id", pid, flush=True)
    t0 = time.time()
    while time.time() - t0 < 5400:
        h = json.loads(urllib.request.urlopen(f"{BASE}/history/{pid}", timeout=30).read())
        if pid in h:
            it = h[pid]
            print("elapsed_s", round(time.time() - t0, 1))
            print("status", it.get("status", {}).get("status_str"))
            for m in it.get("status", {}).get("messages", []):
                if m[0] == "execution_error":
                    print("ERR node", m[1].get("node_type"), str(m[1].get("exception_message"))[:400])
            print("outputs", json.dumps(it.get("outputs", {}))[:600])
            return 0
        time.sleep(10)
    print("TIMEOUT")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
