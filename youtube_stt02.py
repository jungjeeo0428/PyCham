from pathlib import Path
import os
import torch
import whisper
import yt_dlp
from whisper.utils import get_writer

# 현재 스크립트 실행 위치를 ffmpeg 경로로 지정
current_dir = Path(__file__).parent.resolve()
os.environ["PATH"] += os.pathsep + str(current_dir)

# ── 1. 기본 설정 ──────────────────────────────
url = "YouTube URL"
print(f"처리할 URL: {url}")

model_name = "base"   # 필요 시 small, medium 등으로 변경
language = "ko"       # 한국어: ko / 영어: en / 자동 감지: None

output_dir = current_dir / "stt_result"
output_dir.mkdir(parents=True, exist_ok=True)


# ── 2. YouTube 음성 다운로드 + WAV 변환 ────────
options = {
    "format": "bestaudio/best",
    "outtmpl": str(output_dir / "%(id)s.%(ext)s"),
    "noplaylist": True,
    "ffmpeg_location": str(current_dir),  # ffmpeg 및 ffprobe가 위치한 폴더 지정
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
        }
    ],
}

with yt_dlp.YoutubeDL(options) as ydl:
    info = ydl.extract_info(url, download=True)
    wav_path = Path(ydl.prepare_filename(info)).with_suffix(".wav")

if not wav_path.is_file():
    raise FileNotFoundError(f"WAV 파일이 생성되지 않았습니다: {wav_path}")

print(f"\nWAV 저장 완료: {wav_path}")


# ── 3. Whisper로 음성 → 텍스트 변환 ────────────
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"사용 장치: {device}")

model = whisper.load_model(model_name, device=device)

result = model.transcribe(
    str(wav_path),
    language=language,
    task="transcribe",
    fp16=(device == "cuda"),
    verbose=True,
)


# ── 4. 텍스트와 자막 저장 ──────────────────────
for file_format in ("txt", "srt"):
    writer = get_writer(file_format, str(output_dir))
    writer(result, str(wav_path))

print("\n전체 인식 결과:")
print(result["text"])

print(f"\n결과 저장 위치: {output_dir.resolve()}")