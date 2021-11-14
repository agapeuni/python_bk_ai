# Microsoft Bing 사이트에서 특정 검색어에 대한 이미지를 크롤링해 오는 프로그램
# 이미지를 크롤링하여 폴더에 저장하고, 데이터셋을 만들어 학습시키기
# Microsoft Bing 외에도 중국 포털 바이두Baidu, 구글을 통해 이미지 크롤링이 가능
# py -m pip install icrawler 모듈을 설치할 것

from icrawler.builtin import BingImageCrawler
# from icrawler.builtin import BaiduImageCrawler, GoogleImageCrawler

############## 검색어 및 크롤링 이미지 갯수 설정 ##############
key_word = input('검색어:')       # 검색어 설정 ex) dog, cat, horse, 개, 고양이....
crawl_num = int(input('크롤링 이미지 갯수:'))  # 크롤링 최대 갯수  ex) 100

############## MS Bing을 통한 이미지 크롤링 ##################
bing_crawler = BingImageCrawler(
    feeder_threads = 1,
    parser_threads = 1,
    downloader_threads = 4, 
    storage = {'root_dir':'iCrawler\\'+key_word} ) # 현재 디렉토리/iCrawler/검색어

bing_crawler.crawl(keyword=key_word, filters=None, offset=0, max_num=crawl_num)

print('Image Crawling is done.')