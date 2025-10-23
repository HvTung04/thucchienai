```python
from openai import OpenAI
import base64

# --- Cấu hình ---
AI_API_BASE = "https://api.thucchien.ai/v1"
AI_API_KEY = "<your_api_key>"

# --- Khởi tạo client ---
client = OpenAI(
  api_key=AI_API_KEY,
  base_url=AI_API_BASE
)

# --- Gọi API để tạo hình ảnh ---
response = client.images.generate(
  model="imagen-4",
  prompt="An astronaut riding a horse on Mars, photorealistic",
  n=2, # Yêu cầu 2 ảnh
)

# --- Xử lý và lưu từng ảnh ---
for i, image_obj in enumerate(response.data):
  b64_data = image_obj.b64_json
  image_data = base64.b64decode(b64_data)
  
  save_path = f"generated_image_{i+1}.png"
  with open(save_path, 'wb') as f:
      f.write(image_data)
  print(f"Image saved to {save_path}")
```

```python
from openai import OpenAI
import base64

# --- Cấu hình ---
AI_API_BASE = "https://api.thucchien.ai/v1"
AI_API_KEY = "<your_api_key>" # Thay bằng API key của bạn
IMAGE_SAVE_PATH = "generated_chat_image.png"

# --- Khởi tạo client ---
client = OpenAI(
  api_key=AI_API_KEY,
  base_url=AI_API_BASE,
)

# --- Bước 1: Gọi API để tạo hình ảnh ---
try:
  response = client.chat.completions.create(
      model="gemini-2.5-flash-image-preview",
      messages=[
          {
              "role": "user",
              "content": "A detailed illustration of a vintage steam train crossing a mountain bridge. High resolution, photorealistic, 8k"
          }
      ],
      modalities=["image"]  # Chỉ định trả về dữ liệu ảnh
  )

  # Trích xuất dữ liệu ảnh base64
  base64_string = response.choices[0].message.images[0].get('image_url').get("url")
  print("Image data received successfully.")

  # --- Bước 2: Giải mã và lưu hình ảnh ---
  if ',' in base64_string:
      header, encoded = base64_string.split(',', 1)
  else:
      encoded = base64_string

  image_data = base64.b64decode(encoded)

  with open(IMAGE_SAVE_PATH, 'wb') as f:
      f.write(image_data)
      
  print(f"Image saved to {IMAGE_SAVE_PATH}")

except Exception as e:
  print(f"An error occurred: {e}")
```