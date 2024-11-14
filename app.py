from psycopg2 import connect
conn = connect(host='app_db',port=5432,user='root',password='123456',dbname='test_db')
conn.autocommit = True

with conn: 
    with conn.cursor() as curs:
     curs.execute('''CREATE TABLE IF NOT EXISTS pg_dem(id INT, name varchar(60), Age INT, Departament varchar(60));
                    INSERT INTO pg_dem VALUES (1, 'MAGA', 30, 'HR'), 
                  (2, 'TYGA', 44, 'Engineering'), 
                  (3, 'ROBERT', 32, 'Sales');
                  SELECT * FROM pg_dem; 
                  ''')
     print(curs.fetchall())
conn.close()
