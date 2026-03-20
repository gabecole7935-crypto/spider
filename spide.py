import requests
from bs4 import BeautifulSoup
import random
import time
import csv
def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.status_code == 200:
            resp.encoding = 'utf-8'
            return BeautifulSoup(resp.text, 'lxml')
        else:
            print(f'请求失败，状态码：{resp.status_code}')
            return None
    except Exception as e:
        print(f'发生异常：{e}')
        return None
def parse_page(soup):
    movies=[]
    items=soup.find_all('div',class_='item')
    for item in items:
        title=item.find('span',class_='title').text
        rating=item.find('span',class_='rating_num').text
        quote_tag=item.find('span',class_='inq')
        quote=quote_tag.text if quote_tag else''
        movies.append([title,rating,quote])
    return movies
def save_to_csv(movies,filename='douban.csv'):
    with open(filename,'a',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerows(movies)
def main():
    with open('douban.csv','w',encoding='utf-8')as f:
        write=csv.writer(f)
        write.writerow(['标题','评分','引用语'])
    for page in range(5):
        start=page*25
        url=f'https://movie.douban.com/top250?start={start}'
        print(f"正在抓取第{page+1}页")
        soup=fetch_page(url)
        if soup is None:
            print('无法获得页面')
            break
        movies=parse_page(soup)
        print(f'解析到{len(movies)}部电影')
        save_to_csv(movies)
        time.sleep(random.uniform(2,4))
    print('抓取完成！数据保存到 douban.csv')
if __name__=='__main__':
    main()




