import tkinter as tk
from crawl1_todaync import crawl1
from crawl2_poplin1 import crawl2
from crawl3_hbking import crawl3
from crawl4_gamezone import crawl4
from crawl5_linpop2023 import crawl5
from crawl0_nowdia2 import crawl_hongbo

def crawl(idx):
    cur_url = idx
    if idx == 0:
        cur_url = crawl1(False)
    elif idx == 1:
        cur_url = crawl2(False)
    elif idx == 2:
        cur_url = crawl3(False)
    elif idx == 3:
        cur_url = crawl4(False)
    elif idx == 4:
        cur_url = crawl5(False)
    
    text.insert(tk.END,"{}. {}\n".format(idx+1,cur_url))

    return

def crawlAll(idx):
    for i in range(idx): 
        crawl(i)

    writeEvent()
    return

def writeEvent():
    #text.insert(tk.END,"{}. {}\n".format(1,"https://todaync.com/bbs/board.php?bo_table=hongbo_diablo&wr_id=17056"))
    #text.insert(tk.END,"{}. {}\n".format(2,"https://poplin1.xyz/bbs/board.php?bo_table=0304&wr_id=2355"))
    #text.insert(tk.END,"{}. {}\n".format(3,"https://hb-king.xyz/index.php?mid=GAMES&document_srl=255517"))
    #text.insert(tk.END,"{}. {}\n".format(4,"http://gamezone.live/index.php?mid=board_WLoA38&document_srl=12374892"))
    #text.insert(tk.END,"{}. {}\n".format(5,"http://www.linpop2023.com/bbs/board.php?bo_table=d_game&wr_id=3581"))
    
    if text.get(5.0, 5.1) == '5':
        result = text.get(1.0, tk.END+"-1c")
        cur_url = crawl_hongbo(False,result)
        print(cur_url)
    
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
    