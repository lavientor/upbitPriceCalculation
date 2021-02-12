# 쪼꼬 열등반 등록 기념
# 1. 환율 가져오기
# 2. 역프 가져오기
# 3. 가격범위 a - b 입력받기
# 4. 소지금액 입력받기
# 5. 사용비율 입력받기
# 6. gui로 만들기
#    입력을 gui로 받음
#    출력을 엑셀 테이블 형태로 화면출력 / 엑셀저장
import time
import warnings
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


#
# # warning 무시
# warnings.filterwarnings(action='ignore')
#
# currency_url = 'https://www.investing.com/currencies/usd-krw'
# res = requests.get(currency_url,verify=False,headers={"User-Agent": "Mozilla/5.0"})
#
# print(res)
# soup = BeautifulSoup(res.text,'html.parser')
#
# # 환율 정보
# usd_krw=soup.select_one('#last_last').get_text()
#
#
# # 역프 가져오기
# premium_url = 'https://luka7.net/'
# res = requests.get(premium_url,verify=False,headers={"User-Agent": "Mozilla/5.0"})
# soup = BeautifulSoup(res.text,'html.parser')
# time.sleep(1)
# usd_krw=soup.select_one('#coinList > div.row.val.BTC > div.usdPrm.minus')
#
# print(res.text)
# print(soup.select('#coinList > div.row.val.BTC'))
#

# 공통
PAUSE_TIME = 2

# 셀레니움 로드
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")

driver = webdriver.Chrome(executable_path='./chromedriver',options=options)

# 묵시적 대기시간 설
driver.implicitly_wait(time_to_wait=10)

# 환율 정보
url = 'https://www.google.com/search?newwindow=1&biw=1200&bih=683&sxsrf=ALeKk00h9FYH2hEYe_YmZj9if6lN7jTuLA%3A1613001970811&ei=8nQkYMbvMMm3mAXcjKrQBQ&q=USD+KRW&oq=USD+KRW&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEMsBEEYQggIyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywE6BwgAEEcQsAM6BAgjECc6BAgAEEM6AggAOgcIABAUEIcCOgIILjoJCCMQJxBGEIICUKxBWOtOYJtVaAFwAngAgAG6AYgBswiSAQMwLjeYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwjGsPfLxODuAhXJG6YKHVyGCloQ4dUDCA0&uact=5'
driver.get(url=url)
WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_all_elements_located( (By.CSS_SELECTOR,'#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.vk_bk.gsrt.gzfeS > span.DFlfde.SwHCTb') )
)
time.sleep(2) # 필

exchangeRate = driver.execute_script("return document.querySelector('#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.vk_bk.gsrt.gzfeS > span.DFlfde.SwHCTb').textContent")
print('환율: ',exchangeRate)

# 역프 정보
url = 'https://www.luka7.net'
driver.get(url=url)

# AJAX 동기화 대기간
# 일단 동작하는 코드
# WebDriverWait(driver, 10).until(
#     expected_conditions.presence_of_all_elements_located( (By.CSS_SELECTOR,'#coinList > div.row.val.BTC') )
# )
# time.sleep(2) # 필

# WebDriverWait로는 원하는대로 동작하지 않아서 직접적인 형태로 조치
while True:
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_all_elements_located( (By.CSS_SELECTOR,'#coinList > div.row.val.BTC') )
    )
    check = driver.execute_script("return document.querySelector('#coinList > div.row.val.BTC > div.usdPrm').textContent")

    if check != '':
        break
    else:
        time.sleep(1)

premium = driver.execute_script("return document.querySelector('#coinList > div.row.val.BTC > div.usdPrm').textContent")
pos_s, pos_e = premium.find('('), premium.find('%')
premium_rate = premium[pos_s+1:pos_e]   # 대상 샘플 : -1,034,710.00 (-2.09%)
print('프리미엄: ',premium)
print('프리미엄 비율: ',premium_rate)


# 3. 가격범위 a - b 입력받기
price_a = input()
price_b = input()

print('price range :',price_a,' ~ ',price_b)





driver.close()