import glob
from typing import Dict, List, Set, Tuple, Any
import mysql.connector
import datetime
import face_recognition
from datetime import datetime
import tkinter as tk
import cv2
import numpy as np
from PIL import Image
import os

WEB_CAM = 0
conn = mysql.connector.connect(host="localhost", database="sms", user="root")
cursor = conn.cursor()

class Window:
    def __init__(self):
        # Creating a Tkinter GUI Window
        window = tk.Tk()
        window.title("Attendance System")
        # window.geometry('920x720')
        window.configure(background='light green')
        window.grid_rowconfigure(1, weight=3)
        window.grid_columnconfigure(1, weight=3)

        label1 = tk.Label(window, background="light blue", fg="black", text="Name :", width=10, height=1,
                          font=('Helvetica', 16))
        label1.grid(row=0, column=0)

        self.std_name = tk.Entry(window, background="yellow", fg="black", width=45, font=('Helvetica', 14))
        self.std_name.grid(row=0, column=1)

        clearBtn1 = tk.Button(window, background="light blue", command=self.clear, fg="black", text="CLEAR", width=8,
                              height=1,
                              activebackground="light blue", font=('Helvetica', 10))
        clearBtn1.grid(row=0, column=2)

        self.label4 = tk.Label(window, background="yellow", fg="black", width=75, height=4,
                               font=('Helvetica', 14, 'italic'))
        self.label4.grid(row=1, columnspan=3)

        takeImageBtn = tk.Button(window, command=self.takeImage, background="yellow", fg="black",
                                 text="CAPTURE NEW IMAGE \n Add a new student image",
                                 activebackground="light blue",
                                 width=40, height=3, font=('Helvetica', 12))
        takeImageBtn.grid(row=2, columnspan=3)

        cropimagebtn = tk.Button(window, command=self.cropimage, background="yellow", fg="black",
                                 text="CROP CAPTURED IMAGE \n Crop the added image",
                                 activebackground="red",
                                 width=40, height=3, font=('Helvetica', 12))
        cropimagebtn.grid(row=3, columnspan=3)

        takeattendancebtn = tk.Button(window, command=self.takeattendance, background="yellow", fg="black",
                                      text="TAKE ATTENDANCE \n Start taking attendance of all students that come in frame",
                                      activebackground="red",
                                      width=40, height=3, font=('Helvetica', 12))
        takeattendancebtn.grid(row=4, columnspan=3)

        self.window = window

    def clear(self):
        self.std_name.delete(0, 'end')
        res = ""
        self.label4.configure(text=res)

    def takeImage(self):
        name = (self.std_name.get())
        if name.isalpha():
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0

            cam = cv2.VideoCapture(WEB_CAM)
            cam.read()  # First image is full and very dark
            ret, img = cam.read()  # Read just one image from the cam
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.1, 1)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum = sampleNum + 1

            # store the captured image
            cv2.imwrite(os.path.join('ImagesAttendance', f'{name}.jpg'), gray)
            cv2.putText(img, 'Press q or esp to close image', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                        cv2.LINE_AA)
            cv2.imshow('Add student image to the database', img)

            while True:
                k = cv2.waitKey(1)  # change the value from the original 0 (wait forever) to something appropriate
                if k == 27 or k == 113:
                    cv2.destroyAllWindows()
                    break

            cam.release()

            # print the student name and id after a successful face capturing
            res = f'Image of student {name} saved. \n' \
                  f'Now when you take attendance, it will also match this new image.'

            # Check if mysql has this name
            cursor.execute('SELECT name from students;')
            students: List[Tuple[Any]] = cursor.fetchall()
            students: List[str] = [tup[0] for tup in students]
            if name not in students:
                res += f'\n Note: {name} is not present in the students database. \n' \
                       f'Add this name using admin login otherwise his attendance will not be shown in system'

            # row = [roll_number, name]
            # with open('studentDetailss.csv', 'a+') as csvFile:
            #     writer = csv.writer(csvFile)
            #     writer.writerow(row)
            self.label4.configure(text=res)
        else:
            res = "Name entered is not alphanumeric. Reenter the name."
            self.label4.configure(text=res)

    def getImagesAndLabels(self, path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        Ids = []
        for imagePath in imagePaths:
            pilImage = Image.open(imagePath).convert('L')
            imageNp = np.array(pilImage, 'uint8')
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids

    def cropimage(self):
        name = (self.std_name.get())
        img_path = os.path.join('ImagesAttendance', f'{name}.jpg')

        # Read image
        im = cv2.imread(img_path)

        # Select ROI
        r = cv2.selectROI(windowName='Select Face', img=im)

        # Crop image
        imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

        # Display cropped image
        cv2.imshow("Image", imCrop)

        # Overwrite the image file
        cv2.imwrite(img_path, imCrop)

        cv2.destroyAllWindows()

    def takeattendance(self):
        path = 'ImagesAttendance'
        images = []
        classNames = []
        for img_path in glob.glob(os.path.join(path, '*.jpg')):
            curImg = cv2.imread(img_path)
            images.append(curImg)
            name = os.path.splitext(os.path.basename(img_path))[0]
            classNames.append(name.strip())
        print(classNames)

        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        def markAttendance(name):
            now = datetime.now()
            CurrentDate = now.strftime("%Y-%m-%d")
            # f.writelines(f'\n{name},{dtString},{CurrentDate}')
            print('Yo. You dont reach here')
            sql = "INSERT INTO attendance (name, date) VALUES (%s, %s)"
            val = (name, CurrentDate)
            cursor.execute(sql, val)
            print('reached here')
            conn.commit()

        encodeListKnown = findEncodings(images)
        print('Encoding Complete')

        cap = cv2.VideoCapture(WEB_CAM)

        people_present: Set[str] = set()
        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches: List[np.ndarray] = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis: np.ndarray = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    # Matched with a face is found in the dataset
                    name = classNames[matchIndex].strip()
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    if name not in people_present:
                        markAttendance(name)
                        people_present.add(name)

            cv2.putText(img, 'Press q or esp to close image', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                        cv2.LINE_AA)
            cv2.imshow('Take attendance of all people present in image', img)
            k = cv2.waitKey(100) & 0xFF
            if k == 27 or k == 113:
                cv2.destroyAllWindows()
                break

    def show_window(self):
        self.window.mainloop()


def main():
    Window().show_window()


if __name__ == '__main__':
    main()
