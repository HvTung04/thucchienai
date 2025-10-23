import requests
import base64
from pathlib import Path
import wave

# --- Cấu hình ---
API_URL = "https://api.thucchien.ai/gemini/v1beta/models/gemini-2.5-pro-preview-tts:generateContent"
AI_API_KEY = "sk-_L5p4n0oPzdMhkMFZh8clA" # Thay bằng API key của bạn

content = """
Thùy Linh: Quý vị và các bạn thân mến, câu chuyện của bác Long có lẽ cũng là câu chuyện của rất nhiều những người lính đã đi qua năm tháng chiến tranh. Những vết thương trên da thịt có thể lành, nhưng những vết sẹo trong tâm hồn vẫn luôn âm ỉ. Đôi khi, tất cả những gì họ cần không phải là lời khuyên "hãy quên đi", mà là một không gian an toàn để được lắng nghe, được thấu hiểu và được sẻ chia. "Đối thoại với ký ức" xin được khép lại số hôm nay tại đây. Cảm ơn sự quan tâm theo dõi của quý vị. Xin chào và hẹn gặp lại trong những số tiếp theo.
"""

# --- Dữ liệu ---
data = {
  "contents": [{
    "parts": [
      {"text": """Người tư vấn Thùy Linh có giọng nói ấm áp, lễ phép, chuyên nghiệp, giọng Sài Gòn. Cựu chiến binh già yếu 70 tuổi nói giọng Hà Nội, giọng nói trầm, có chút mệt mỏi, giọng phù hợp để chia sẻ kinh nghiệm sống:\n{0}""".format(content)}
    ]
  }],
  "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [{
              "speaker": "Thùy Linh",
              "voiceConfig": {
                "prebuiltVoiceConfig": {
                  "voiceName": "Zephyr"
                }
              }
            }, {
              "speaker": "Quốc Long",
              "voiceConfig": {
                "prebuiltVoiceConfig": {
                  "voiceName": "Algieba"
                }
              }
            }]
        }
      }
  }
}

# --- Headers ---
headers = {
    'x-goog-api-key': AI_API_KEY,
    'Content-Type': 'application/json'
}

# --- Thực thi ---
try:
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()  # Ném lỗi nếu request không thành công (status code không phải 2xx)

    response_data = response.json()

    # --- Xử lý phản hồi ---
    if 'candidates' in response_data and response_data['candidates']:
        candidate = response_data['candidates'][0]
        if 'content' in candidate and 'parts' in candidate['content'] and candidate['content']['parts']:
            part = candidate['content']['parts'][0]
            if 'inlineData' in part and 'data' in part['inlineData']:
                audio_data_base64 = part['inlineData']['data']
                
                # Giải mã base64
                audio_bytes = base64.b64decode(audio_data_base64)
                
                # Lưu file âm thanh
                output_path = Path("src/v0_part6.wav")
                
                # Ghi file WAV
                with wave.open(str(output_path), 'wb') as wf:
                    wf.setnchannels(1)  # Mono
                    wf.setsampwidth(2)  # 16-bit PCM (L16)
                    wf.setframerate(24000) # 24kHz sample rate
                    wf.writeframes(audio_bytes)
                
                print(f"Đã lưu file âm thanh thành công tại: {output_path}")
            else:
                print("Không tìm thấy 'inlineData' hoặc 'data' trong phản hồi.")
        else:
            print("Không tìm thấy 'content' hoặc 'parts' trong phản hồi.")
    else:
        print("Không tìm thấy 'candidates' trong phản hồi.")

except requests.exceptions.RequestException as e:
    print(f"Lỗi khi gọi API: {e}")
except KeyError as e:
    print(f"Lỗi khi xử lý JSON response: không tìm thấy key {e}")
except Exception as e:
    print(f"Đã có lỗi xảy ra: {e}")
