import pymysql

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    # MySQL DB에 연결. 연결에 필요한 호스트 주소, 사용자 이름, 암호, DB 이름 및 문자 인코딩 지정
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='1111',
        db='homestead',
        charset='utf8'
    )

    # 데이터 삽입 sql 정의
    sql = '''
    INSERT tb_student(name, age, address) values('Kei', 35, 'Korea')
    '''

    # 데이터 삽입
    with db.cursor() as cursor: # DB 커서를 사용하여 SQL 쿼리를 실행
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close() # DB와의 연결을 종료