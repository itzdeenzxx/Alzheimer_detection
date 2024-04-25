from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

# โหลดภาพ
image = cv2.imread("static/img/banner_count_game.png")

# โหลดภาพโดยใช้ PIL
pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# สร้างอ็อบเจ็กต์ ImageDraw
draw = ImageDraw.Draw(pil_image)

# โหลดฟอนต์ที่ต้องการใช้
font_path = 'static/font/Prompt-Regular.ttf'
font = ImageFont.truetype(font_path, size=40)  # เลือกขนาดฟอนต์ตามที่ต้องการ

# แสดงข้อความบนภาพโดยใช้ฟอนต์ที่กำหนด
text = "สวัสดี OpenCV"
draw.text((50, 50), text, fill=(255, 255, 255), font=font)

# แปลงภาพกลับเป็นภาพ OpenCV
image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

# แสดงภาพ
cv2.imshow("Image", image_with_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
