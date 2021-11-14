# YOLO v3를 이용해 80종의 다양한 물체를 빠르게 인식하고 표시해 주는 프로그램
# 카메라로 거리 풍경을 비춰가며 사람이나 자동차가 움직이는 것을 검출해보기
# 키보드의 q를 누르면 프로그램이 종료됨
import cv2
import numpy as np

cap = cv2.VideoCapture(0)    ################### 카메라 영상을 가져오기 위한 기본 코드: 0은 첫번째 카메라 
whT =320              # 폭과 높이의 크기(픽셀 수)
confThreshold = 0.5   # 물체 인식을 위한 기준 확률(0.5보다 크면 인식된 것으로 간주) 
nmsThreshold = 0.3    # Non-Maximun suppression 영상 엣지를 찾기위한 효율적 방법
                      # 많은 물체를 인식할 때 연산량을 줄여줌. 기준 픽셀의 주변값 비교, 최대치만 살림

classesFile = 'coco.names'   # 80종의 물체의 분류명이 기록된 파일
classNames = []
with open(classesFile, 'rt') as f:  # coco.names의 텍스트를 'rt' read text로 읽어옴
    classNames = f.read().rstrip('\n').split('\n')
    # print(classNames)             # 80개의 분류명이 표기되는 것을 확인
    # print(len(classNames))        # 80으로 표시됨을 확인

modelConfiguration = 'yolov3-tiny.cfg'   # yolo version3의 cfg파일, weights파일을 불러오기
modelWeights = 'yolov3-tiny.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)  # 네트워크 설정
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)                # openCV의 DNN네트웍을 사용
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)                     # GPU 사용 없이 CPU만을 사용

def findObjects(outputs, img):
    hT, wT, cT = img.shape  # 물체의 높이, 폭, 중심점의 위치
    bbox = []               # Bounding Box
    classIDs = []           # 물체 번호
    confs = []              # 인식 확률

    for output in outputs:
        for det in output:     # det(detection)
            scores = det[5:]   # 85개의 정보중 위치..확률의 맨 앞 5개의 정보는 버림.  
            classID = np.argmax(scores)  # 뒤쪽의 80개 물체 Id 중 인식 확률이 가장 높은 것을 고름.
            confidence = scores[classID]     # 인식 확률이 가장 높은 물체의 실제 인식된 확률 
            if confidence > confThreshold:   # 인식 확률이 기준 확률(여기서는 0.5)보다 높다면
                # 앞의 5개 정보 중 3번째의 폭 정보와 4번째의 높이 정보에 실제 픽셀을 곱해서 중심점의 좌표를 구함.
                w, h = int(det[2]*wT), int(det[3]*hT)   
                # 앞의 5개 정보 중 1번째의 중심점 x좌표와 2번째의 y좌표에 실제 픽셀을 곱해서 중심점의 좌표를 구함.
                x, y = int(det[0]*wT-w/2), int(det[1]*hT-h/2)  # 폭과 높이의 절반값을 빼서 실제 중심점의 좌표를 구함.
                bbox.append([x,y,w,h])
                classIDs.append(classID)
                confs.append(float(confidence))
    # print(len(bbox))
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)
    for i in indices:    # 인식된 모든 물체의 바운딩 박스와 물체명, 확률을 표시하기 위한 코드
        i = i[0]
        box = bbox[i]
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,255), 2)  # 바운딩 박스 표시
        cv2.putText(img, f'{classNames[classIDs[i]].upper()} {int(confs[i]*100)}%',  # 확률과 물체의 이름을 대문자로 표시
                    (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,255), 2)  # 바운딩박스 윗부분에 두께2, 오렌지색으로 표시

while True:
    success, img = cap.read() ################### 카메라 영상을 가져오기 위한 기본 코드
    # image를 blob(Binary Large Object)으로 변환
    blob = cv2.dnn.blobFromImage(img, 1/255, (whT, whT), [0,0,0], 1, crop=False) 
    net.setInput(blob)
    layerNames = net.getLayerNames()
    # print(layerNames)
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()] # layer에서 출력 부분을 추출해 냄.
    # print(outputNames)
    # print(net.getUnconnectedOutLayers())
    outputs = net.forward(outputNames)
    # print(outputs[0].shape)     # (300, 85)  (바운딩박스의 갯수, (x위치, y위치, 폭, 높이, 확률, 80개 물체 인식확률))
    # print(outputs[1].shape)     # (1200, 85) (No of Bounding Boxes, (cx, cy, w, h, confidence, 80 Objects))
    # print(outputs[2].shape)     # (4800, 85)  shape of output.png를 참조하세요.
    # print(outputs[0][0])        # x위치, y위치, 폭, 높이, 확률, 80개 물체 인식된 확률

    findObjects(outputs, img)

    cv2.imshow('Image', img)  ################### 카메라 영상을 가져오기 위한 기본 코드
    if cv2.waitKey(1) & 0xFF ==ord('q'):     ############ 키보드의 q 키가 입력되면 정지
        break