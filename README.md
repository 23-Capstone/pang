# Pang! Project
<img width="827" alt="image" src="https://github.com/kwakeunji/pang/assets/67047653/7c1a48ba-1e46-4b25-a635-7439353814c0">
> 자동으로 카테고리별로 정리해주는 마인드맵 형식의 메모 웹애플리케이션 서비스입니다.

- 노트를 재활용하기 어렵거나, 메모 찾는 것에 어려움을 겪거나, 정리하는데 오랜 시간을 겪었던 사용자들을 위해 메모를 작성하면 자동으로 카테고리별로 분류되고, 직관적인 UI로 표시됩니다.

- **맡은 역할: 프로젝트 기획, 데이터 수집 및 라벨링, 템플릿 기반 클라이언트, django 서버**
    - 1,239개의 메모 데이터를 수집하고 3,952개의 단어로 정리한 후, 12개의 카테고리로 데이터를 분류하는 데이터 라벨링 수행
    - 풀스택 프레임워크인 Django를 이용하여 백엔드와 프론트엔드 구현
    - 상위 카테고리, 하위 카테고리, 메모 내용이 구성될 수 있도록 총 3개의 테이블 설계
    - NLP 모델을 연결하여, 반환값을 가져올 수 있도록 함수로 구현
    - Django 템플릿을 사용하여 데이터를 동적으로 출력할 수 있도록 프론트엔드 구성. 마인드맵 방사형 형식으로 메모가 보여질 수 있도록 구현
    
- **프로젝트를 진행하며 경험한 부분**
    - 마인드맵을 효과적으로 구성하기 위해 데이터베이스 구조를 설정하고, 데이터를 라벨링하면서 카테고리를 최적화했습니다.
    - 단순히 자바스크립트를 조작하는 것은 익숙하지 않았기에 마인드맵 형태로 뻗어나가는 일은 상당한 도전이었습니다. 하지만 이러한 도전과제를 해결하기 위해 중심좌표와 지름을 구해 마인드맵 형태로 표현하고, 줌인 줌 아웃 기능을 추가하여 프로젝트를 성공적으로 마무리했습니다.

## 프로토타입
> **Video**

https://github.com/Mingguriguri/capstone-Pang/assets/101111603/a601dbda-a27c-4ec6-b187-a9b514d36c1d

> **전체 모습**
![PANG_2-2](https://github.com/Mingguriguri/capstone-Pang/assets/101111603/e89c9635-31cb-4e69-862e-3232410e543b)

> **각 카테고리별로 확대한 모습**
![PANG_3-2](https://github.com/Mingguriguri/capstone-Pang/assets/101111603/99b917db-767c-4543-9dfb-659e77c36994)
![PANG_3](https://github.com/Mingguriguri/capstone-Pang/assets/101111603/c0f25ca8-9f52-43fc-9f3c-e0e97cecb696)
![PANG3-3](https://github.com/Mingguriguri/capstone-Pang/assets/101111603/e524564d-63f1-4233-99de-d8268930bc6a)


## 실행방법
> **사전 준비**
Python version: 3.x

## 프로젝트 설정

### 1단계: 저장소 클론

먼저, git을 사용하여 저장소를 로컬 컴퓨터에 클론합니다. 

```sh
git clone https://github.com/Mingguriguri/capstone-Pang.git
cd capstone-Pang
```
또는 저장소를 fork 한 후, 개인 저장소에서 클론합니다. 

### 2단계: 가상 환경 생성 (선택 사항)
종속성을 관리하고 다른 프로젝트와의 충돌을 피하기 위해 가상 환경을 생성하는 것을 권장합니다.
- Windows:
``` sh
python -m venv venv
venv\Scripts\activate
```

- macOS/Linux:
```sh
python -m venv venv
source venv/bin/activate
```

### 3단계: 종속성 설치
가상 환경을 활성화한 후, requirements.txt 파일에 나열된 종속성을 설치합니다.
```sh
pip install -r requirements.txt
```

### 4단계: 프로젝트 실행
프로젝트가 잘 실행되는지 확인해보세요!
```sh
python manage.py runserver
```

잘 실행된다면 프로젝트에 기여해주시면 됩니다 :D

### 가상환경 비활성화
```sh
deactivate
```
## 


## Service Architecture
<img width="1105" alt="스크린샷 2024-07-01 오후 8 52 12" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/3cd2ee49-9ca2-4ef5-a055-f5c1c4539801">

> **사용기술:**

- Frontend: Html, CSS, Javascript
- Backend: Django
- Data Storage: SQLite
- AI: FastText, KoNLPy

---
## AI
### Model
- FastText Model: Text classification
- Tokenizer: konlpy

### Dataset
-  데이터 총 개수: 1,239개
- → 총 단어 개수: 3,952개
- → label 개수: 24개

- 데이터 수집 방법: 팀원들이 직접 지인들로부터 수집
- 데이터 라벨링 방식: “`__label__    __label__ `형태소로 분류된 텍스트”

```
__label__1.할일    __label__주문    __label__음식    슈크림 빵 구매 하 기
__label__2.아이디어    __label__의료    약 알러지 있 는 사람 기록 , 이쪽저쪽 병원 다 지니 지 않 고 병력 사항 을 모두 조회 가능 하 도록
__label__1.할일    __label__학교    __label__프로그래밍    padding 어떻 ㄹ 때 하 는지 얼만큼 하 는지 꼭 물어보 기
__label__4.기타    __label__가고싶은곳    __label__대구    오랜지 막창
__label__1.할일    __label__학교    취업 상담 신청 하 지
```

- 데이터 카테고리
  ```python
  level_dict = {"💡아이디어":{"💻프로그래밍":0,"📖소재":1,"🧶잡생각":2},
              "☑️할일":{"📔학교":0,"🏠집":1,"🔥대외활동":2,"👞회사&알바":3},
              "🤓정보":{"🍽️맛집":0,"🍯꿀팁":1,"🚩핫플레이스":2,"🎫문화생활":3},
              "📌기억할것":{"❗피드백":0,"🎯추천리스트":1,"😎임무":2,"📢중요":3},
              "🔮위시리스트":{"🎥미디어":0,"🍔먹킷리스트":1,"🛒쇼핑리스트":2,"📝버킷리스트":3}}

  ```

---
## Backend
- python version: 3.9
- framework: Django 4

### MTV Pattern
<img width="1235" alt="스크린샷 2024-07-01 오후 8 56 14" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/8a9a0b89-8bca-49e8-9b7b-9b840d6b17d7">

### Database, Model
<img width="816" alt="스크린샷 2024-07-01 오후 9 56 36" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/089d55c6-db65-4b22-a6df-28960d6b51ff">

admin page
<img width="751" alt="스크린샷 2024-07-01 오후 9 57 04" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/3df990c3-2702-42c0-ae58-c5f712b00169">

### URL pattern
<img width="772" alt="스크린샷 2024-07-01 오후 9 57 17" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/1a4aa39e-5a38-4bec-888a-4e7454406c12">

### View
<img width="761" alt="스크린샷 2024-07-01 오후 9 57 30" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/b894bfcc-d83f-4f61-87ed-816c857eb28e">
<img width="777" alt="스크린샷 2024-07-01 오후 9 58 01" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/0533eeec-70c8-40f0-b957-42d5ce7b0f85">



## Frontend (Template)
<img width="781" alt="스크린샷 2024-07-01 오후 9 58 27" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/a2eccd30-3594-405b-b05d-84641b31c3ab">

<img width="782" alt="스크린샷 2024-07-01 오후 9 58 36" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/7ad9a2a4-00d8-4adf-b28f-ec72db75d1c3">

<img width="786" alt="스크린샷 2024-07-01 오후 9 58 45" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/7693023c-cc52-4dc6-8596-b7d202c89b1d">

<img width="781" alt="스크린샷 2024-07-01 오후 9 58 53" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/98523994-cef4-490b-8a2d-f8e3f34e3d90">

<img width="770" alt="스크린샷 2024-07-01 오후 9 59 04" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/7b3cc1f7-ea9f-44a1-8238-6cda362cea0b">

<img width="775" alt="스크린샷 2024-07-01 오후 9 59 14" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/c39adeae-56fb-432f-a8c0-c320ab78714b">

<img width="786" alt="스크린샷 2024-07-01 오후 9 59 24" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/09f2c23b-17f3-468c-93b4-42e76d52916b">

<img width="804" alt="스크린샷 2024-07-01 오후 9 59 34" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/dcdea2a1-722b-40eb-b7e9-8e6a5982ed0e">

<img width="779" alt="스크린샷 2024-07-01 오후 9 59 46" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/58ac98ca-38c7-4ec4-94bb-bd4cf14cd426">

<img width="781" alt="스크린샷 2024-07-01 오후 9 59 55" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/be85e85c-39a0-4ebd-afcf-9561f741cdc6">

<img width="782" alt="스크린샷 2024-07-01 오후 10 00 04" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/cb1882e2-9d68-4e5e-8e27-b59c2c1d99d1">

<img width="778" alt="스크린샷 2024-07-01 오후 10 00 11" src="https://github.com/Mingguriguri/capstone-Pang/assets/101111603/c798a32a-2474-4df8-adc8-98b92c85b58c">

# Docs
발표자료: [바로가기](https://drive.google.com/file/d/1OztFz9sChpzaPJr6qajO_m8DBiyEtzSf/view?usp=drive_link)

