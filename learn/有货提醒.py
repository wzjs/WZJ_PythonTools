from bs4 import BeautifulSoup
import requests
import re
from splinter.browser import Browser
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
while True:
	req = requests.get("https://c0.3.cn/stock?skuId=6199058&area=15_1233_42324_52189&venderId=1000004319&cat=670,12800,12801&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=1131171708&pdpin=wzjsssssssss&detailedAdd=null&callback=jQuery3349251")

	soup = BeautifulSoup(req.text,"html.parser")

	a = soup.find(text="无货")
	print(a)
	if a == None:
		app = Application()
		app.master.title('Hello World')
		app.mainloop()
		break;



# //<a href="//cart.jd.com/gate.action?pid=6199058&pcount=1&ptype=1" id="InitCartUrl" class="btn-special1 btn-lg "  clstag="shangpin|keycount|product|加入购物车_1">加入购物车</a>
# //<a href="//cart.jd.com/gate.action?pid=6199058&pcount=1&ptype=1" id="InitCartUrl" class="btn-special1 btn-lg "  clstag="shangpin|keycount|product|加入购物车_1">加入购物车</a>



