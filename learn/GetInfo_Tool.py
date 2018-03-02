import re
import requests
import os


f = open("D:/log.txt",'a')

for x in range(1,2):
	try:
		print(x)
		# global url
		url = "http://www.youwonn.com/options/xinwenzixun/list_7_%s.html" %x

		if x == 1:
			url = "http://www.youwonn.com/options/xinwenzixun/"

		r = requests.get(url)
		arr = re.findall(r'/options/xinwenzixun/\d+.html',r.text)
		for y in set(arr):
			url1 = "http://www.youwonn.com%s" %y
			r = requests.get(url1)
			r.encoding = 'utf-8'
			arr1 = re.findall(r'<div class="new_title">\s*<p>(.*)</p>\s*<span>(.*)</span>\s*</div>\s*<div class="newxq_con new_p">\s*<p><p>(.*)</p>\s*</p>',r.text)
			print(url1)
			print(arr1)
			f.write('''
{
title: '%s',
description: '%s',
content:'<p></p>',
release_time: '%s'
}

					''' %(arr1[0][0],arr1[0][2].strip(),arr1[0][1]))

	except Exception as e:
		continue
f.close()