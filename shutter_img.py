# ประกาศตัวแปรที่จำเป็น
confirm_timer = True  # ตัวแปรเพื่อยืนยันการนับถอยหลัง
timer_started = False  # ตัวแปรเพื่อตรวจสอบว่านับถอยหลังเริ่มต้นหรือไม่
start_stop = True  # ตัวแปรเพื่อแสดงถึงการเริ่มหรือหยุดการนับถอยหลัง
start_stop_continue = False  # ตัวแปรเพื่อตรวจสอบว่าการเริ่มหรือหยุดการนับถอยหลังยังคงดำเนินการอยู่หรือไม่
countdown_time = 60  # เวลาที่กำหนดในการนับถอยหลัง (วินาที)
pause_requested = False  # ตัวแปรเพื่อตรวจสอบว่ามีคำขอให้หยุดชั่วคราวหรือไม่
timer_paused = False  # ตัวแปรเพื่อแสดงถึงการหยุดชั่วคราวของการนับถอยหลัง
pause_time = 0  # เวลาที่เก็บไว้เมื่อการหยุดชั่วคราวเกิดขึ้น
resume_requested = False  # ตัวแปรเพื่อตรวจสอบว่ามีคำขอให้ดำเนินการต่อหลังจากการหยุดชั่วคราวหรือไม่

# เงื่อนไขสำหรับการหยุดชั่วคราว
if confirm_timer:
    if not timer_started:
        if start_stop:
            start_time = cv2.getTickCount()
            start_stop_continue = False
        timer_started = True
    current_time = cv2.getTickCount()

    # Check if pausing is requested
    if pause_requested:
        if not timer_paused:
            pause_time = cv2.getTickCount()
            timer_paused = True
        pause_duration = (cv2.getTickCount() - pause_time) / cv2.getTickFrequency()
        elapsed_time += pause_duration  # Add pause duration to elapsed time
        pause_requested = False  # Reset pause request flag
    else:
        # Check if resuming is requested
        if resume_requested:
            if timer_paused:
                resume_time = cv2.getTickCount()
                pause_duration = (resume_time - pause_time) / cv2.getTickFrequency()
                start_time += pause_duration  # Adjust start time to resume
                timer_paused = False
            resume_requested = False  # Reset resume request flag

    elapsed_time = (current_time - start_time) / cv2.getTickFrequency()
    remaining_time = max(0, countdown_time - elapsed_time)
    remaining_time_continue = remaining_time

text = f"Time left: {int(remaining_time_continue)} seconds"
self.draw_text(frame, text, (frame.shape[1] // 2, 50))
