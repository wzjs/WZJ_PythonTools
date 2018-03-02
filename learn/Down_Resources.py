from bs4 import BeautifulSoup
import requests
import re
_input = input("please input want find...")
request = requests.get("http://www.btcerise.info/search?keyword=%s" %_input)

soup = BeautifulSoup(request.text,"html.parser")
first = soup.find(text=re.compile("收录时间"))
for x in first.parent.parent.stripped_strings:
	if x == "磁力链接":
		continue
	print(x)
url = soup.find("a",href=re.compile("magnet:"))
print("迅雷链接:"+url['href'])
name = soup.find('h5')
print("标题:",end="")
for x in name.stripped_strings:
	print(x,end="")

