# 🎂 오늘은 너의 날 (Today is Your Day)

> 보호종료아동과 이름이 같은 사람들로부터 롤링페이퍼와 생일 축하를 받는 따뜻한 커뮤니티 플랫폼입니다.  
> 이 프로젝트는 Django + DRF + PostgreSQL + Docker 기반으로 개발됩니다.

---

## ⚙️ 개발 환경
- Python 3.11
- Django 4.x
- Django REST Framework
- PostgreSQL (Docker)
- Redis (Docker)
- Poetry (패키지 관리)
- Docker Compose (통합 실행)
- pre-commit, ruff (코드 품질 관리)

## 🚀 실행 방법
### 1. 저장소 클론
```bash
git clone https://github.com/your-username/today-your-day.git
cd today-your-day
```

### 2. Poetry 환경 구성
```bash
poetry install
poetry shell
```

### 3. Docker 컨테이너 실행
```bash
docker-compose up --build
```
⚠️ 도커 데몬이 실행 중인지 확인하세요! (Docker Desktop 켜기)

4. 마이그레이션 및 superuser 생성
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## ✅ 테스트 방법
```bash
docker-compose exec web python manage.py test users
# keepdb 옵션으로 테스트 DB 재사용:
docker-compose exec web python manage.py test users --keepdb
```

## 🧪 테스트 예시 (users)
- 회원가입 성공
- 필수 입력값 누락 시 실패

## 🧼 코드 품질 체크 (pre-commit)
```bash
pre-commit install
pre-commit run --all-files
```

## 📬 향후 개발 예정 기능
- 이름 기반 회원가입
- 생일 입력 및 연결
- 롤링페이퍼 API 작성
- 실물 초대장 및 케이크 배달 API
- AI 기반 음악 생성 연동

# 오늘은 너의 날 - API 문서 (v1)

## 🔐 인증

### 1. 회원가입  
`POST /api/users/signup/`  
사용자 계정을 생성합니다.

**Request Body:**
```json
{
  "name": "이승우",
  "nickname": "테스트승우",
  "birthday": "2000-08-06",
  "phone_number": "01012345678",
  "password": "strongpassword123!"
}
```

**Response:**
- 201 CREATED

---

### 2. 로그인 (JWT)
`POST /api/users/login/`  
JWT 토큰을 발급받습니다.

**Request Body:**
```json
{
  "phone_number": "01012345678",
  "password": "strongpassword123!"
}
```

**Response:**
```json
{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}
```

---

### 3. 내 정보 조회  
`GET /api/users/me/`  
**Header:** Authorization: Bearer {access_token}

**Response:**
```json
{
  "id": 1,
  "name": "이승우",
  "nickname": "테스트승우",
  "birthday": "2000-08-06",
  "phone_number": "01012345678"
}
```

---

### 4. 회원탈퇴  
`DELETE /api/users/me/`  
**Header:** Authorization: Bearer {access_token}  
회원 정보를 삭제합니다.

**Response:**
- 204 NO CONTENT

---

## 🎁 수신자 (Recipient)

### 5. 수신자 생성
`POST /api/recipients/`  
생일 초대장을 받을 대상자를 등록합니다.

**Request Body:**
```json
{
  "name": "홍길동",
  "birthday": "2001-05-03",
  "address": "서울시 강남구 테헤란로 123",
  "phone_number": "01012345678"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "홍길동",
  "birthday": "2001-05-03",
  "address": "서울시 강남구 테헤란로 123",
  "phone_number": "01012345678",
  "uuid": "UUID값"
}
```

---

## 💌 롤링페이퍼

### 6. 롤링페이퍼 작성  
`POST /api/recipients/rollingpapers/`  
특정 수신자에게 메시지와 이미지를 전달합니다.

**Request Body:**
multipart/form-data
- recipient: Recipient ID
- message: 텍스트 메시지 (최대 100자)
- image: 선택 이미지 파일

**Response:**
- 201 CREATED

---

### 7. 특정 수신자의 초대 페이지 조회 (웹 랜딩)
`GET /api/recipients/<uuid:uuid>/invite/`  
템플릿 기반 HTML 랜딩 페이지 제공

---

### 8. 특정 수신자 롤링페이퍼 목록 조회  
`GET /api/recipients/<uuid:uuid>/rollingpapers/`  
수신자에게 전달된 롤링페이퍼를 모두 조회합니다.

**Response:**
```json
[
  {
    "id": 1,
    "message": "생일 축하해요 :)",
    "image": "http://localhost:8000/media/rollingpaper_images/...",
    "created_at": "2025-03-30T12:00:00Z"
  },
  ...
]
```
