FROM python:3.8.6-alpine3.12

ENV PYTHONUNBUFFERED=0

RUN pip install apscheduler

RUN mkdir -p /root/app
ADD app /root/app

# 로그파일 위치 생성
RUN mkdir -p /var/log/app

ENTRYPOINT ["python", "/root/app/dummy_file_logs.py"]