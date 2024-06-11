# Segmentation-Neural-Style-Transfer 
#### (뉴런 스타일 변화 및 특정 영역 지정 스타일 변환)

- - -

## 프로젝트 개요
### 스타일 이미지 + 사계절, 콘텐트 이미지 → 시간에 따라 변하는 gif 생성
- - -

## 필요한 라이브러리 
- - -
## 데이터 세트

직접 촬영한 8초 짜리 학교 영상을 -> 초당 프레임이 **30fps**인 **240**장의 연속된 사진들로 변환함.

![학교 영상](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/blob/main/ky_school.mov)


=> 위 사진과 같이 content_0to59, content_60to119, content_120to179, content_180to239 총 4개의 파일에 구분해둠.

- - -
## 모델 설명


content로 사용할 연속적인 학교 이미지 중 가장 첫 번째 사진


![학교 첫 번째 이미지](https://github.com/ryu020619/Segmentation-Neural-Style-Transfer1/blob/main/frame_0000.jpg)
- - -
## 실험 결과
- - -
### 추후 개선 사항

