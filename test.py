# -*- coding: utf-8 -*-

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='cp949')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# ������ ���� ���� (�����: 'w', �̾��: 'a')
output_file = open("comments.txt", "w", encoding="UTF-8")

# 1. ����̹� ����
url = 'https://gall.dcinside.com/board/lists/?id=bitcoins_new1&exception_mode=recommend'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(2)

# 2. �Խñ� ��ũ ����
post_links = driver.find_elements(By.CSS_SELECTOR, ".gall_tit.ub-word > a")
urls = [a.get_attribute("href") for a in post_links if "view" in a.get_attribute("href")]

# 3. �� �Խñ��� ��� ����
for post_url in urls[:5]:  # �Խñ� 5����
    driver.get(post_url)
    time.sleep(2)

    output_file.write(f"\n[? Post URL] {post_url}\n")

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    comments = soup.select("div.comment_box > div.ub-content")

    if not comments:
        output_file.write("? No comments\n")
        continue

    for comment in comments:
        text = comment.get_text(strip=True)
        output_file.write(f"? {text}\n")

# 4. ����̹� ���� �� ���� �ݱ�
driver.quit()
output_file.close()

print("? Comments have been saved to 'comments.txt'.")
