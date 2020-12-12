import cv2
from deepface import DeepFace

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Can not open webcam")

while True:
    ret, frame = cap.read()

    result = DeepFace.analyze(frame, actions=['dominant_emotion'])

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX




    cv2.imshow('Original Video', frame)

    plt.style.use('fivethirtyeight')

    x_vals = []
    y_vals = dt.no

    index = count()


    def animate(i):

        x = range(1, 60)
        y1 = y_vals

        plt.cla()

        plt.plot(x, y1, label='Channel 1')

        plt.legend(loc='upper left')
        plt.tight_layout()


    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.tight_layout()
    plt.show()

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()