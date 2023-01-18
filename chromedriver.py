import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

def _enable_download_in_headless_chrome(driver: webdriver):
    """
    :param driver: 크롬 드라이버 인스턴스
    :param download_dir: 파일 다운로드 경로
    """
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow'
        }
    }
    driver.execute("send_command", params)
    
def generate_chrome(
    headless: bool=False
    ) -> webdriver:

    options = Options()
    if headless:
        options.add_argument('--headless') # 창숨기기
        options.add_argument('--disable-gpu') # 그래픽가속끄기
        options.add_argument('--disable-software-rasterizer') # 
    options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "hide_console": True
    })
    options.add_argument('--disable-extensions') # 크롬확장 비활성화
    
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

    try:
        chrome = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)   
    except:
        chromedriver_autoinstaller.install('./')
        chrome = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)

    if headless:
        _enable_download_in_headless_chrome(chrome)
    
    return chrome

'''
try:
    generate_chrome(False)
except Exception as e:
    print(e)
'''