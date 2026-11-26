"""內建 ComfyUI workflow 預設（依 240 實際節點定義 /object_info 撰寫）。

240 上檔案齊全才會出現在模型清單；不需手動匯出 workflow。
"""

from __future__ import annotations

WAN_NEG = ("色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，"
           "JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，"
           "形态畸形的肢体，手指融合，静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走")


def _flux2(turbo: bool) -> dict:
    model_src = ["1", 0]
    g = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "flux2_dev_fp8mixed.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "mistral_3_small_flux2_bf16.safetensors", "type": "flux2", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "flux2-vae.safetensors"}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": "{{prompt}}", "clip": ["2", 0]}},
        "5": {"class_type": "FluxGuidance", "inputs": {"conditioning": ["4", 0], "guidance": "{{guidance}}"}},
        "7": {"class_type": "RandomNoise", "inputs": {"noise_seed": "{{seed}}"}},
        "8": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
        "9": {"class_type": "Flux2Scheduler", "inputs": {"steps": "{{steps}}", "width": "{{width}}", "height": "{{height}}"}},
        "10": {"class_type": "EmptyFlux2LatentImage", "inputs": {"width": "{{width}}", "height": "{{height}}", "batch_size": 1}},
        "12": {"class_type": "VAEDecode", "inputs": {"samples": ["11", 0], "vae": ["3", 0]}},
        "13": {"class_type": "SaveImage", "inputs": {"images": ["12", 0], "filename_prefix": "REACH/flux2"}},
    }
    if turbo:
        g["14"] = {"class_type": "LoraLoaderModelOnly",
                   "inputs": {"model": ["1", 0], "lora_name": "Flux_2-Turbo-LoRA_comfyui.safetensors", "strength_model": 1.0}}
        model_src = ["14", 0]
    g["6"] = {"class_type": "BasicGuider", "inputs": {"model": model_src, "conditioning": ["5", 0]}}
    g["11"] = {"class_type": "SamplerCustomAdvanced",
               "inputs": {"noise": ["7", 0], "guider": ["6", 0], "sampler": ["8", 0], "sigmas": ["9", 0], "latent_image": ["10", 0]}}
    return g


def _wan22_i2v(fp16: bool = False) -> dict:
    suffix = "fp16" if fp16 else "fp8_scaled"
    te = "umt5_xxl_fp16.safetensors" if fp16 else "umt5_xxl_fp8_e4m3fn_scaled.safetensors"
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": f"wan2.2_i2v_high_noise_14B_{suffix}.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "UNETLoader", "inputs": {"unet_name": f"wan2.2_i2v_low_noise_14B_{suffix}.safetensors", "weight_dtype": "default"}},
        "3": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["1", 0], "lora_name": "wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors", "strength_model": 1.0}},
        "4": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["2", 0], "lora_name": "wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors", "strength_model": 1.0}},
        "5": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["3", 0], "shift": 5.0}},
        "6": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["4", 0], "shift": 5.0}},
        "7": {"class_type": "CLIPLoader", "inputs": {"clip_name": te, "type": "wan", "device": "default"}},
        "8": {"class_type": "VAELoader", "inputs": {"vae_name": "wan_2.1_vae.safetensors"}},
        "9": {"class_type": "CLIPTextEncode", "inputs": {"text": "{{prompt}}", "clip": ["7", 0]}},
        "10": {"class_type": "CLIPTextEncode", "inputs": {"text": "{{negative}}", "clip": ["7", 0]}},
        "11": {"class_type": "LoadImage", "inputs": {"image": "{{image}}"}},
        "12": {"class_type": "WanImageToVideo", "inputs": {
            "positive": ["9", 0], "negative": ["10", 0], "vae": ["8", 0], "start_image": ["11", 0],
            "width": "{{width}}", "height": "{{height}}", "length": "{{frames}}", "batch_size": 1}},
        "13": {"class_type": "KSamplerAdvanced", "inputs": {
            "model": ["5", 0], "add_noise": "enable", "noise_seed": "{{seed}}", "steps": 4, "cfg": 1.0,
            "sampler_name": "euler", "scheduler": "simple", "positive": ["12", 0], "negative": ["12", 1],
            "latent_image": ["12", 2], "start_at_step": 0, "end_at_step": 2, "return_with_leftover_noise": "enable"}},
        "14": {"class_type": "KSamplerAdvanced", "inputs": {
            "model": ["6", 0], "add_noise": "disable", "noise_seed": "{{seed}}", "steps": 4, "cfg": 1.0,
            "sampler_name": "euler", "scheduler": "simple", "positive": ["12", 0], "negative": ["12", 1],
            "latent_image": ["13", 0], "start_at_step": 2, "end_at_step": 10000, "return_with_leftover_noise": "disable"}},
        "15": {"class_type": "VAEDecode", "inputs": {"samples": ["14", 0], "vae": ["8", 0]}},
        "16": {"class_type": "CreateVideo", "inputs": {"images": ["15", 0], "fps": "{{fps}}"}},
        "17": {"class_type": "SaveVideo", "inputs": {"video": ["16", 0], "filename_prefix": "REACH/wan22",
                                                     "format": "auto", "codec": "auto"}},
    }


WAN_NEG = ("色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，"
           "JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，"
           "手指融合，静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走")


def _wan22_t2v() -> dict:
    """Wan 2.2 T2V 14B fp16：高噪 0–2 步構圖、低噪 2–4 步補細節（lightx2v 4 步 LoRA）。"""
    return {
        "1": {"class_type": "CLIPLoader", "inputs": {"clip_name": "umt5_xxl_fp16.safetensors", "type": "wan", "device": "default"}},
        "2": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["1", 0], "text": "{{prompt}}"}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["1", 0], "text": "{{negative}}"}},
        "4": {"class_type": "UNETLoader", "inputs": {"unet_name": "wan2.2_t2v_high_noise_14B_fp16.safetensors", "weight_dtype": "default"}},
        "5": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["4", 0], "lora_name": "wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors", "strength_model": 1.0}},
        "6": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["5", 0], "shift": 5.0}},
        "7": {"class_type": "UNETLoader", "inputs": {"unet_name": "wan2.2_t2v_low_noise_14B_fp16.safetensors", "weight_dtype": "default"}},
        "8": {"class_type": "LoraLoaderModelOnly", "inputs": {"model": ["7", 0], "lora_name": "wan2.2_t2v_lightx2v_4steps_lora_v1.1_low_noise.safetensors", "strength_model": 1.0}},
        "9": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["8", 0], "shift": 5.0}},
        "10": {"class_type": "EmptyHunyuanLatentVideo", "inputs": {"width": "{{width}}", "height": "{{height}}", "length": "{{frames}}", "batch_size": 1}},
        "11": {"class_type": "KSamplerAdvanced", "inputs": {
            "model": ["6", 0], "add_noise": "enable", "noise_seed": "{{seed}}", "steps": 4, "cfg": 1.0,
            "sampler_name": "euler", "scheduler": "simple", "positive": ["2", 0], "negative": ["3", 0],
            "latent_image": ["10", 0], "start_at_step": 0, "end_at_step": 2, "return_with_leftover_noise": "enable"}},
        "12": {"class_type": "KSamplerAdvanced", "inputs": {
            "model": ["9", 0], "add_noise": "disable", "noise_seed": "{{seed}}", "steps": 4, "cfg": 1.0,
            "sampler_name": "euler", "scheduler": "simple", "positive": ["2", 0], "negative": ["3", 0],
            "latent_image": ["11", 0], "start_at_step": 2, "end_at_step": 4, "return_with_leftover_noise": "disable"}},
        "13": {"class_type": "VAELoader", "inputs": {"vae_name": "wan_2.1_vae.safetensors"}},
        "14": {"class_type": "VAEDecode", "inputs": {"samples": ["12", 0], "vae": ["13", 0]}},
        "15": {"class_type": "CreateVideo", "inputs": {"images": ["14", 0], "fps": "{{fps}}"}},
        "16": {"class_type": "SaveVideo", "inputs": {"video": ["15", 0], "filename_prefix": "REACH/wan22t2v", "format": "auto", "codec": "auto"}},
    }


def _wan22_5b() -> dict:
    """Wan 2.2 TI2V 5B fp16：單模型、20 步 cfg 5，走 Wan22ImageToVideoLatent（無首幀＝純文字生影片）。"""
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "wan2.2_ti2v_5B_fp16.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["1", 0], "shift": 8.0}},
        "3": {"class_type": "CLIPLoader", "inputs": {"clip_name": "umt5_xxl_fp16.safetensors", "type": "wan", "device": "default"}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["3", 0], "text": "{{prompt}}"}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["3", 0], "text": "{{negative}}"}},
        "6": {"class_type": "VAELoader", "inputs": {"vae_name": "wan2.2_vae.safetensors"}},
        "7": {"class_type": "Wan22ImageToVideoLatent", "inputs": {
            "vae": ["6", 0], "width": "{{width}}", "height": "{{height}}", "length": "{{frames}}", "batch_size": 1}},
        "8": {"class_type": "KSampler", "inputs": {
            "model": ["2", 0], "seed": "{{seed}}", "steps": 20, "cfg": 5.0, "sampler_name": "uni_pc",
            "scheduler": "simple", "denoise": 1.0, "positive": ["4", 0], "negative": ["5", 0], "latent_image": ["7", 0]}},
        "9": {"class_type": "VAEDecode", "inputs": {"samples": ["8", 0], "vae": ["6", 0]}},
        "10": {"class_type": "CreateVideo", "inputs": {"images": ["9", 0], "fps": "{{fps}}"}},
        "11": {"class_type": "SaveVideo", "inputs": {"video": ["10", 0], "filename_prefix": "REACH/wan22-5b", "format": "auto", "codec": "auto"}},
    }


HY_NEG = ("色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，"
          "JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，"
          "手指融合，静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走")


def _hunyuan15(i2v: bool = False) -> dict:
    """HunyuanVideo 1.5 720p fp16：雙文字編碼器（Qwen2.5-VL + ByT5）、CFGGuider、20 步 24fps。"""
    g = {
        "1": {"class_type": "DualCLIPLoader", "inputs": {"clip_name1": "qwen_2.5_vl_7b_fp8_scaled.safetensors",
                                                        "clip_name2": "byt5_small_glyphxl_fp16.safetensors",
                                                        "type": "hunyuan_video_15", "device": "default"}},
        "2": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["1", 0], "text": "{{prompt}}"}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["1", 0], "text": "{{negative}}"}},
        "4": {"class_type": "UNETLoader", "inputs": {"unet_name": ("hunyuanvideo1.5_720p_i2v_fp16.safetensors" if i2v
                                                                   else "hunyuanvideo1.5_720p_t2v_fp16.safetensors"),
                                                     "weight_dtype": "default"}},
        "5": {"class_type": "ModelSamplingSD3", "inputs": {"model": ["4", 0], "shift": 7.0}},
        "6": {"class_type": "VAELoader", "inputs": {"vae_name": "hunyuanvideo15_vae_fp16.safetensors"}},
        "7": {"class_type": "CFGGuider", "inputs": {"model": ["5", 0], "positive": ["2", 0], "negative": ["3", 0], "cfg": 6.0}},
        "8": {"class_type": "BasicScheduler", "inputs": {"model": ["5", 0], "scheduler": "simple", "steps": 20, "denoise": 1.0}},
        "9": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
        "10": {"class_type": "RandomNoise", "inputs": {"noise_seed": "{{seed}}"}},
        "12": {"class_type": "VAEDecode", "inputs": {"samples": ["15", 0], "vae": ["6", 0]}},
        "13": {"class_type": "CreateVideo", "inputs": {"images": ["12", 0], "fps": "{{fps}}"}},
        "14": {"class_type": "SaveVideo", "inputs": {"video": ["13", 0], "filename_prefix": "REACH/hunyuan15",
                                                     "format": "auto", "codec": "auto"}},
        "15": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["10", 0], "guider": ["7", 0], "sampler": ["9", 0],
                                                                "sigmas": ["8", 0], "latent_image": ["11", 0]}},
    }
    if i2v:
        g["16"] = {"class_type": "LoadImage", "inputs": {"image": "{{image}}"}}
        g["17"] = {"class_type": "CLIPVisionLoader", "inputs": {"clip_name": "sigclip_vision_patch14_384.safetensors"}}
        g["18"] = {"class_type": "CLIPVisionEncode", "inputs": {"clip_vision": ["17", 0], "image": ["16", 0], "crop": "center"}}
        g["11"] = {"class_type": "HunyuanVideo15ImageToVideo", "inputs": {
            "positive": ["2", 0], "negative": ["3", 0], "vae": ["6", 0], "width": "{{width}}", "height": "{{height}}",
            "length": "{{frames}}", "batch_size": 1, "start_image": ["16", 0], "clip_vision_output": ["18", 0]}}
        g["7"]["inputs"]["positive"] = ["11", 0]
        g["7"]["inputs"]["negative"] = ["11", 1]
        g["15"]["inputs"]["latent_image"] = ["11", 2]
    else:
        g["11"] = {"class_type": "EmptyHunyuanVideo15Latent", "inputs": {
            "width": "{{width}}", "height": "{{height}}", "length": "{{frames}}", "batch_size": 1}}
    return g


LTX_NEG = "pc game, console game, video game, cartoon, childish, ugly, blurry, low quality, watermark, text"

LTX_SIGMAS_8 = "1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0"


def _ltx25() -> dict:
    """LTX 2.5 22B distilled int8：8 步蒸餾 sigma、AV 聯合潛空間、內建音訊（對白/環境音一起生）。"""
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors",
                                                     "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "gemma4-12b-with-proj-ltx-2.5-bf16.safetensors",
                                                     "type": "ltxv", "device": "default"}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": "{{prompt}}"}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": "{{negative}}"}},
        "5": {"class_type": "LTXVConditioning", "inputs": {"positive": ["3", 0], "negative": ["4", 0], "frame_rate": "{{fps}}"}},
        "6": {"class_type": "VAELoader", "inputs": {"vae_name": "ltx-2.5-video-vae-bf16.safetensors"}},
        "7": {"class_type": "VAELoader", "inputs": {"vae_name": "ltx-2.5-audio-vae-bf16.safetensors"}},
        "8": {"class_type": "EmptyLTXVLatentVideo", "inputs": {"width": "{{width}}", "height": "{{height}}",
                                                               "length": "{{frames}}", "batch_size": 1}},
        "9": {"class_type": "LTXVEmptyLatentAudio", "inputs": {"frames_number": "{{frames}}", "frame_rate": "{{fps}}",
                                                               "batch_size": 1, "audio_vae": ["7", 0]}},
        "10": {"class_type": "LTXVConcatAVLatent", "inputs": {"video_latent": ["8", 0], "audio_latent": ["9", 0]}},
        "11": {"class_type": "LTXVDualCFGGuider", "inputs": {"model": ["1", 0], "positive": ["5", 0], "negative": ["5", 1],
                                                             "video_cfg": 1.0, "audio_cfg": 1.0}},
        "12": {"class_type": "ManualSigmas", "inputs": {"sigmas": LTX_SIGMAS_8}},
        "13": {"class_type": "RandomNoise", "inputs": {"noise_seed": "{{seed}}"}},
        "14": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler_ancestral"}},
        "15": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["13", 0], "guider": ["11", 0], "sampler": ["14", 0],
                                                                 "sigmas": ["12", 0], "latent_image": ["10", 0]}},
        "16": {"class_type": "LTXVSeparateAVLatent", "inputs": {"av_latent": ["15", 0]}},
        "17": {"class_type": "VAEDecode", "inputs": {"samples": ["16", 0], "vae": ["6", 0]}},
        "18": {"class_type": "LTXVAudioVAEDecode", "inputs": {"samples": ["16", 1], "audio_vae": ["7", 0]}},
        "19": {"class_type": "CreateVideo", "inputs": {"images": ["17", 0], "fps": "{{fps}}", "audio": ["18", 0]}},
        "20": {"class_type": "SaveVideo", "inputs": {"video": ["19", 0], "filename_prefix": "REACH/ltx25",
                                                     "format": "auto", "codec": "auto"}},
    }


def _ltx25_dev() -> dict:
    """LTX 2.5 22B dev bf16 高畫質版：30 步 + LTXVScheduler(token 感知 shift) + 雙 CFG(影片 3.0 / 音訊 7.0)。"""
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "ltx-2.5-22b-dev-transformer-bf16.safetensors",
                                                     "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "gemma4-12b-with-proj-ltx-2.5-bf16.safetensors",
                                                     "type": "ltxv", "device": "default"}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": "{{prompt}}"}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": "{{negative}}"}},
        "5": {"class_type": "LTXVConditioning", "inputs": {"positive": ["3", 0], "negative": ["4", 0], "frame_rate": "{{fps}}"}},
        "6": {"class_type": "VAELoader", "inputs": {"vae_name": "ltx-2.5-video-vae-bf16.safetensors"}},
        "7": {"class_type": "VAELoader", "inputs": {"vae_name": "ltx-2.5-audio-vae-bf16.safetensors"}},
        "8": {"class_type": "EmptyLTXVLatentVideo", "inputs": {"width": "{{width}}", "height": "{{height}}",
                                                               "length": "{{frames}}", "batch_size": 1}},
        "9": {"class_type": "LTXVEmptyLatentAudio", "inputs": {"frames_number": "{{frames}}", "frame_rate": "{{fps}}",
                                                               "batch_size": 1, "audio_vae": ["7", 0]}},
        "10": {"class_type": "LTXVConcatAVLatent", "inputs": {"video_latent": ["8", 0], "audio_latent": ["9", 0]}},
        "11": {"class_type": "LTXVDualCFGGuider", "inputs": {"model": ["1", 0], "positive": ["5", 0], "negative": ["5", 1],
                                                             "video_cfg": "{{vcfg}}", "audio_cfg": "{{acfg}}"}},
        "12": {"class_type": "LTXVScheduler", "inputs": {"steps": "{{steps}}", "max_shift": 2.05, "base_shift": 0.95,
                                                         "stretch": True, "terminal": 0.1, "latent": ["10", 0]}},
        "13": {"class_type": "RandomNoise", "inputs": {"noise_seed": "{{seed}}"}},
        "14": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler_ancestral"}},
        "15": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["13", 0], "guider": ["11", 0], "sampler": ["14", 0],
                                                                 "sigmas": ["12", 0], "latent_image": ["10", 0]}},
        "16": {"class_type": "LTXVSeparateAVLatent", "inputs": {"av_latent": ["15", 0]}},
        "17": {"class_type": "VAEDecode", "inputs": {"samples": ["16", 0], "vae": ["6", 0]}},
        "18": {"class_type": "LTXVAudioVAEDecode", "inputs": {"samples": ["16", 1], "audio_vae": ["7", 0]}},
        "19": {"class_type": "CreateVideo", "inputs": {"images": ["17", 0], "fps": "{{fps}}", "audio": ["18", 0]}},
        "20": {"class_type": "SaveVideo", "inputs": {"video": ["19", 0], "filename_prefix": "REACH/ltx25dev",
                                                     "format": "auto", "codec": "auto"}},
    }


QWEN_NEG = "低质量，模糊，噪点，变形，多余的手指，错误的比例，过曝，水印，文字残留"

def _qwen21_t2i() -> dict:
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "qwen_image_2.1_bf16.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "QwenImage21Cache", "inputs": {"model": ["1", 0], "device": "auto", "dtype": "default"}},
        "3": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen3vl_8b_bf16.safetensors", "type": "qwen_image", "device": "default"}},
        "4": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_2.1_vae_bf16.safetensors"}},
        "5": {"class_type": "TextEncodeQwenImage21", "inputs": {
            "clip": ["3", 0], "prompt": "{{prompt}}", "negative_prompt": "{{negative}}",
            "resolution": 1024, "images": [], "vae": ["4", 0]}},
        "6": {"class_type": "EmptyLatentImage", "inputs": {"width": "{{width}}", "height": "{{height}}", "batch_size": 1}},
        "7": {"class_type": "KSampler", "inputs": {
            "model": ["2", 0], "positive": ["5", 0], "negative": ["5", 1], "latent_image": ["6", 0],
            "seed": "{{seed}}", "steps": "{{steps}}", "cfg": "{{cfg}}",
            "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["4", 0]}},
        "9": {"class_type": "SaveImage", "inputs": {"images": ["8", 0], "filename_prefix": "REACH/qwen21"}},
    }


def _qwen_edit(fast: bool) -> dict:
    model_src = ["1", 0]
    g = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "qwen_image_edit_2511_bf16.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_2.5_vl_7b_fp8_scaled.safetensors", "type": "qwen_image"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_vae.safetensors"}},
        "4": {"class_type": "LoadImage", "inputs": {"image": "{{image}}"}},
        "5": {"class_type": "FluxKontextImageScale", "inputs": {"image": ["4", 0]}},
        "6": {"class_type": "TextEncodeQwenImageEditPlus", "inputs": {
            "clip": ["2", 0], "prompt": "{{prompt}}", "vae": ["3", 0], "image1": ["5", 0]}},
        "7": {"class_type": "TextEncodeQwenImageEditPlus", "inputs": {
            "clip": ["2", 0], "prompt": "{{negative}}", "vae": ["3", 0], "image1": ["5", 0]}},
        "8": {"class_type": "VAEEncode", "inputs": {"pixels": ["5", 0], "vae": ["3", 0]}},
    }
    if fast:
        g["10"] = {"class_type": "LoraLoaderModelOnly",
                   "inputs": {"model": ["1", 0], "lora_name": "Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors",
                              "strength_model": 1.0}}
        model_src = ["10", 0]
    g["11"] = {"class_type": "ModelSamplingAuraFlow", "inputs": {"model": model_src, "shift": 3.1}}
    g["12"] = {"class_type": "CFGNorm", "inputs": {"model": ["11", 0], "strength": 1.0}}
    g["13"] = {"class_type": "KSampler", "inputs": {
        "model": ["12", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["8", 0],
        "seed": "{{seed}}", "steps": "{{steps}}", "cfg": "{{cfg}}",
        "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0}}
    g["14"] = {"class_type": "VAEDecode", "inputs": {"samples": ["13", 0], "vae": ["3", 0]}}
    g["15"] = {"class_type": "SaveImage", "inputs": {"images": ["14", 0], "filename_prefix": "REACH/qwen-edit"}}
    return g


def _minimax_h3_i2v(hi: bool = False) -> dict:
    """首幀 → 影片＋聲音。寬高由首幀比例自動推算（約 0.9MP），幀數對齊 17k+5。"""
    unet = "minimax_h3_fl2va_bf16.safetensors" if hi else "minimax_h3_fl2va_pruned_int8_convrot.safetensors"
    vae = "minimax_h3_video_vae_fp16.safetensors" if hi else "minimax_h3_video_vae_int8_convrot.safetensors"
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": unet, "weight_dtype": "default"}},
        "2": {"class_type": "LoraLoaderModelOnly", "inputs": {
            "model": ["1", 0], "lora_name": "minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors", "strength_model": 1.0}},
        "3": {"class_type": "BasicGuider", "inputs": {"model": ["2", 0], "conditioning": ["7", 0]}},
        "4": {"class_type": "BasicScheduler", "inputs": {"model": ["2", 0], "scheduler": "simple", "steps": "{{steps}}", "denoise": 1.0}},
        "5": {"class_type": "RandomNoise", "inputs": {"noise_seed": "{{seed}}"}},
        "6": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "res_multistep"}},
        "8": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", "type": "minimax", "device": "default"}},
        "9": {"class_type": "VAELoader", "inputs": {"vae_name": vae}},
        "16": {"class_type": "VAELoader", "inputs": {"vae_name": "minimax_h3_audio_vae_fp32.safetensors"}},
        "13": {"class_type": "LoadImage", "inputs": {"image": "{{image}}"}},
        "14": {"class_type": "ImageScaleToTotalPixels", "inputs": {
            "image": ["13", 0], "upscale_method": "nearest-exact", "megapixels": 0.9, "resolution_steps": 32}},
        "20": {"class_type": "GetImageSize", "inputs": {"image": ["14", 0]}},
        # 高 32 對齊、面積 ~0.9MP
        "21": {"class_type": "ComfyMathExpression", "inputs": {
            "expression": "round(sqrt(900000 * b / a) / 32) * 32", "values.a": ["20", 0], "values.b": ["20", 1]}},
        "22": {"class_type": "ComfyMathExpression", "inputs": {
            "expression": "round(a * b / c / 32) * 32", "values.a": ["21", 0], "values.b": ["20", 0], "values.c": ["20", 1]}},
        "25": {"class_type": "PrimitiveInt", "inputs": {"value": "{{frames}}"}},
        # 幀數對齊：n → n + (5 - n % 17) % 17
        "24": {"class_type": "ComfyMathExpression", "inputs": {
            "expression": "max(5, a) + (5 - (max(5, a) % 17)) % 17", "values.a": ["25", 0]}},
        "7": {"class_type": "MiniMaxH3ImageToVideo", "inputs": {
            "clip": ["8", 0], "vae": ["9", 0], "prompt": "{{prompt}}",
            "width": ["22", 1], "height": ["21", 1], "length": ["24", 1], "first_frame": ["14", 0]}},
        "10": {"class_type": "SamplerCustomAdvanced", "inputs": {
            "noise": ["5", 0], "guider": ["3", 0], "sampler": ["6", 0], "sigmas": ["4", 0], "latent_image": ["7", 1]}},
        "11": {"class_type": "VAEDecode", "inputs": {"samples": ["10", 0], "vae": ["9", 0]}},
        "15": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["10", 0], "vae": ["16", 0]}},
        "17": {"class_type": "CreateVideo", "inputs": {"images": ["11", 0], "audio": ["15", 0], "fps": "{{fps}}"}},
        "18": {"class_type": "SaveVideo", "inputs": {"video": ["17", 0], "filename_prefix": "REACH/h3", "format": "auto", "codec": "auto"}},
    }


def _minimax_h3_r2v(hi: bool = False) -> dict:
    """參考圖 → 影片＋聲音（ref2va）。角色／風格參考，不是首幀；prompt 用 <Picture 1> 指涉參考圖。"""
    unet = "minimax_h3_ref2va_bf16.safetensors" if hi else "minimax_h3_ref2va_pruned_int8_convrot.safetensors"
    clip = "qwen3vl_32b_minimax_h3_bf16.safetensors" if hi else "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors"
    vae = "minimax_h3_video_vae_fp16.safetensors" if hi else "minimax_h3_video_vae_int8_convrot.safetensors"
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": unet, "weight_dtype": "default"}},
        "3": {"class_type": "BasicGuider", "inputs": {"model": ["1", 0], "conditioning": ["7", 0]}},
        "4": {"class_type": "BasicScheduler", "inputs": {"model": ["1", 0], "scheduler": "simple", "steps": "{{steps}}", "denoise": 1.0}},
        "5": {"class_type": "RandomNoise", "inputs": {"noise_seed": "{{seed}}"}},
        "6": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "res_multistep"}},
        "8": {"class_type": "CLIPLoader", "inputs": {"clip_name": clip, "type": "minimax", "device": "default"}},
        "9": {"class_type": "VAELoader", "inputs": {"vae_name": vae}},
        "16": {"class_type": "VAELoader", "inputs": {"vae_name": "minimax_h3_audio_vae_fp32.safetensors"}},
        "13": {"class_type": "LoadImage", "inputs": {"image": "{{image}}"}},
        "14": {"class_type": "ImageScaleToTotalPixels", "inputs": {
            "image": ["13", 0], "upscale_method": "nearest-exact", "megapixels": 0.9, "resolution_steps": 32}},
        "20": {"class_type": "GetImageSize", "inputs": {"image": ["14", 0]}},
        # 高 32 對齊、面積 ~0.9MP
        "21": {"class_type": "ComfyMathExpression", "inputs": {
            "expression": "round(sqrt(900000 * b / a) / 32) * 32", "values.a": ["20", 0], "values.b": ["20", 1]}},
        "22": {"class_type": "ComfyMathExpression", "inputs": {
            "expression": "round(a * b / c / 32) * 32", "values.a": ["21", 0], "values.b": ["20", 0], "values.c": ["20", 1]}},
        "25": {"class_type": "PrimitiveInt", "inputs": {"value": "{{frames}}"}},
        # 幀數對齊：n → n + (5 - n % 17) % 17
        "24": {"class_type": "ComfyMathExpression", "inputs": {
            "expression": "max(5, a) + (5 - (max(5, a) % 17)) % 17", "values.a": ["25", 0]}},
        "7": {"class_type": "MiniMaxH3ReferenceToVideo", "inputs": {
            "clip": ["8", 0], "prompt": "{{prompt}}",
            "width": ["22", 1], "height": ["21", 1], "length": ["24", 1], "ref_image_size": "{{ref_size}}",
            "vae": ["9", 0], "audio_vae": ["16", 0], "ref_images": {"ref_image_0": ["14", 0]}}},
        "10": {"class_type": "SamplerCustomAdvanced", "inputs": {
            "noise": ["5", 0], "guider": ["3", 0], "sampler": ["6", 0], "sigmas": ["4", 0], "latent_image": ["7", 1]}},
        "11": {"class_type": "VAEDecode", "inputs": {"samples": ["10", 0], "vae": ["9", 0]}},
        "15": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["10", 0], "vae": ["16", 0]}},
        "17": {"class_type": "CreateVideo", "inputs": {"images": ["11", 0], "audio": ["15", 0], "fps": "{{fps}}"}},
        "18": {"class_type": "SaveVideo", "inputs": {"video": ["17", 0], "filename_prefix": "REACH/h3r2v", "format": "auto", "codec": "auto"}},
    }


# 預設 workflow（不依賴字典順序；comfyui.default() 讀這裡，缺件才退回第一個）
DEFAULT_BY_KIND: dict[str, str] = {"image": "flux2-dev", "video": "wan22-i2v"}

PRESETS: dict[str, dict] = {
    "flux2-dev": {
        "kind": "image", "note": "內建｜Flux.2 Dev fp8，20 步，品質優先",
        "requires": {"diffusion_models": ["flux2_dev_fp8mixed.safetensors"],
                     "text_encoders": ["mistral_3_small_flux2_bf16.safetensors"], "vae": ["flux2-vae.safetensors"]},
        "defaults": {"steps": 20, "guidance": 4.0, "width": 1024, "height": 1024},
        "size_multiple": 16, "build": lambda: _flux2(False),
    },
    "flux2-turbo": {
        "kind": "image", "note": "內建｜Flux.2 Dev + Turbo LoRA，8 步，速度優先",
        "requires": {"diffusion_models": ["flux2_dev_fp8mixed.safetensors"],
                     "text_encoders": ["mistral_3_small_flux2_bf16.safetensors"], "vae": ["flux2-vae.safetensors"],
                     "loras": ["Flux_2-Turbo-LoRA_comfyui.safetensors"]},
        "defaults": {"steps": 8, "guidance": 4.0, "width": 1024, "height": 1024},
        "size_multiple": 16, "build": lambda: _flux2(True),
    },
    "ltx-25-t2v": {
        "kind": "video", "note": "內建｜LTX 2.5 22B distilled int8，8 步；文字生影片含同步音訊，mp4 24fps",
        "requires": {"diffusion_models": ["ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors"],
                     "text_encoders": ["gemma4-12b-with-proj-ltx-2.5-bf16.safetensors"],
                     "vae": ["ltx-2.5-video-vae-bf16.safetensors", "ltx-2.5-audio-vae-bf16.safetensors"]},
        "defaults": {"fps": 24.0, "negative": LTX_NEG, "width": 1280, "height": 720, "frames": 97, "steps": 8},
        "frame_multiple": 8, "size_multiple": 32, "timeout": 3600, "build": _ltx25,
    },
    "ltx-25-t2v-hq": {
        "kind": "video", "note": "內建｜LTX 2.5 22B dev bf16，40 步 + 雙 CFG；畫質優先，含音訊，mp4 24fps",
        "requires": {"diffusion_models": ["ltx-2.5-22b-dev-transformer-bf16.safetensors"],
                     "text_encoders": ["gemma4-12b-with-proj-ltx-2.5-bf16.safetensors"],
                     "vae": ["ltx-2.5-video-vae-bf16.safetensors", "ltx-2.5-audio-vae-bf16.safetensors"]},
        "defaults": {"fps": 24.0, "negative": LTX_NEG + ", letterbox, black bars",
                     "width": 1280, "height": 720, "frames": 97, "steps": 40, "vcfg": 3.0, "acfg": 7.0},
        "frame_multiple": 8, "size_multiple": 32, "timeout": 3600, "build": _ltx25_dev,
    },
    "hunyuan15-t2v": {
        "kind": "video", "note": "內建｜HunyuanVideo 1.5 720p fp16，20 步；文字生影片，mp4 24fps",
        "requires": {"diffusion_models": ["hunyuanvideo1.5_720p_t2v_fp16.safetensors"],
                     "text_encoders": ["qwen_2.5_vl_7b_fp8_scaled.safetensors", "byt5_small_glyphxl_fp16.safetensors"],
                     "vae": ["hunyuanvideo15_vae_fp16.safetensors"]},
        "defaults": {"fps": 24.0, "negative": HY_NEG, "width": 1280, "height": 720, "frames": 121, "steps": 20},
        "frame_multiple": 4, "size_multiple": 16, "timeout": 3600, "build": lambda: _hunyuan15(False),
    },
    "hunyuan15-i2v": {
        "kind": "video", "note": "內建｜HunyuanVideo 1.5 720p fp16 i2v（SigLIP 影像理解）；需首幀；mp4 24fps",
        "requires": {"diffusion_models": ["hunyuanvideo1.5_720p_i2v_fp16.safetensors"],
                     "text_encoders": ["qwen_2.5_vl_7b_fp8_scaled.safetensors", "byt5_small_glyphxl_fp16.safetensors"],
                     "vae": ["hunyuanvideo15_vae_fp16.safetensors"],
                     "clip_vision": ["sigclip_vision_patch14_384.safetensors"]},
        "defaults": {"fps": 24.0, "negative": HY_NEG, "width": 1280, "height": 720, "frames": 121, "steps": 20},
        "frame_multiple": 4, "size_multiple": 16, "timeout": 3600, "build": lambda: _hunyuan15(True),
    },
    "wan22-5b-fast": {
        "kind": "video", "note": "內建｜Wan2.2 TI2V 5B fp16，20 步；最省顯存的草稿引擎，mp4 24fps",
        "requires": {"diffusion_models": ["wan2.2_ti2v_5B_fp16.safetensors"],
                     "text_encoders": ["umt5_xxl_fp16.safetensors"], "vae": ["wan2.2_vae.safetensors"]},
        "defaults": {"fps": 24.0, "negative": WAN_NEG, "width": 1280, "height": 704, "frames": 121},
        "frame_multiple": 4, "size_multiple": 16, "timeout": 1800, "build": _wan22_5b,
    },
    "wan22-t2v": {
        "kind": "video", "note": "內建｜Wan2.2 T2V 14B fp16 + lightx2v 4 步；純文字生影片，mp4 16fps",
        "requires": {"diffusion_models": ["wan2.2_t2v_high_noise_14B_fp16.safetensors",
                                          "wan2.2_t2v_low_noise_14B_fp16.safetensors"],
                     "loras": ["wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors",
                               "wan2.2_t2v_lightx2v_4steps_lora_v1.1_low_noise.safetensors"],
                     "text_encoders": ["umt5_xxl_fp16.safetensors"], "vae": ["wan_2.1_vae.safetensors"]},
        "defaults": {"fps": 16.0, "negative": WAN_NEG, "width": 832, "height": 480, "frames": 49},
        "frame_multiple": 4, "size_multiple": 16, "timeout": 1800, "build": _wan22_t2v,
    },
    "wan22-i2v-hq": {
        "kind": "video", "note": "內建｜Wan2.2 I2V 14B fp16（畫質版）+ lightx2v 4 步；需首幀；mp4 16fps",
        "requires": {"diffusion_models": ["wan2.2_i2v_high_noise_14B_fp16.safetensors",
                                          "wan2.2_i2v_low_noise_14B_fp16.safetensors"],
                     "loras": ["wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors",
                               "wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors"],
                     "text_encoders": ["umt5_xxl_fp16.safetensors"], "vae": ["wan_2.1_vae.safetensors"]},
        "defaults": {"fps": 16.0, "negative": WAN_NEG, "width": 832, "height": 480, "frames": 81},
        "frame_multiple": 4, "size_multiple": 16, "timeout": 1800, "build": lambda: _wan22_i2v(True),
    },
    "wan22-i2v": {
        "kind": "video", "note": "內建｜Wan2.2 I2V 14B fp8 + lightx2v 4 步；需首幀（關鍵影格）；mp4 16fps",
        "requires": {"diffusion_models": ["wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors",
                                          "wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors"],
                     "loras": ["wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors",
                               "wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors"],
                     "text_encoders": ["umt5_xxl_fp8_e4m3fn_scaled.safetensors"], "vae": ["wan_2.1_vae.safetensors"]},
        "defaults": {"fps": 16.0, "negative": WAN_NEG, "width": 832, "height": 480, "frames": 81},
        "frame_multiple": 4, "size_multiple": 16, "build": _wan22_i2v,
    },
    "qwen-image-21": {
        "kind": "image", "note": "內建｜Qwen-Image 2.1 文生圖，25 步；中文字卡與版式最強",
        "requires": {"diffusion_models": ["qwen_image_2.1_bf16.safetensors"],
                     "text_encoders": ["qwen3vl_8b_bf16.safetensors"], "vae": ["qwen_image_2.1_vae_bf16.safetensors"]},
        "defaults": {"steps": 25, "cfg": 1.0, "negative": QWEN_NEG, "width": 1024, "height": 1024},
        "size_multiple": 16, "timeout": 600, "build": _qwen21_t2i,
    },
    "qwen-image-edit-2511": {
        "kind": "image", "note": "內建｜Qwen-Image-Edit 2511 指令改圖，8 步 cfg 2.5；需參考圖（角色一致、換鏡位）",
        "requires": {"diffusion_models": ["qwen_image_edit_2511_bf16.safetensors"],
                     "text_encoders": ["qwen_2.5_vl_7b_fp8_scaled.safetensors"], "vae": ["qwen_image_vae.safetensors"]},
        "defaults": {"steps": 8, "cfg": 2.5, "negative": "", "width": 1024, "height": 1024},
        "size_multiple": 16, "timeout": 600, "build": lambda: _qwen_edit(False),
    },
    "qwen-image-edit-2511-fast": {
        "kind": "image", "note": "內建｜Edit 2511 + Lightning 4 步 LoRA，cfg 1.0；模型已載入時約 3 秒",
        "requires": {"diffusion_models": ["qwen_image_edit_2511_bf16.safetensors"],
                     "text_encoders": ["qwen_2.5_vl_7b_fp8_scaled.safetensors"], "vae": ["qwen_image_vae.safetensors"],
                     "loras": ["Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors"]},
        "defaults": {"steps": 4, "cfg": 1.0, "negative": "", "width": 1024, "height": 1024},
        "size_multiple": 16, "timeout": 600, "build": lambda: _qwen_edit(True),
    },
    "minimax-h3-i2v": {
        "kind": "video", "note": "內建｜MiniMax H3 首幀→影片＋原生音訊，turbo 8 步；寬高依首幀自動、輸出 mp4 24fps",
        "requires": {"diffusion_models": ["minimax_h3_fl2va_pruned_int8_convrot.safetensors"],
                     "text_encoders": ["qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors"],
                     "vae": ["minimax_h3_video_vae_int8_convrot.safetensors", "minimax_h3_audio_vae_fp32.safetensors"],
                     "loras": ["minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors"]},
        "defaults": {"fps": 24.0, "steps": 8, "width": 1344, "height": 768, "frames": 56},
        "size_multiple": 32, "timeout": 1800, "build": lambda: _minimax_h3_i2v(False),
    },
    "minimax-h3-i2v-hq": {
        "kind": "video", "note": "內建｜MiniMax H3 bf16 高畫質版（較慢、吃顯存）；其餘同上",
        "requires": {"diffusion_models": ["minimax_h3_fl2va_bf16.safetensors"],
                     "text_encoders": ["qwen3vl_32b_minimax_h3_bf16.safetensors"],
                     "vae": ["minimax_h3_video_vae_fp16.safetensors", "minimax_h3_audio_vae_fp32.safetensors"],
                     "loras": ["minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors"]},
        "defaults": {"fps": 24.0, "steps": 8, "width": 1344, "height": 768, "frames": 56},
        "size_multiple": 32, "timeout": 2400, "build": lambda: _minimax_h3_i2v(True),
    },
    "minimax-h3-r2v": {
        "kind": "video", "note": "內建｜MiniMax H3 參考圖→影片＋聲音（角色連戲）；prompt 用 <Picture 1>；mp4 24fps",
        "requires": {"diffusion_models": ["minimax_h3_ref2va_pruned_int8_convrot.safetensors"],
                     "text_encoders": ["qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors"],
                     "vae": ["minimax_h3_video_vae_int8_convrot.safetensors", "minimax_h3_audio_vae_fp32.safetensors"]},
        "defaults": {"fps": 24.0, "steps": 20, "width": 1344, "height": 768, "frames": 56, "ref_size": "match"},
        "size_multiple": 32, "timeout": 2400, "build": lambda: _minimax_h3_r2v(False),
    },
    "minimax-h3-r2v-hq": {
        "kind": "video", "note": "內建｜MiniMax H3 bf16 參考圖→影片（較慢、吃顯存）；其餘同上",
        "requires": {"diffusion_models": ["minimax_h3_ref2va_bf16.safetensors"],
                     "text_encoders": ["qwen3vl_32b_minimax_h3_bf16.safetensors"],
                     "vae": ["minimax_h3_video_vae_fp16.safetensors", "minimax_h3_audio_vae_fp32.safetensors"]},
        "defaults": {"fps": 24.0, "steps": 20, "width": 1344, "height": 768, "frames": 56, "ref_size": "match"},
        "size_multiple": 32, "timeout": 3000, "build": lambda: _minimax_h3_r2v(True),
    },
}


def available(installed: dict) -> list[str]:
    return [pid for pid, p in PRESETS.items()
            if all(f in (installed.get(folder) or []) for folder, files in p["requires"].items() for f in files)]


def spec(pid: str) -> dict:
    p = PRESETS[pid]
    out = {"id": pid, "kind": p["kind"], "status": "builtin", "note": p["note"], "defaults": dict(p["defaults"]),
           "size_multiple": p.get("size_multiple", 16), "workflow": p["build"]()}
    if p.get("frame_multiple"):
        out["frame_multiple"] = p["frame_multiple"]
    return out
