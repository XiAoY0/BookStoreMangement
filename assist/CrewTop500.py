import csv
import random
import requests
from bs4 import BeautifulSoup

# 爬取豆瓣图书TOP500
def scrape_douban_top_500():
    url = 'https://book.douban.com/top250'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='pl2')
        books = []
        for item in items:
            title = item.find('a')['title']
            # 重新定位作者信息的位置
            author_info = item.find_next_sibling('p', class_='pl')
            if author_info:
                author_info = author_info.get_text().strip().split('/')
                author = author_info[0].strip()
                publisher = author_info[-2].strip()
                category = author_info[-1].strip()
                price = random.uniform(20, 100)  # 价格随机生成
                inventory = random.randint(50, 200)  # 库存数量随机生成
                books.append((title, author, publisher, price, category, inventory))
            else:
                print("未找到作者信息。")
        return books
    else:
        print("Failed to retrieve data from Douban.")
        return None

# 生成图书编号
def generate_book_id(base_id, count):
    return [base_id + i for i in range(count)]

# 写入CSV文件
def write_to_csv(file_name, books):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['图书编号', '图书名称', '图书作者', '图书出版社', '图书价格', '图书类别', '图书库存数量'])
        for i, book in enumerate(books):
            book_id = generate_book_id(2000, len(books))[i]
            writer.writerow([book_id] + list(book))

# 爬取豆瓣TOP500图书信息并写入CSV文件
books = scrape_douban_top_500()
if books:
    write_to_csv('douban_top_500.csv', books)
    print("豆瓣TOP500图书信息已写入CSV文件。")
else:
    print("未能成功获取豆瓣TOP500图书信息。")
