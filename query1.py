# Тест на наличие таблицы `good`
# Проверка наличия таблицы в базе данных, если таблица отсутствует выдать ошибку

import pymysql
import pymysql.cursors
from main_config_base import host, user, password, db_name

try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print('success')
    print('#' * 30)
    try:
         with connection.cursor() as cursor:
              cursor.execute('SHOW TABLES LIKE "good"')
              check_tables = cursor.fetchone()
              for table in check_tables:
                   print(table)
 
    finally:
        connection.close()
         
except Exception as ex:
    print('Connection rufus')
    print(ex)
            
