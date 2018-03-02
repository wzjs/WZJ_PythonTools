from splinter.browser import Browser

# b = Browser(driver_name="chrome")

# b.visit("http://www.baidu.com")
# browser = Browser(driver_name='chrome')
# browser.visit('http://www.baidu.com')

# browser.fill('wd','这是一个测试')

# btn=  browser.find_by_id("su")
# btn.click()

# with Browser("chrome") as b:
# 	b.visit('http://www.baidu.com')
# 	b.reload()
# b = Browser('chrome')
# b.visit('http://www.baidu.com')
# b.visit('http://www.360.com')
# # b.reload()
# print(b.title)
# b.back()
# b.forward()

b = Browser("chrome")

b.visit("http://www.baidu.com/")

b.cookies.add({'BDUSS': 'jY4bi1pb1Rpc3hyOVZmWHlXRTlnSkNXd29JdWtkdUlabWRpTHZJfn5xS0N5cGhhQVFBQUFBJCQAAAAAAAAAAAEAAABUPe0avty'})

# print(b.find_by_id("lg")[0])
# print(b.find_by_id("u1")[0].name)
# print(b.find_by_name('rn'))
# print(b.find_by_css('p').value)
# print(b.find_*('rn'))
# b.find_by_text("更多产品").mouse_over()
# print(b.find_by_name('tj_briicon'))
# print(b.find_by_text("输入法")[0])
# print(b.find_by_value("百度一下")[0])
# print(b.find_by_css("textarea")[0])
# 
# b.check()

# b.click_link_by_partial_text("超市")
# b.click_link_by_partial_href("travel")
# b.windows.current = b.windows[1]
# print(b.windows.current )
# print(b.windows)
# b.windows.current = b.windows[0]
# print(b.title)

# data = b.find_by_xpath("//title")
# data = b.find_by_text("新闻")
# print(b.html)
# print(data[0].text+"ffffffffffffff")
# a = b.find_by_xpath('//audio[@controls="controls"]')
# print(b.html)
# print(a)

