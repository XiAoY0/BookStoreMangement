import requests
from bs4 import BeautifulSoup
import sqlite3

# 创建数据库连接
conn = sqlite3.connect('douban_books.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT
                )''')

# 获取豆瓣图书前500的页面内容
url = 'https://book.douban.com/top250'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 提取图书信息并存储到数据库
books = soup.find_all('div', class_='pl2')
for index, book in enumerate(books):
    if index >= 500:
        break
    title = book.find('a')['title']
    author = book.find('p', class_='pl').text.strip().split('/')[0]
    cursor.execute('''INSERT INTO books (title, author) VALUES (?, ?)''', (title, author))
    conn.commit()

# 关闭数据库连接
conn.close()
