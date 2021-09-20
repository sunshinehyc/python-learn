# 本程序来源于百度翻译的api
# 你可以把它当作一个翻译程序
import requests
import tkinter as tk
from tkinter import END


def fanyi(keyword):
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    }
    data = {
        "kw": keyword
    }
    respone = requests.post(url=url, headers=headers, data=data)
    messages = respone.json()
    return messages['data']


window = tk.Tk()
window.title('翻译程序')
window.geometry('400x500')
listk = []
var1, var2 = '', ''


def hitme():
    global listk
    kw = entry1.get()
    messages = fanyi(kw)
    listk = messages[:]
    listbox.delete(0, END)
    for message in messages:
        # listk.append(message)
        en = message['k']
        cn = message['v']
        encn = f'{en}--->{cn}'
        listbox.insert('end', encn)


entry1 = tk.Entry(master=window)
entry1.pack()
button = tk.Button(master=window, text='翻译', command=hitme)
button.pack()
listbox = tk.Listbox(window, width=400, height=10, selectbackground='grey', yscrollcommand=True)
listbox.pack()
label1 = tk.Label(master=window, text='', wraplength=80, )
label2 = tk.Label(master=window, text='', wraplength=400, )


def xianshi():
    global var1, var2
    selectme = listbox.curselection()
    sel = selectme[0]
    var1 = listk[sel].get('k')
    # print(listk)
    var2 = listk[sel].get('v')
    label1.configure(text=var1)
    label2.configure(text=var2)


buttom2 = tk.Button(master=window, text='完整显示', command=xianshi)
buttom2.pack()
label1.pack()
label2.pack()

window.mainloop()

