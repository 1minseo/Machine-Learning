import pymysql

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='1111',
        db='homestead', # 접속할 DB의 이름
        charset='utf8' # DB 연결에 사용할 문자 인코딩
    )

    # 테이블 생성에 사용할 SQL 쿼리를 문자열로 정의
    sql = '''
    CREATE TABLE tb_student (
        id int primary key auto_increment not null,
        name varchar(32),
        age int,
        address varchar(32)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''

    # 테이블 생성
    with db.cursor() as cursor:
        # DB 커서를 사용하여 SQL 쿼리를 실행. with문을 사용하여 커서를 생성하고, 해당 블록이 끝나면 자동으로 커서를 닫음
        cursor.execute(sql)
        # 커서를 사용하여 SQL 쿼리를 실행. DB에 대한 수정 작업을 수행

except Exception as e: # try 블록에서 발생한 예외를 처리
    print(e)

finally:
    if db is not None:
        db.close()