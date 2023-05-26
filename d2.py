import tkinter as tk
from chromedriver import generate_chrome
from crawl1 import crawl1
from crawlt import crawlt

def crawl(idx):
    cur_url = idx
    driver = generate_chrome(False)
    driver.maximize_window()
    driver.implicitly_wait(5)
    if idx == 0:
        cur_url = crawlt(driver, False, -1)
    elif idx == 1:
        cur_url = crawlt(driver, False, -1)
    elif idx == 2:
        cur_url = crawlt(driver, False, -1)
    elif idx == 3:
        cur_url = crawlt(driver, False, -1)
    elif idx == 4:
        cur_url = crawlt(driver, False, -1)
    
    text.insert(tk.END,"{}. {}\n".format(idx+1,cur_url))

    driver.quit()

    return

def crawlAll(idx):
    text.delete("0.0","end")

    driver = generate_chrome(False)
    # 창최대화
    driver.maximize_window()
    # 5초대기
    driver.implicitly_wait(5)

    # 탭별크롤링
    for i in range(idx): 
        driver.execute_script('window.open("about:blank", "_blank");')
        cur_url = crawlt(driver, False, i)
        text.insert(tk.END,"{}. {}\n".format(i+1,cur_url))

    driver.quit()
    #writeEvent()
    return

def writeEvent():
   
    if text.get(5.0, 5.1) == '5':
        result = text.get(1.0, tk.END+"-1c")
        #cur_url = crawl_hongbo(False,result)
        #print(cur_url)
    
    return

# GUI 창을 생성합니다.
root = tk.Tk()
root.title("Web Crawler")
root.geometry("600x480+300+300") #가로 *세로 +x +y

# 텍스트 파일에서 웹 주소를 읽어옵니다.
with open("urls.txt") as f:
    urls = f.readlines()

# 웹 주소를 표시할 라벨을 생성합니다.
for i, url in enumerate(urls):
    # IntVar 객체를 생성합니다.
    chk = tk.IntVar()

    checkbutton = tk.Checkbutton(root, text="{}".format(url), variable=chk)
    checkbutton.grid(row=i, column=0, sticky="nsw", padx=10, pady=10)
    #checkbutton.pack()
    button = tk.Button(root, text="실행", command=lambda i=i:crawl(i))
    #button = tk.Button(root, text="실행", command=crawl(i))
    button.grid(row=i, column=1, sticky="nsw", padx=10, pady=10)
    #button.pack()
    root.rowconfigure(i, minsize=40)

last = i+1
allbutton = tk.Button(root, text="전체실행", command=lambda i=last:crawlAll(i))
allbutton.grid(row=last, column=0, sticky="nsw", padx=10, pady=10)

evtbutton = tk.Button(root, text="이벤트작성", command=lambda:writeEvent())
evtbutton.grid(row=last, column=1, sticky="nsw", padx=10, pady=10)

text = tk.Text(root)
text.place(x=10 , y=350, width=550, height=100)

# 윈도우 좌우에 100의 여백을 추가합니다.
# root.pack(padx=100)

root.mainloop()
