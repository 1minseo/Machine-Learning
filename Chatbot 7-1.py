import pymysql

# DB_HOST=127.0.0.1
# DB_PORT=3306
# DB_DATABASE=homestead
# DB_USERNAME=homestead
# DB_PASSWORD=secret

db = None # DB 연결 객체 초기화
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect( # pymysql 모듈의 connect() 함수를 사용하여 MySQL DB에 연결
        host='127.0.0.1',
        user='root', # MySQL DB에 접속할 사용자 이름
        passwd='1111',
        db='homestead', # DB 이름
        charset='utf8'
    )
    print("DB 연결 성공")


except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print("DB 연결 닫기 성공")