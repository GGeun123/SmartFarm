import leelee
import pymssql
# DB 서버 주소
server = leelee.get_server()
# 데이터 베이스 이름
database = leelee.get_database()
# 접속 유저명
username = leelee.get_username()
# 접속 유저 패스워드
password = leelee.get_password()
# MSSQL 접속
cnxn = pymssql.connect(server , username, password, database,port=1455)
cursor = cnxn.cursor()
# SQL문 실행
cursor.execute('SELECT * FROM sensor;')
# 데이타를 하나씩 Fetch하여 출력
row = cursor.fetchone()
