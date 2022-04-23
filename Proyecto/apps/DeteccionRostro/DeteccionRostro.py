import cv2
import os
import numpy as np
import imutils
from matplotlib import image

def CAPTURANDO(name):
    
    personName = name
    dataPath = 'apps/DeteccionRostro/datos/' #rutas 
    personPath = dataPath + '/' + personName

    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #con este accedemos a la webcam
    #cap = cv2.VideoCapture('Vanessa.mp4')

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0

    while True:

        ret, frame = cap.read()
        if ret == False: break
        frame =  imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)
            count = count + 1
        cv2.imshow('frame',frame)

        k =  cv2.waitKey(1)
        if k == 2 or count >= 20:
            break

    cap.release()
    cv2.destroyAllWindows()

def ENTRENANDO(name):
    dataPath = 'apps/DeteccionRostro/datos/' + name
    peopleList = os.listdir(dataPath)
    print('Lista de personas: ', peopleList)

    labels = []
    facesData = []
    label = 0



    for fileName in peopleList:
        print('Rostros: ', dataPath + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(dataPath+'/'+fileName,0))
        image = cv2.imread(dataPath+'/'+fileName,0)
        #cv2.imshow('image',image)
        #cv2.waitKey(10)
    label = label + 1

    #print('labels= ',labels)
    #print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))
    #print('Número de etiquetas 1: ',np.count_nonzero(np.array(labels)==1))

    # Métodos para entrenar el reconocedor

    face_recognizer = cv2.face.EigenFaceRecognizer_create()  #parametros de 5k
    #face_recognizer = cv2.face.FisherFaceRecognizer_create() #parametros de 500
    #face_recognizer = cv2.face.LBPHFaceRecognizer_create()   # parametros de 70

    # Entrenando el reconocedor de rostros
    print("Entrenando...")
    face_recognizer.train(facesData, np.array(labels))

    # Almacenando el modelo obtenido
    face_recognizer.write('modeloEigenFace.xml')
    #face_recognizer.write('modeloFisherFace.xml')
    #face_recognizer.write('modeloLBPHFace.xml')
    print("Modelo almacenado...")
    print("")


def RECONOCIENDO():
    dataPath = 'apps/DeteccionRostro/datos/' 
    imagePaths = os.listdir(dataPath)
    print('imagePaths=',imagePaths)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    #face_recognizer = cv2.face.FisherFaceRecognizer_create()
    #face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Leyendo el modelo
    face_recognizer.read('modeloEigenFace.xml')
    #face_recognizer.read('modeloFisherFace.xml')
    #face_recognizer.read('modeloLBPHFace.xml')

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #Este sirve para encender la camara
    #cap = cv2.VideoCapture('Emma.mp4')

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    while True:
        ret,frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            # EigenFaces
            if result[1] < 3165:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                cap.release()
                cv2.destroyAllWindows()
                return print("adios")
                
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if k == 27:
            break