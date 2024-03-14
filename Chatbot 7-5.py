import pymysql

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect( # MySQL DB에 연결
        host='127.0.0.1',
        user='root',
        passwd='1111',
        db='homestead',
        charset='utf8'
    )

    # 데이터 삭제 sql 정의
    id = 1  # 데이터 id (PK)
    sql = '''
        DELETE from tb_student where id=%d
        ''' % id # 'td_student'테이블에서 ID가 주어진 값과 일치하는 레코드 삭제

    # 데이터 삭제
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit() # DB에 대한 변경 사항을 커밋하여 영구적으로 저장


except Exception as e:
    print(e)

finally:
    if db is not None: # DB 연결 객체 db가 유효한지 확인
        db.close()