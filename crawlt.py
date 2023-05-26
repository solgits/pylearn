import sys
import os
import time
from chromedriver import generate_chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def crawlt(driver: webdriver, headless: bool=False, tab: int=0):

    try:

        if(tab >= 0) :
            tabs = driver.window_handles
            driver.switch_to.window(tabs[tab])
        # 페이지
        driver.get("https://google.com/")
        # 요소검색시 10초간 대기 > 요소발견시 다음진행
        wait = WebDriverWait(driver, 10)

        # 10초대기
        time.sleep(5)
        
        cur_url = driver.current_url
        #print(driver.current_url)
    except TimeoutException as te:
        #print('not found!!')
        raise Exception(str(te))
    except Exception as e:
        #print(str(e))
        raise Exception(str(e))
    finally:
        #driver.quit()
        pass
    
    return cur_url
''''''
try:
    #print(crawlt(False))
    pass
except Exception as e:
    print(str(e))
