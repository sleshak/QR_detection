import cv2
from pyzbar.pyzbar import decode

target_qr_code = "БЭК основной"

cap = cv2.VideoCapture('assets\образец №2.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    decoded_objects = decode(blurred_frame)

    found = False
    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        if qr_data == target_qr_code:
            print("Нужный QR-код найден:", qr_data)
            found = True
            print("Позиция QR-кода:", obj.rect)

if found == False:
    print("Нужный QR-код не найден.")

cap.release()
cv2.destroyAllWindows()
