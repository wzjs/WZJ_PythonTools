import socket
import threading
import os
import requests
from flask import Flask
from flask import request
from bs4 import BeautifulSoup
import json
global sock

#实现通过微信控制手机app定位发送给服务器显示位置信息

loca = "welcome"
app = Flask(__name__)

#搭建web服务器通过socket发送消息给app索取定位信息，然后转发给微信服务器
@app.route("/wx_check",methods=["POST","GET"]) #这里用了一个Web框架   "/wx_check" 是你在微信中填的开发者服务器路径
def application():
	openID = request.args['openid'] # 微信发的,详见开发者文档
	soup = BeautifulSoup(request.data,"html.parser")
	content = soup.find("content") # content 是微信用户发的消息,可用来验证用户
	sock.send(b"getlocation") #  发送信息通知android
	global loca
	while True:  #手动阻塞
		if loca != "welcome":
			break
	back = loca
	loca = "welcome"
	return """
	<xml> 
	<ToUserName>%s</ToUserName> 
	<FromUserName>qqmsssssssss</FromUserName>
	<CreateTime>12345678</CreateTime> 
	<MsgType>text</MsgType> 
	<Content>%s</Content> 
	</xml>"""%(openID,back)
def start():
	app.run('0.0.0.0',80)
threading.Thread(target=start,args=()).start()

# 与app进行socket连接 接受定位信息 另外用到经纬度兼容转换API 和经纬度转位置API
def tcplink(sock,addr):
	try:
		print('Accept new connection from %s:%s...' % addr)
		while True:
			sock.setblocking(True)
			data = sock.recv(1024)
			location = data.decode('utf-8')
			print("client:"+location)
			# 以下进行经纬度 地图信息的转换 loca为app所在地址接上面的 堵塞
			if location != "":
				global loca
				print(location)
				lis = location.split(",")
				location = "%s,%s"%(lis[1],lis[0])
				print(location)
				xml = requests.get("http://api.gpsspg.com/convert/coord/?oid=7820&key=AE9175EA3FFD63B3910CF0332D1ACA28&from=0&to=3&latlng=%s&output=xml"%location)
				soup = BeautifulSoup(xml.text,"html.parser")
				print(soup.text)
				lat= soup.find("lat").string
				lng= soup.find("lng").string
				location = "%s,%s"%(lng,lat)
				print("after"+location)
				a = requests.get("http://restapi.amap.com/v3/geocode/regeo?key=afac014631ef858bf4a209b8446b327a&location="+location)
				loca = a.text
				obj = json.loads(loca)
				loca = obj["regeocode"]["formatted_address"]
			else:
				print("socket is close,waiting new accept")
				sock.close()
				break
	except Exception as e:
		location = "raise error"
	finally:
		pass
	

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(('0.0.0.0',9999))
	s.listen(10)
	print('waiting to connect')

	while True:
		sock,addr = s.accept()	 #等待app来连接
		t = threading.Thread(target=tcplink,args=(sock,addr))
		t.start()
	
finally:
	print("ending")
