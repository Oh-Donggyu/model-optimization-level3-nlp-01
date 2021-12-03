# BoostCamp AI - Run & Learn

<div align="center">
  <a href="https://github.com/boostcampaitech2/mrc-level2-nlp-01">
    <img src="https://i.imgur.com/b48hDWD.png" alt="Logo" width="500">
  </a>

  <h3 align="center">Model Optimization</h3>

  <p align="center">
    Run & Learn Team - BoostCamp AI Second
    <br />
  </p>
</div>

## 프로젝트 주제

- 모바일 플랫폼, 온-디바이스 환경 등 실제 서비스에서의 제한된 환경을 고려하여 더 작고 빠르게 동작할 수 있는 경량화 된 모델 만들기
- 분리수거 로봇에 가장 기초 기술인 쓰레기 이미지 분류 모델 생성 (class: 캔, 종이, 종이팩, 플라스틱, 스티로폼)

## 활용 장비 및 재료(개발 환경 등)

- PostgreSQL
- Pytorch & Optuna
- WandB

## 데이터 구성

- COCO format의 재활용 쓰레기 데이터인 TACO 데이터 사용
- 단순한 Classification 문제로 설정하기 위해 TACO 데이터셋의 Bounding box를 crop 한 데이터를 사용
    - 이미지의 width와 height가 모두 제각각으로 다름
- train data는 6개의 카테고리로 분류되어 있고 총 20,851장의 .jpg format 이미지
    - class imbalance 문제

💡 경량화 문제에 초점을 맞추기 위해, 외부데이터셋 사용은 금지

## 평가 기준

어느 정도 이상의 성능을 유지하며 크기가 작은 모델과 빠른 추론 속도를 갖는 모델인지를 판단할 수 있는 최종 score를 통해 판단

- 최종 score는 모델의 f1-score와 모델의 Submit time를 통해 계산 (낮을수록 좋음)

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d411e9e8-c03d-45a4-b926-ff0f7f9c3d16/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211203T061100Z&X-Amz-Expires=86400&X-Amz-Signature=83e2a49e576d4bc743c64b183c0a4f892f783115145795124120ad464750a4a7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)


## 프로젝트 구조

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e33a5252-b462-4b9a-b124-afc7e9073f8d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20211203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211203T061113Z&X-Amz-Expires=86400&X-Amz-Signature=7ee85c84e27e1da8febb22a3306be8b3230e09f6c28f317c516d3641747f6dca&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 실험하고자 하는 모델 구조와 하이퍼파라미터 정의
- 정의한 모델 구조와 하이퍼파라미터 학습
- 정확도, 속도, 모델 크기 등 목적을 기준으로 실험한 configuration 평가
- TPE, Gaussian Processes 등 알고리즘을 통해 다음 탐색하면 좋을 구간 파악
- 다음 구간 탐색
