import cv2
import time


def video_processing():
    cap = cv2.VideoCapture(0)
    down_points = (576, 324)
    file = open('res', 'w')
    file.write('lower_left_x, lower_left_y, upper_right_x, upper_right_y\n')
    img = cv2.imread('fly64.png', cv2.IMREAD_UNCHANGED)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img_res = cv2.resize(img, (w, h))
            for c in range(0, 3):
                frame[y:y + h, x:x + w, c] = (img_res[:, :, c] *
                                              (img_res[:, :, 3] / 255.0) + frame[y:y + h, x:x + w, c] *
                                              (1.0 - img_res[:, :, 3] / 255.0))
            file.write(str(x) + ',' + str(y) + ',' + str(x + w) + ',' + str(y + h) + '\n')
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.1)
    file.close()
    cap.release()


if __name__ == '__main__':
    video_processing()

cv2.waitKey(0)
cv2.destroyAllWindows()