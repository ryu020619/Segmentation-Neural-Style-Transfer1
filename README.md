# Segmentation-Neural-Style-Transfer 💻 + 🎨 = ?
- - -

## 프로젝트 개요
- - -
+ ### *NST 알고리즘이란?*
알고리즘은 CNN넷(일반적으로 VGG-16/19)을 사용하여 한 입력 이미지(스타일 이미지)에서 -> 다른 입력 이미지(콘텐츠 이미지)로 스타일을 전송한다.
이 프로젝트에서는 GAN을 활용한 Style Transfer을 통해 연속된 이미지의 스타일 변화를 수행하고, 특정 영역을 지정하여 스타일 변화를 한다. 

+ ### *style GAN이란?*
![style gan](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/blob/main/image.png)

1. 스타일 이미지 + 사계절, 콘텐트 이미지 → 시간에 따라 변하는 gif 생성
2. 특정 영역(지정 영역)만 스타일 변환

   
다음과 같이 Style transfer 응용 분야 확장 총 두 가지를 수행함.


- - -
### 필요한 라이브러리 
- - - 
> *python*,  *numpy*, *os*, *argparse*, *matplotlib*, *cv2* 기타 등등...

### channels:
  - defaults
  - pytorch
    
### dependencies:
  - python=3.7.6
  - pip=20.0.2
  - matplotlib=3.1.3
  - pytorch==1.4.0
  - torchvision=0.5.0

### pip:
  - numpy==1.18.1
  - opencv-python==4.2.0.32
- - -
### 데이터 세트
- - -
직접 촬영한 8초짜리 학교 영상을 -> 초당 프레임이 **30fps**인 **240**장의 연속된 사진들로 변환함.

### ![학교 영상](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/blob/main/ky_school.mov) << 눌러서 원본 동영상 확인


![연속 된 사진](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/blob/main/ex_content.png)




=> 위 사진과 같이 content_0to59 파일 안에 저장된 60장의 사진들.

=> content_0to59, content_60to119, content_120to179, content_180to239 총 4개의 파일에 60장씩 구분해둠.

- - -
### 모델 설명 - 사용한 모델의 종류 및 선택 이유
- - -
생성 모델인 GAN의 종류는 다음과 같다.
1. Conditional gan(2014)
2. DC gan (2015)
3. cycle gan (2017)
4. star gan (2018)
5. style gan (2019)


(보통 VGG-16나 VGG-19 사용)

+ 이 중에서 style gan이 가장 최신 버전이다.
+ 따라서 건물이나 사람의 얼굴 잘 style transfer시키기 때문에 뛰어난 성능을 가졌다고 판단했다. 

-> 위와 같은 이유로
style gan으로 모델을 짠 git hub 파일들을 찾아보다가,

첨부한 자료가 내가 하고자 하는 방향과 가장 비슷하다고 생각하여

메인으로 참고하여 진행하게 되었다.  ![git hub 참고](https://github.com/gordicaleksa/pytorch-neural-style-transfer)
- - -
### 실험 결과 中 1
#### 1. 스타일 이미지 + 사계절, 콘텐트 이미지 → 시간에 따라 변하는 gif 생성
- - -
       
+ 60장씩 총 네 번의 style transfer 진행
+ style은 사계절 이미지 (봄, 여름, 가을, 겨울) 사용
                                                          
결과 => 2초가 지날 때마다 계절이 바뀌는 8초짜리 학교 영상 및 gif 생성

![spring](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/blob/main/spring.png)
![spring](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/blob/main/summer.png)
![spring](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/blob/main/autumn.png)
![spring](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/blob/main/winter.png)

+ spring 60장 + summer 60장 + autumn 60장 + winter 60장 합친 gif

![gif](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/assets/144203528/9db85a86-51c4-4c5a-9df4-6efbb4ee6174
)

- - -
### 실험 결과 中 2
#### 2. 특정 영역(지정 영역)만 스타일 변환
- - -



- - -
### 추후 개선 사항
- - -
