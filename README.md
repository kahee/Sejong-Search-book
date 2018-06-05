# 세종 도서 검색 서비스 
## 프로젝트 소개
세종대학교 학술정보원에 있는 도서를 검색하여 도서 위치와 도서 대출 여부를 알려주는 서비스입니다. 
## 사용법
1. 도서명 검색

2. 도서상세 검색 

## 프로젝트 구성 
- 사용 언어 및 프로그램
    - AWS EC2
    - Django
    - Docker
    - PostgreSQL
    - Python
    - RDS
    - S3
- 주요 내용
    - 개발 환경 분리 (local/dev/production)
    - `.secrets` 폴더로 비밀키 관리 
    - `django-json-secrets` 패키지를 활용하여 비밀키를 좀 더 편리하게 관리 (참고)[https://github.com/LeeHanYeong/django-json-secrets]

## Requirements
- beautifulsoup4<=4.6.0
- boto3<1.7
- Django<2.1
- django-extensions==2.0.7
- django-json-secrets==0.1.9
- django-storages==1.6.5
- lxml==4.2.1
- Pillow<6.0.0
- psycopg2-binary==2.7.4
- requests<2.19
- raven<6.7
- uWSGI<2.1

## AWS 환경 
- Python(3.6)
- S3 Bucket, 해당 Bucket을 사용할 수 있는 IAM User의 AWS AccessKey, SecretAccessKey
- RDS Database(보안그룹 허용 필요), 해당 database를 사용할 수 있는 RDS의  User,Password 

## Installation(Django runserver)
```angular2html
pip install -r .requirements/dev.txt
```

### 로컬 환경 (local)
```
expose DJANGO_SETTINGS_MODULE=config.settings.dev
pip install -r .requirements/dev.txt
python manage.py runserver
```
### AWS환경 (dev)
```
expose DJANGO_SETTINGS_MODULE=config.settings.dev
pip install -r .requirements/dev.txt
python manage.py runserver
```
### 배포환경 (production)
```
expose DJANGO_SETTINGS_MODULE=config.settings.dev
pip install -r .requirements/dev.txt
python manage.py runserver
```

## Installation(Docker)
### 로컬환경 (local)
`localhost:8000`에서 확인
```
docker build -t eb-docker:base -f Dockerfile.local
docker run --rm -it 8000:80 eb-docker:local
```
### AWS환경 (dev)
```
docker build -t eb-docker:dev -f Dockerfile.dev
docker run --rm -it 8000:80 eb-docker:dev
```
### AWS환경 (production)
```
docker build -t eb-docker:production -f Dockerfile.production
docker run --rm -it 8000:80 eb-docker:production
```
## Dockerhub 관련
```
docker build -t eb-docker:base -f Dockerfile.base
docker tag eb-docker:base <자신의 사용자명>/<저장소명>:base
docker push <사용자명>/<저장소명>:base
```
이후 Elasticbeanstalk을 사용한 배포 시, 해당 이미지를 사용
```Docker
# Dockerfile
FROM    <사용자명>/<저장소명>:base
```
## Secrets
`.secrets/base.json`
```json
"SECRET_KEY": "<Django settings SECRET_KEY value>"
  "RAVEN_CONFIG": {
    "dsn": "https://<sentry_Client_Keys>",
    "release": "raven.fetch_git_sha(os.path.abspath(os.pardir))"
  },
  "SUPERUSER_USERNAME":"<superuser username>",
  "SUPERUSER_PASSWORD":"<superuser user-password>",
  "SUPERUSER_EMAIL":"<superuser user-email>",
  "AWS_ACCESS_KEY_ID":"<AWS_ACCESS_KEY value> ",
  "AWS_SECRET_ACCESS_KEY":"<AWS_SECRET_ACCESS_KEY value>",
  "AWS_STORAGE_BUCKET_NAME":"<AWS_BUCKET_NAME>",
  "AWS_S3_REGION_NAME":"<region name>, default='ap-northeast-2'",
  "AWS_S3_SIGNATURE_VERSION":"<version>, default: s3v4",
  "AWS_DEFAULT_ACL":"private",
```
`.secrets/local.json`
`.secrets/dev.json & .secrets/production.json`
```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "<자신의 RDS주소. ex)instance-name.###.region.rds.amazonaws.com>",
      "NAME": "<DB name>",
      "USER": "<DB username>",
      "PASSWORD": "<DB user password>",
      "PORT": <Port number, default:5432>
    }
  }
}
```
