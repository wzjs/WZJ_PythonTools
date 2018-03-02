import requests
import re
import json
from bs4 import BeautifulSoup

while(1):
	x = input("please input ...")
	r = requests.get('http://www.iciba.com/%s' %x)
	# g = re.findall(r'(<span class="prop">.*</span>\s*<p>\s*)(.*)(\s*</p>)',r.text)
	# g = re.findall(r'<span class="prop">.*</span>\s*<p>(\s*<span>(.*)</span>)+\s*</p>',r.text)

	# print(g)
	soup = BeautifulSoup(r.text,"html.parser")
	lis= soup.find_all("span","prop")

	for x in lis:
		for y in x.find_next_sibling('p').find_all("span"):
			print(y.string)

# a = re.match(r"<span>%s[a-zA-z\u4e00-\u9fa5]*</span>" %'Anim','<span>Animaaa</span>')
# print(a)