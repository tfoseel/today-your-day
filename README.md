# 🎉 오늘은 너의 생일 (Today Your Day)

KAIST 전산학 특강 "돌봄 및 사회적 약자를 위한 컴퓨팅 플랫폼" 수업에서 기획한 프로젝트입니다.

자립청년들의 생일을 함께 축하하고 응원하는 감성 플랫폼의 웹사이트 파트입니다.
자립청년 중 외로움, 고립감 등 심리적 어려움을 겪고 있는 사람들에게 "이름이 같은 사람들"이 롤링페이퍼를 작성하면, Suno AI를 이용해 롤링페이퍼들을 모아 노래로 만들고, 실물 케이크, 롤링페이퍼, 그리고 플랫폼으로 연결되는 실물 초대장을 배송하여 서프라이즈 생일 파티를 해 주는 플랫폼입니다.
이 레포지토리는 그 중 롤링페이퍼를 모으는 기능을 하며, 전체 플랫폼 기획 및 소설 형태의 몰입형 시나리오, 인터뷰 내용 등은 [여기(2025.04.03. 버전)](https://drive.google.com/file/d/196h6ROaQygnmibBEk-gqHnuc-GbmkQIz/view?usp=drive_link)에서 보실 수 있습니다. 

---

## 📌 주요 링크

| 경로 | 설명 |
|------|------|
| [`/`](https://web-production-2f16.up.railway.app/users/)| 루트 주소 접근 시 자동으로 `/users/login/`으로 리다이렉트 |
| [`/users/login/`](https://web-production-2f16.up.railway.app/users/login/ ) | **로그인 페이지** – 전화번호와 비밀번호로 로그인 |
| [`/users/signup/`](https://web-production-2f16.up.railway.app/users/) | **회원가입 페이지** – 이름, 닉네임, 전화번호, 생일 입력 |
| `/home/` | 로그인 후 보여지는 **메인 화면** – 같은 이름을 가진 수신자들의 캐릭터 등장 |
| [`/recipients/<uuid>/invite`](https://web-production-2f16.up.railway.app/recipients/5c6e84a7-b1f8-4dea-bc5b-a1f8b7cd357a/invite/) | **초대장 페이지** – 특정 수신자의 생일을 축하하도록 초대 |
| [`/recipients/<uuid>/write/`](https://web-production-2f16.up.railway.app/recipients/5c6e84a7-b1f8-4dea-bc5b-a1f8b7cd357a/write/) | **롤링페이퍼 작성 페이지** – 메시지와 이미지 첨부 가능 |
| [`/recipients/<uuid>/papers/`](https://web-production-2f16.up.railway.app/recipients/5c6e84a7-b1f8-4dea-bc5b-a1f8b7cd357a/papers/) | **롤링페이퍼 보기 페이지** – 축하 메시지와 음악 감상 가능 |

링크를 클릭하면, 배포된 데모 페이지를 보실 수 있습니다. 가입 시 이름을 '승우'로 하면, 생일이 같은 승우들의 아바타를 `/home/`에서 보실 수 있습니다.

---

## 🎨 주요 기능

- 회원 가입 및 로그인
- 같은 이름을 가진 수신자 추천
- 롤링페이퍼 작성 (이미지 첨부 가능)
- 롤링페이퍼 목록 보기 (토글 형식)
- 수신자별 음악 업로드 및 감상 기능
- 초대장 페이지에서 회원 가입 또는 비회원 롤링페이퍼 작성 가능
- 캐릭터 기반 인터랙티브 UI
- 생일 축하 음악 재생 기능

---

## 🧑‍💻 로컬 개발 환경 세팅

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. `.env` 설정

```
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
ADMIN_PHONE=01012345678
ADMIN_PASS=adminpassword
DATABASE_URL=postgres://username:password@localhost:5432/dbname
```

### 3. DB 초기화 및 관리자 계정 생성

```
python manage.py migrate
python manage.py create_admin
```

### 4. 로컬 서버 실행

```
python manage.py runserver
```

