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
            #  cursor.execute('SHOW TABLES')
            #  tables = cursor.fetchall()
            #  print('Tables in database')
            #  print(type(tables))
            #  for table in tables:
            #      print(type(table))
            #      print(table['table_in ' + db_name])
            #  print('#' * 30)



            # create_table_kate = 'CREATE TABLE IF NOT EXISTS `students`(id INT AUTO_INCREMENT, name VARCHAR(32), email VARCHAR(32), age INT, PRIMARY KEY (id))';
            # cursor.execute(create_table_kate); # Создали таблицу
            # print('Table STUDENTS created')

            # my_query =  """
            # INSERT INTO `students` (name, email, age)
            # VALUES ('Natasha', 'email', 40), ('Katusha', 'email', 40), ('Lena', 'email', 40);
            #                """
            # cursor.execute(my_query)
            # connection.commit()
            # print('data inserted')

            # my_query_2 =  """
            # SELECT * FROM `students` LIMIT 2
            # ;
            #                """
            # cursor.execute(my_query_2)
            # my_students = cursor.fetchall()
            # connection.commit()
            # print('data inserted', my_students)
            # for i in my_students:
            #     print(i)

            

            # my_query =  """
            # INSERT INTO `students` (name, email, age)
            # VALUES ('Natasha', 'email', 40), ('Katusha', 'email', 40), ('Lena', 'email', 40);
            #                """
            # cursor.execute(my_query)
            # connection.commit()
            # print('data inserted')

            my_query_3 =  """
            CREATE VIEW ice_tea AS
            SELECT id, category_id, name, count, price 
            FROM `good` 
            WHERE name LIKE '%Айс Ти%'"""
            cursor.execute(my_query_3)
            #connection.commit()
            print('View_ created')
            

            
    finally:
        connection.close()
         
except Exception as ex:
    print('Connection rufus')
    print(ex)


# try:
#     connection = pymysql.connect(
#         host = host,
#         port = 3306,
#         user = user,
#         password = password,
#         database = db_name,
#         cursorclass = pymysql.cursors.DictCursor
#     )
#     print('success')
#     print('#' * 30)
#     try:
#          with connection.cursor() as cursor:
#              cursor.execute('SHOW TABLES')
#              tables = cursor.fetchall()
#              print('Tables in database')
#              print(type(tables))
#              for table in tables:
#                  print(type(table))
#                  print(table['table_in ' + db_name])
#              print('#' * 30)

#             # create_table_q = 'CREATE TABLE `users`(id INT AUTO_INCREMENT, name VARCHAR(32), password VARCHAR(32), email VARCHAR(32), PRIMARY KEY (id))'
#             # cursor.execute(create_table_q)
#     finally:
#         connection.close()
         
# except Exception as ex:
#     print('Connection rufus')
#     print(ex)
