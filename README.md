# Fluentd Examples

## Run
본 예제는 `docker-compose.yml`을 포함하고 있지 않다. docker-compose 파일은 목적에 따라 분리하여 저장하였고 사용자가 적접 아래의 명령어를 이용하여 합쳐서 사용하길 바란다.
* docker-compose.build.yml
* docker-compose.essential.yml
* docker-compose.log-collector.yml

```bash
$ docker-compose -f docker-compose.build.yml -f docker-compose.log-collector.yml -f docker-compose.essential.yml config > docker-compose.yml 
$ docker-compose up -d
```

## 로그 생성기 이미지
### test-dummy-file-logs:latest
파일로 로그 데이터를 생성. 사용자 지정 포맷 사용
 
### test-dummy-json-stream-logs:latest
JSON 포맷의 로그를 `stdout`으로 스트리밍. Docker Log Driver가 Fluentd로 전송

## MongoDB 접속 및 데이터 확인
```bash
# docker exec -it mongoddb mongo
> use dummy-logs
> db.getCollection('test').find({"name": "dummy-json-stream-logs"})
{ "_id" : ObjectId("61319ef6c7339c001211d5fc"), "asctime" : "2021-09-03 04:03:48,335", "levelname" : "DEBUG", "name" : "dummy-json-stream-logs", "thread" : NumberLong("139705041726240"), "message" : "[task-dummy-json-stream-logs-0]", "time" : ISODate("2021-09-03T04:05:00.263Z") }
{ "_id" : ObjectId("61319ef6c7339c001211d5fd"), "asctime" : "2021-09-03 04:03:48,336", "levelname" : "DEBUG", "name" : "dummy-json-stream-logs", "thread" : NumberLong("139705041726240"), "message" : "[task-dummy-json-stream-logs-1]", "time" : ISODate("2021-09-03T04:05:00.263Z") }
```

