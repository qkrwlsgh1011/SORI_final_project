# :musical_note: Project 우리 알리미 'SORI' 

<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/228908423-65d2812a-8034-43fd-979c-3553052841f8.PNG" width="200"></p>

<div align="center">
저시력자들을 위한 음성고지서 서비스 SORI입니다. 
데모 버전입니다.
</div>

------------------------------

<br>

</br>

## 💁 팀 구성  
|  팀  | 멤버     |      
|:-----:|:----------:|
|조장 김의석|<img src="https://user-images.githubusercontent.com/119566469/228912270-95157db4-8d2e-4a63-8f1c-a3bce062ec18.JPG" width = 150>| 
|객체팀(Text Detection(Yolov5)) <br>이한재  최성주|<img src="https://user-images.githubusercontent.com/119566469/228913186-aa0d59e6-6462-46b3-8282-2e1dd2f580f6.JPG" width = 150><img src="https://user-images.githubusercontent.com/119566469/228913198-ad1cc97e-0937-4b73-ac8d-be3912bec12c.JPG" width = 150>|
|텍스트팀(Text Recognition(Pytesseract)) <br> 김의석 박진호|<img src="https://user-images.githubusercontent.com/119566469/228912270-95157db4-8d2e-4a63-8f1c-a3bce062ec18.JPG" width = 150><img src="https://user-images.githubusercontent.com/119566469/228914447-d2da8896-61c8-4e38-83b2-d8bce609a2cf.JPG" width = 150>|
|보이스팀(Voice(TensorflowTTS)) <br> 고준성 김수윤|<img src="https://user-images.githubusercontent.com/119566469/228914919-0eefb368-1855-4d2b-8a5b-0925407c42c1.JPG" width = 150><img src="https://user-images.githubusercontent.com/119566469/228914945-2e90b14a-2cf5-4e6e-a9a9-b68444df74f4.JPG" width = 150>|
|웹팀(Web) 최성주|<img src="https://user-images.githubusercontent.com/119566469/228913198-ad1cc97e-0937-4b73-ac8d-be3912bec12c.JPG" width = 150>| 
------------------------------------

## :cloud: 아이디어 구상 
저시력자들을 대상으로 QR코드를 이용하여 고지서의 내용을 음성으로 전환해주는 서비스가 존재하나 몇가지 문제로 서비스의 제한이 많아 무용지물 상태라는 뉴스를 보았습니다.<br>
저희는 QR코드가 아닌 고지서 전체를 찍으면 음성으로 안내해주는 서비스를 도전했습니다.


<br>

</br>

## 📜 사용환경
### Languege 
- Python
### Text Detection
- CUDA 11.2 - torch 1.7.1 - torchvision 0.8.2
- Fine tuning form YoloV5 pretrained weights
- opencv - Python 4.7.0.72

### Text Recognition
- tesseract 5.3.0

### Voice 
- Window 11
- WSL2: Ubuntu 22.04 LTS
- Python>=3.8 
- GPU: GeforceRTX 3080ti
- CPU: AMD Ryzen 7 5800X 8-Core Processor
- RAM == 64.0GB 

<br>

</br>


<br>

</br>

## 🔄 프로세스 

<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/229003876-f67ae56d-af04-422c-93e7-f673e48c5fc7.png" width="700"></p>

- 초기 서비스 프로세스 입니다.
    -  초기 : webcam으로 data 전달 : 화질 저하로 인한 OCR인식 불가 
    -  현재 : image/video로 data 전달 
    

<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/228916839-1d6f27be-d9d0-4688-85bf-0997adb0bf93.PNG" width="700"></p>

- Text Detection : Yolov5 모델을 사용해 Image의 원하는 부분을 추출
<br>

- Text Recognition : Pytesseract를 사용해 Text Detection을 통해 나온 이미지의 글자를 추출
<br>

- Voice : TensorflowTTS를 사용해 Text Recognition의 글자들을 음성으로 생성

---------------------------------------

<br>

</br>


## 🛠️ 모델 기능별 구현

### Text Detection
- YoloV5는 실시간 객체인식 분야에서 yolo는 one-stage detector로써 two-stage detector모델들에 비해 추론속도와 모델크기에 있어서 강점
<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/229000082-dea4e659-79df-4f6a-b794-616eeb740a13.png" width="700"></p>


- 고지서 내의 핵심 내용이 담긴 영역을 YoloV5를 통해 가져온다.

<div>
  <img src="https://user-images.githubusercontent.com/119566469/228919068-51ccc13f-e757-4ea7-b8fc-1337cbcd6475.PNG" width="300">
  <img src="https://user-images.githubusercontent.com/119566469/228919992-b880bd03-b3d2-478e-b6e5-329a1a85edda.png" width="308">
</div>


<br>

</br>
 
<div>
  <img src="https://user-images.githubusercontent.com/119566469/228921514-4743c267-1819-4b32-8585-d9bde7988923.jpg" width="300">
</div>

<br>
</br>

### Text Recognition
- 두 가지 Model fine tuning(TrOCR, CRNN)과 Library(EasyOCR, Tesseract)의 성능 비교를 통해 최종적으로 Tesseract를 사용하여 프로젝트 진행
<div>
  <img src="https://user-images.githubusercontent.com/119566469/229001108-1b5b6a1a-a3aa-4f88-a210-9846bfa557dd.jpeg" width="300">
  <img src="https://user-images.githubusercontent.com/119566469/229001112-6e5bebda-0f0e-481d-88ed-725add778a0a.png" width="300">
  <img src="https://user-images.githubusercontent.com/119566469/229001115-695b8651-479e-4b31-9eb1-1825415986c5.png" width="300">
</div>

- 라이브러리 선정 후 추가적인 학습과 이미지 전처리를 통해 인식률을 높임

<br>
</br>

### Voice 
- Tortoise 등 여러 TTS 모델이 있으나 한국어를 지원 하지 않거나 라이브러리 호환 문제로 TACOTRON2, FastSpeech2를 기반으로 모델 사용
<div>
  <img src="https://user-images.githubusercontent.com/119566469/229001350-f2a81d9e-4d30-4fa2-b863-f7b82986536f.png" width="600">
</div>

- 프로토타입 모델 구현 전 TACOTRON2 기반으로 Language : KOR 선택이 가능하도록 설계된 TeonsorFlowTTS의 업데이트로 인한 의존성 문제로 TeonsorFlowTTS의 FastSpeech2 모델 사용을 최종적으로 결정

<br>
</br>

### Web
- Flask를 사용한 웹 구현 방법 
<div>
  <img src="https://user-images.githubusercontent.com/119566469/229002030-e59b1196-05cc-42ed-8648-46f93e80c6bc.png" width="800">
</div>

1. Client가 image/video를 선택해 로컬 서버에 전송
2. 받은 image/video를 로컬 서버에 포함된 Yolov5모델(학습되어있는)에 전달하여 예측값을 추출
3. 추출한 image를 Pytesseract를 사용하여 원하는 text를 image에서 추출
4. 추출한 text를 Docker Cotainer안에 있는 Tensorflowtts에 전달하고 다시 음성파일로 로컬 서버에 전달
5. 전달받은 음성파일을 로컬 서버에서 Client에 음성으로 전달

-----------------------------------------


<br>
</br>

## 👾 기능별 오류 및 해결

### Text Detection 
- 테스트 데이터 구성을 위해 웹크롤링으로 고지서 이미지를 수집하였으나 수집한 데이터의 화질, 구도, 채광 등의 차이가 심해 모델 학습에 적합하지 않다고 판단하여 실제 고지서를 통해 Dataest을 구성

### Text Recognition
- 실제 Webcam에서 가져온 저화질 이미지가 Tesseract의 인식률에 영향을 주어
Input Process를 실시간 입력이 아닌 이미지 및 동영상 업드로 변경하여 화질 문제로 인한 인식률 저하 문제를 해결

### Voice
  ##### Tensorflow 버전 오류
  - docker container를 2.6.0 으로 만든 다음 터미널 안에서 intall 하면 강제적으로 가동하지만, dockerfile 내에서 구동하면 오류 발생. 2.7.0에서 구동이 되지 않는 라이브러리가 있음을 확인 

  ##### 권한 변경 및 docker container 설정 변경
  - NumPy와 다른 라이브러리 호환성 이슈 발생으로 dockerfile에 pip install numpy==1.19.5 추가하고 Nvidia GPG Public Key를 교체하여 Dockerfile을 구동할 수있게 수정

----------------------


<br>
</br>


## 🙏 개선점 (추가 작업)
<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/229005410-d682be5e-d36d-49f0-9b42-652b0ee8465b.png" width="700"></p>

- 클라우드 배포 
- 스마트폰을 통해 웹에 접속해 서비스를 이용 가능하게 함 (편의성,접근성)
- voice : 정형화된 데이터(출력물 중 고정된 문자열)를 가지고 음성을 미리 리스트로 저장하고 필요한 부분(금액과 같은 부분)만 생성하면 서비스속도가 개선되어질것이라고 보임
- 프론트엔드 개선 

------
<p align="center"><img src ="https://user-images.githubusercontent.com/119566469/229005616-6a3345ac-1719-4817-b4a6-afcce738b3db.png" width="900"></p>


