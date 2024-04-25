from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

def draw_text(image_path, text, font_scale=1, font_thickness=2):
    # โหลดภาพ
    image = cv2.imread(image_path)
    
    # สร้างภาพ PIL
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    # กำหนดฟอนต์
    font_path = 'static/font/Prompt-Regular.ttf'
    font = ImageFont.truetype(font_path, size=40)
    # วาดข้อความลงบนภาพ
    draw.text((50, 50), text, fill=(255, 255, 255), font=font)
    
    # แปลงภาพกลับเป็นภาพ Numpy
    image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    
    # แสดงข้อความด้วย OpenCV
    cv2.putText(image_with_text, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)
    
    return image_with_text

# เรียกใช้งาน
image_path = "static/img/banner_count_game.png"
text = "Sample sสวัสดเีText"
position = (100, 100)
result_image = draw_text(image_path, text, position)

# แสดงภาพ
cv2.imshow("Image with Text", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
