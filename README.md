# 🎂 오늘은 너의 날 (Today is Your Day)

> 보호종료아동과 이름이 같은 사람들로부터 롤링페이퍼와 생일 축하를 받는 따뜻한 커뮤니티 플랫폼입니다.  
> 이 프로젝트는 Django + DRF + PostgreSQL + Docker 기반으로 개발됩니다.

---

## 📁 프로젝트 구조

```bash
today-your-day/
├── app/              # Django 프로젝트 루트
│   ├── users/        # 사용자 관련 앱 (회원가입 등)
│   ├── today/        # 프로젝트 설정
├── docker/           # Docker 관련 설정
├── pyproject.toml    # Poetry 의존성 관리
├── docker-compose.yml
```

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