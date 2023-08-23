import pdfplumber
import mysql.connector
import uuid
import numpy as np
# 连接到MySQL数据库
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="test",
    use_unicode=True,  # 添加use_unicode参数
    charset="utf8mb4"     # 添加charset参数
)
cursor = db_connection.cursor()

# 打开PDF文件
target_pages = [9,10,11]  # 例如，提取第1、2、3页的数据
with pdfplumber.open("C:/Users/Administrator/Desktop/data.pdf") as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        if page_number in target_pages:
            table = page.extract_table()
            arr = np.array(table)
            #print(table)
            #print(arr.shape)
            #print(len(table))
            # 处理表格数据并插入到数据库
            middle_columns = arr[:, 1:4]  # 选择第2到第4列（索引1到3）  
            print(middle_columns)             
            # 处理表格数据并插入到数据库
            for row in middle_columns[1:]:
                print(row)
                col1, col2, col3 = row
                #todo 处理节次string拆分
                id=uuid.uuid1()
                #query = "INSERT INTO curriculum (id,curriculum_classroom, curriculum_name, weekdate) VALUES (%s,%s, %s, %s)"
                #values = (str(id),col1, col2, col3)
                #cursor.execute(query, values)

                query = f"INSERT INTO curriculum (id, curriculum_classroom, curriculum_name, weekdate) VALUES ('{id}', '{col1}', '{col2}', '{col3}')"
                print(query)
                cursor.execute(query)
                db_connection.commit()

# 关闭数据库连接
cursor.close()
db_connection.close()
