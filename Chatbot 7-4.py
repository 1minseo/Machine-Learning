import pymysql

db = None # DB 연결 객체 초기화
try: # 예외 처리 시작
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect( # MySQL DB에 연결
        host='127.0.0.1',
        user='root',
        passwd='1111',
        db='homestead',
        charset='utf8'
    )

    # 데이터 수정 sql 정의
    id = 1  # 데이터 id (PK)
    sql = '''
        UPDATE tb_student set name="케이", age=36 where id=%d
        ''' % id

    # 데이터 수정
    with db.cursor() as cursor: # with문을 사용하여 커서 생성
        cursor.execute(sql)
    db.commit() # 변경 사항을 커밋하여 DB에 영구적으로 저장


except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()