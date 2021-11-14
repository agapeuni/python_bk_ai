# chrom 브라우저로 설정, 반드시 chromdriver.exe 파일이 같은 폴더 내에 있어야 함.
# Google Chrom 브라우저에서 이미지 검색창에 검색어를 입력하고
# 엔터키 누르고, 이미지를 선택하여 모아오기
# 스크롤링을 하여 모든 이미지르 가져오기 위한 코드

from selenium import webdriver              # py -m pip install selenium
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl") # Google 이미지 검색 
elem = driver.find_element_by_name("q")                        # 검색창 부분
elem.send_keys("xylobot")                                      # 검색어 입력
elem.send_keys(Keys.RETURN)                                    # Enter키를 눌러 검색

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: # 스크롤이 끝까지 내려갔다면
        try:                      # 이미지 더 보기 버튼을 클릭해 줌.
            driver.find_element_by_css_selector(".mye4qd").click()
        except:                   #  더이상 이미지 더 보기가 없으면 작업을 끝냄.
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1               # 이미지 파일 이름을 1,2,3...으로 하기 위한 초기화
for image in images:
    try:
        image.click()   # 첫 번째 이미지 선택
        time.sleep(3)   # 이미지 사이트 검색을 위해 3초간 쉼.
        imgURL = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        # 아래 줄의 폴더 경로 부분은 자신의 PC에 맞추어 변경하기 
        outpath = "D:/AI Study/ImageCrawling/Images/xylobot/" # 이미지를 저장할 폴더 
        outfile = str(count) + ".jpg"
        urllib.request.urlretrieve(imgURL, outpath+outfile)
        count = count + 1
    except:
        pass

driver.close()    # 마지막에는 드라이버를 닫아 줌.