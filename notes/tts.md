```python
from openai import OpenAI
from pathlib import Path

# --- Cấu hình ---
AI_API_BASE = "https://api.thucchien.ai"
AI_API_KEY = "sk-1234" # Thay bằng API key của bạn

# --- Thực thi ---
client = OpenAI(
  api_key=AI_API_KEY,
  base_url=AI_API_BASE
)

speech_file_path = Path(__file__).parent / "speech_from_openai.mp3"

response = client.audio.speech.create(
model="gemini-2.5-flash-preview-tts",
voice="Charon",
input="Hôm nay là một ngày đẹp trời để lập trình."
)

response.stream_to_file(speech_file_path)
print(f"File âm thanh đã được lưu tại: {speech_file_path}")
```

# Check giọng: https://aistudio.google.com/generate-speech