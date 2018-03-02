from splinter.browser import Browser


cookie_manager.add({'BDUSS': 'jY4bi1pb1Rpc3hyOVZmWHlXRTlnSkNXd29JdWtkdUlabWRpTHZJfn5xS0N5cGhhQVFBQUFBJCQAAAAAAAAAAAEAAABUPe0avty--NbcwNbE3VQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAII9cVqCPXFac'})

browse = Browser("chrome")


try:
	browse.visit("http://www.12306.cn")
except Exception as e:
	raise
finally:
	print(browse.title)



browse.click_link_by_href("https://kyfw.12306.cn/otn/index/init")

# print(browse.html)
browse.windows.current = browse.windows[1]
# browse.find_by_id("fromStationText")[0].fill("上海")
# browse.find_by_id("toStationText")[0].fill("郑州")

# browse.fill("leftTicketDTO.from_station_name","上海")
# browse.fill("leftTicketDTO.to_station_name","郑州")
# print(browse.html)

browse.find_by_id("from_station_imageB")[0].click()

print(browse.html)
btn = browse.find_by_xpath("//li[@data='SHH']")
btn[0].click()

btn = browse.find_by_xpath("//li[@data='ZZF']")
btn[0].click()

btn = browse.find_by_id("a_search_ticket")
btn.click()


