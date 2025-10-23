```python
from openai import OpenAI

# --- Cấu hình ---
# Thay <your_api_key> bằng API key của bạn
client = OpenAI(
  api_key="<your_api_key>",
  base_url="https://api.thucchien.ai"
)

# --- Thực thi ---
response = client.chat.completions.create(
  model="gemini-2.5-pro", # Chọn model bạn muốn gemini-2.5-flash
  messages=[
      {
          "role": "user",
          "content": "Explain the concept of API gateway in simple terms."
      }
  ]
)

print(response.choices[0].message.content)
```