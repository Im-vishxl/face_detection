import cv2

face_cap = cv2.CascadeClassifier("C:/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.XML")

video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()             #capturing the video
    col = cv2.cvtColor(video_data, cv2.COLOR_BGRA2GRAY)   #convert the video to black and white
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,                       #factor for face detection
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for(x, y, w, h) in faces:                     #for drawing the box on the capture
        cv2.rectangle(video_data, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(video_data, 'vishal', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    cv2.imshow("video_live", video_data)         #displays the video with face detection
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release()