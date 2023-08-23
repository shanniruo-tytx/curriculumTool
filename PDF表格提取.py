import sqlite3
import tabula  # 用于从PDF提取表格数据

# 提取表格数据并保存为DataFrame
pdf_path = "path/to/your/pdf_file.pdf"
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

# 假设你从表格中提取了以下列：name, age, email
# 清洗数据并转换为列表
data = []
for table in tables:
    for row in table.values:
        if len(row) == 3:  # 假设表格有3列
            name, age, email = row
            data.append((name.strip(), int(age), email.strip()))

# 连接到SQLite数据库
db_conn = sqlite3.connect("your_database.db")
db_cursor = db_conn.cursor()

# 创建表格
db_cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER, email TEXT)")

# 插入数据
for record in data:
    db_cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", record)

# 提交更改并关闭连接
db_conn.commit()
db_conn.close()

print("Data has been inserted into the database.")
