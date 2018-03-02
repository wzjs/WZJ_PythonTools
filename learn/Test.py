#coding=utf-8
from bs4 import BeautifulSoup
import re
from PIL import Image
import pytesseract

# html = "<html id=1><head><title>The Dormouse's story</title></head><p><p id=1>aaaa你好</p></p><p id>bbb Hello world</p></html>"
# soup = BeautifulSoup(html,"html.parser")

# a = soup.find_all(text=re.compile("你好"))
# print(soup.strings)

# for x in soup.strings:
# 	print(x) 
# print(soup.html.children)
# print(soup.html.contents)
# print(soup.html.descendants)

# for x in soup.html.descendants:
# 	print(x) 
# print(soup.html.strings)

# for x in soup.html.stripped_strings:
# 	print(x)
# print(soup.head.parent)

# for x in soup.title.parents:
# 	if not x.parent:
# 		print(x.name)
# 	else: 
# 		print(x)

# print(soup.head.next_sibling)
# print(soup.html.contents[2].next_sibling)

# for x in soup.head.next_siblings:
# 	print(x)
# print(soup.p.next_element)

# for x in soup.p.previous_elements:
# 	print(x)



# print(soup.html.find_all(text=re.compile("Hello"),limit=1,recursive=False))
# print(html.div.find_parents("html"))
# print(soup.html.head.find_next_siblings(text=re.compile("Hello")))

# text=pytesseract.image_to_string(Image.open('D:/e.png'),lang="chi.sim")
# print(text)

# img = Image.open("D:/x.jpg")
# w,h = img.size
# pixdata = img.load()
# for x in range(w):
# 	for y in range(h):
# 		# if pixdata[x,y] < (100,100,160) or pixdata[x,y] > (140,180,190):
# 		# 	pixdata[x,y] = 0

# img.save("D:/img1.jpg")

# print('''
# n=123
# f=456.789
# s1='Hello,world'
# s2='Hello,\'Adam\''
# s3=r'Hello,"Bart"'
# s4=r\'''Hello,\nLisa!''\'
# ''')

# print('''
# ''
# 	''')

import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(("www.sina.com.cn",80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# buff = []
# while True:
# 	d = s.recv(1024)
# 	if d:
# 		buff.append(d)
# 	else:
# 		break
# print(buff)

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# print(buffer)
# print(data.decode('utf-8'))
# import threading
# s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',9999))
# s.listen(5)
# print("start listen...")
# def HandleClient(sock,addr):
# 	while True:
# 		data = sock.recv(1024)
# 		if not data or data.decode("utf-8") == 'exit':
# 				break
# 		print("%s:%s" %(addr[0],addr[1]),data.decode("utf-8"))	
# 		send = input("please send to client:")	
# 		sock.send(send.encode("utf-8"))
# 	sock.close()

# while True:
# 	sock,addr = s.accept()
# 	thread = threading.Thread(target=HandleClient,args=(sock,addr))
# 	thread.start()

# UDP
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('127.0.0.1',9999))
# data,addr =  s.recvfrom(1024)
# print(data.decode('utf-8').encode('ascii'))
# s.sendto(b'Hello,client',addr)

# a = range(10)
# _min,_max = a[0:2]
# print(a[0:2])
# b = range(0,2)
# print(b)
# for x in a:
# 	if _min > x:
# 		_min = x
# 	if _max < x:
# 		_max = x
# print(_min,_max)

# from tkinter import *
# import tkinter.messagebox as messagebox 
# class Application(Frame):
# 	def __init__(self,master=None):
# 			Frame.__init__(self,master)
# 			self.pack()
# 			self.CreaterUI()
# 	def CreaterUI(self):
# 		# self.test_TextUI = Label(self,text="Hello,World")
# 		self.test_TextUI = Entry(self)
# 		self.test_TextUI.pack()
# 		self.test_ButtonUI = Button(self,text="im a btn",command=self.inputFunc)
# 		self.test_ButtonUI.pack()
# 	def inputFunc(self):
# 		name = self.test_TextUI.get() or "world"
# 		messagebox.showinfo('message',name)

# app = Application()
# app.master.title("this is a title")
# app.mainloop()

# def Application(environ,start_response):
# 	start_response('200 OK',[('Content-Type','text/html')])
# 	return [b'<h1>Hello,World</h1>']

# from wsgiref.simple_server import make_server

# httpd = make_server('',8000,Application)
# print("start listen...")
# httpd.serve_forever()

# import asyncio

# def CanChangeFunc(*params,name="xiaoli", city,job):
# 	for x in params:
# 		print(x)

# 	print(city)
# 	print(job)

# CanChangeFunc(1,2,3,4,5,6,city="sh",job="hw")


# def log(func):
# 	def wrap(*arg,**argss):
# 		print("this is a func")
# 		return func(*arg,**argss)
# 	return wrap

# @log
# def f(*arg,**argss):
# 	print("func self")
# 	print(arg)
# 	print(argss)

# now = log(f)
# print(now(1,2,3,4))

# f(1,2,3,4)

# from splinter.browser import Browser

# b = Browser(driver_name="chrome")

# b.visit("http://www.baidu.com")
# browser = Browser(driver_name='chrome')
# browser.visit('http://www.baidu.com')
# import jieba

# a = jieba.cut("我们中出了一个叛徒")
# print(type(a))
# print('/'.join(a))

# from echarts import Echart,Legend,Pie


# male = 1
# female = 2
# other = 5
# total = 7
# print(u"男性朋友:%.2f,%.2f" % ((float(male) / total * 100),(float(male) / total * 100)))
# friends = [{'NickName':"wzj"}]
# # chart = Echart(u"%s的微信男女比例饼状图" % u"wzj",u"from wechat")
# # chart.use(Pie("wechat",[
# # 		{'value':male,'name':u"男性%.2d"%(float(male)/total * 100)},
# # 		{'value':female,'name':u"女性%.2d"%(float(female)/total * 100)},
# # 		{'value':other,'name':u"中性%.2d"%(float(other)/total * 100)}],
# # 		radius=["50%","70%"]))


# chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
# chart.use(Pie('WeChat',
#               [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
#                {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
#                {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
#               radius=["50%", "70%"]))
# chart.use(Legend(["male", "female", "other"]))
# del chart.json["xAxis"]
# del chart.json["yAxis"]
# chart.plot()

str = "sssssaaa</span>"

s = str.split("<span ")

print(s[0][0])

