
## 思路是用正则或者美丽的汤(此处用的是正则)爬取主页上的所有网页链接和图片链接,保存到指定目录,在通过递归来检索所有网页
## 不保证对所有网页都通用
import re
import requests
import os
import threading

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
urls = []
path = "D://well/%s" # image location 
CONFIG_NAME = "dict.txt" #用来缓存已经下载过的网页,可用于下次继续上一次的图片下载
URL = "http://lolisz.com/"
#
def GetImage(url,path):
	global urls
	request = requests.get(url,headers=headers)
	code = request.text
	matchs= re.findall("(?:src|href)=\"?(h[^\"]*jpg)",code)
	print("本页面张数:%s"%len(matchs))
	txt = open(path%CONFIG_NAME,"a")
	b=0
	matchs = [x for x in matchs if x.split("/")[-1] not in os.listdir(path%"")]
	print(matchs)
	for x in matchs:
		try:
			print(x)
			request = requests.get(x,headers=headers)
			x = x.split("/")[-1]
			if len(x) > 200:
				x = x[-200:-1]
			print(x)
			with open(path%x,"wb") as bs:
				bs.write(request.content)
			b+=1
			print("%s/%s"%(b,len(matchs)))
		except Exception as e:
			print(e)
		


	matchs = re.findall("href=\"(http[^\"]*html)\"",code)
	for x in matchs:
		print(x)
		if x in urls:
			print(x+"----------urls ")
			continue
		urls.append(x)
		txt.write("%s,"%x)
		# threading.Thread(target=GetImage,args=(x))
		GetImage(x,path)
	txt.close()

def ReadConfig(path):
	if not os.path.isfile(path):
		return
	global urls
	with open(path,"r") as txt:
		t = txt.read()
	urls = [URL]
	for x in t.split(','):
		urls.append(x)

if __name__ == '__main__':
	ReadConfig(path%CONFIG_NAME)
	GetImage(URL,path)

