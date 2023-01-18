import sys
import os
import time
from chromedriver import generate_chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.common.exceptions import TimeoutException

def crawl1(headless: bool=False):
    # 크롬 드라이버 인스턴스 생성    
    driver = generate_chrome(headless=headless)
    
    #return "aaa"

    try:

        # 3초대기
        driver.implicitly_wait(5)
        # 페이지
        driver.get("https://todaync.com/")
        # 요소검색시 10초간 대기 > 요소발견시 다음진행
        wait = WebDriverWait(driver, 10)
        # 창최대화
        driver.maximize_window()

        # 팝업닫기
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='hd_pops_1']/div[2]/button[2]"))).click()
        # 팝업닫기
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='hd_pops_2']/div[2]/button[2]"))).click()
        
        # 로그인버튼 id찾아서 클릭
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#outlogin_wrap_open"))).click()
        # ID입력칸 id찾아서 값 전송
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#login_id"))).send_keys('parklry')
        # PW입력칸 id찾아서 값 전송
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#login_pw"))).send_keys('t1979suk!')
        # 로그인버튼 id찾아서 클릭
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#login_auto_login"))).click()

        # 포인트존
        driver.get("https://todaync.com/bbs/board.php?bo_table=attend")
        # 출석
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#talk_submit"))).click()
        try:
            alert = driver.switch_to.alert()
            # 취소하기(닫기)
            #alert.dismiss()
            # 확인하기
            alert.accept()
        except:
            pass

        time.sleep(10)

        # 홍보존
        driver.get("https://todaync.com/bbs/board.php?bo_table=hongbo_diablo")
        # 디아블로
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='fboardlist']/div[2]/div[1]/div/a[2]"))).click()

        #글쓰기
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#wr_subject"))).send_keys('디아2 NOWDIA (골드,보석,물약자동줍기/카나이함)')

        # class selector를 이용해 iframe을 확인합니다.
        editor_frame = driver.find_element_by_css_selector('.col-sm-12 iframe')

        # 확인된 ifrime으로 변경합니다.
        driver.switch_to_frame(editor_frame)
        # html 버튼
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='smart_editor2_content']/div[4]/ul/li[2]/button"))).click()
        # 글작성
        send_hongbo = ("디아2 NOWDIA (골드,보석,물약자동줍기/카나이함)"
                       "<br>"
                       "<p><a href='https://nowdia2.cc/tto/adclicks/54389'><span style='font-size:12pt;'><b>https://nowdia2.cc</b></span></a></p>"
                       "<p><a href='https://nowdia2.cc/tto/adclicks/54389'><span style='font-size:12pt;'><b>https://nowdia2.cc</b></span></a></p>"
                       "<br>"
                       "<a href='https://nowdia2.cc/tto/adclicks/54389'><img src='https://nowdia2.cc/data/apms/background/prnew.jpg' alt='nowd2.com'></a></p>"
                       "<br>"
                       "<p><a href='https://nowdia2.cc/tto/adclicks/54389'><span style='font-size:12pt;'><b>https://nowdia2.cc</b></span></a></p>")
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='smart_editor2_content']/div[3]/textarea[1]"))).send_keys(send_hongbo)
        # Editor 버튼
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='smart_editor2_content']/div[4]/ul/li[1]/button"))).click()

        # ifrime에서 원래 frame으로 돌아옵니다.
        driver.switch_to_default_content()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#btn_submit"))).click()

        #10초대기
        time.sleep(10)
        
        cur_url = driver.current_url
        #print(driver.current_url)
    except TimeoutException as te:
        #print('not found!!')
        raise Exception(str(te))
    except Exception as e:
        #print(str(e))
        raise Exception(str(e))
    finally:
        driver.quit()
    
    return cur_url
''''''
try:
    #print(crawl1(False))
    pass
except Exception as e:
    print(str(e))
