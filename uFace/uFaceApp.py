import cv2
import os
import cvzone
import pickle
import numpy as np
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime
import time


#Importando Base de Datos

cred = credentials.Certificate("/Users/juanmonteverde/juanm0nt.dev/myProjects/uFace/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://sistema-de-asistencia-dbed3-default-rtdb.firebaseio.com/",
    "storageBucket":"sistema-de-asistencia-dbed3.appspot.com"
    })

# Captura de Video
capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
imgBackground = cv2.imread("/Users/juanmonteverde/juanm0nt.dev/myProjects/uFace/Resources/background.png")

# Importando los modos de la interfaz en una lista
folderModePath = "/Users/juanmonteverde/juanm0nt.dev/myProjects/uFace/Resources/Modes"
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
# print(len(imgModeList))

# Importanto el archivo generado del encoding y cargandolo al main file
print("Cargando Encode Archivo...")

file = open("/Users/juanmonteverde/juanm0nt.dev/myProjects/uFace/EncodeFile.p", "rb")
encodeListKnownWithIds = pickle.load(file)
file.close()

encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode Archivo Cargado")

bucket = storage.bucket()
modeType = 3
counter = 0
rut = -1
imgStudent = []

# Union de la webcam con la interfaz
while True:
    ret, frame = capture.read()
    imgResize = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    imgResize = cv2.cvtColor(imgResize, cv2.COLOR_BGR2RGB)
    
    # Comparando cara actual con los encodings
    faceCurFrame = face_recognition.face_locations(imgResize)
    encodeCurFrame = face_recognition.face_encodings(imgResize, faceCurFrame)
    
    imgBackground[162:162 + 480,55:55 + 640] = frame
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
    
    if faceCurFrame:
    
        # Comparando encodings y webcam para encontrar coincidencias
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(f"Matches: {matches}")
            # print(f"FaceDistance: {faceDistance}")
            
            # Index especifico el cual se encuentra la coincidencia
            matchIndex = np.argmin(faceDistance)
            # print(f"Match Index: {matchIndex}")
            
            # ID de la persona detectada
            if matches[matchIndex]:
                # print("Rostro Conocido Detectado")
                # print(f"ID Del Estudiante: {studentIds[matchIndex]}")
                
                # Mapeo del rectangulo siguiendo la cara en la webcam
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                boundingRect = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, boundingRect, rt=0)
                rut = studentIds[matchIndex]
                
                if counter == 0:
                    cvzone.putTextRect(imgBackground,"Cargando...", (275,400))
                    cv2.imshow("Sistema de Asistencia", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1
                    
                    
        if counter != 0:
            
            if counter == 1:
                # Obtener Datos
                studentInfo = db.reference(f"Students/{rut}").get()
                # print(studentInfo)
                
                # Obtener la imagen del almacenamiento 
                blob = bucket.get_blob(f"Images/{rut}.png")
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array,cv2.COLOR_BGRA2BGR)
                # Actualizar los datos de asistencia
                dateTimeObject = datetime.strptime(studentInfo["fecha_ultima_asistencia"],
                                                "%Y-%m-%d %H:%M:%S")
                secondPases = (datetime.now()-dateTimeObject).total_seconds()
                print(secondPases)
                

                
                if secondPases >30:
                    ref = db.reference(f"Students/{rut}")
                    studentInfo["asistencia_total"] += 1
                    ref.child("asistencia_total").set(studentInfo["asistencia_total"])
                    ref.child("fecha_ultima_asistencia").set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 0
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            if modeType != 0:
                
                if  10<counter<20:
                    modeType = 2
                    
                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                if counter <=10:
                    # Printeando DATOS en la pantalla
                    cv2.putText(imgBackground,str(studentInfo["asistencia_total"]),(861,125), 
                                cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255), 1)
                    cv2.putText(imgBackground,str(studentInfo["carrera"]),(1005,550), 
                                cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255), 1) 
                    cv2.putText(imgBackground,str(rut),(1005,493),
                                cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255), 1)
                    cv2.putText(imgBackground,str(studentInfo["calidad_estudiante"]),(910,625), 
                                cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100), 1)
                    cv2.putText(imgBackground,str(studentInfo["year"]),(1025,625), 
                                cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100), 1)
                    cv2.putText(imgBackground,str(studentInfo["iniciante_year"]),(1125,625), 
                                cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                    
                    # Centrar nombre
                    (w,h), _ = cv2.getTextSize(studentInfo["nombre"], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset =  (414-w)//2
                    cv2.putText(imgBackground,str(studentInfo["nombre"]),(808+offset,445), 
                                cv2.FONT_HERSHEY_COMPLEX,1,(50,50,50), 1)
                        
                    imgBackground[175:175+216, 909:909+216] = imgStudent
                    
                    
                    
                counter += 1
                
                if counter>=20:
                    counter = 0
                    modeType = 3
                    studentInfo = []
                    imgStudent = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
                               

    else:
        modeType = 3
        counter = 0
                

    # cv2.imshow("Webcam", frame)
    cv2.imshow("Sistema de Asistencia", imgBackground)
    
    if cv2.waitKey(1) == ord("q"):
        break