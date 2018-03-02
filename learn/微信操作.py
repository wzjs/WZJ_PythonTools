#_*_coding:utf-8_*_
import itchat
import re
from echarts import Echart,Legend,Pie
import jieba

itchat.login()

itchat.send(u"Hello,wechat","filehelper")

friends = itchat.get_friends(update=True)


# male = female = other = 0

# for i in friends[1:]:
# 	sex = i["Sex"]
# 	if sex == 1:
# 		male+=1
# 	elif sex == 2:
# 		female+=1
# 	else:
# 		other+=1

# total = len(friends[1:]) 
# print(u"男性朋友:%.2f%%" % (float(male)/total * 100))
# print(u"女性朋友:%.2f%%" % (float(female)/total * 100))
# print(u"中性朋友:%.2f%%" % (float(other)/total * 100))

# chart = Echart(u"%s的微信男女比例饼状图" % friends[0]['NickName'],"from wechat")
# chart.use(Pie("wechat",[
# 		{'value':male,'name':"男性%.2f%%"%(float(male)/total * 100)},
# 		{'value':female,'name':"女性%.2f%%"%(float(female)/total * 100)},
# 		{'value':other,'name':"中性%.2f%%"%(float(other)/total * 100)}],
# 		radius=["50%","70%"]))
# chart.use(Legend(["male","female","other"]))
# chart.plot()


tList = []
for i in friends:
	signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
	rep = re.compile("1f\d.+")
	signature = rep.sub("", signature)
	tList.append(signature)

text  = "".join(tList)

wordList = jieba.cut(text,cut_all=True)

wl_space_split = " ".join(wordList)

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import PIL.Image as Image

# 这里要选择字体存放路径，这里是Mac的，win的字体在windows／Fonts中
my_wordcloud = WordCloud(background_color="white", max_words=2000, 
                         max_font_size=40, random_state=42,
                         font_path='C:\Windows\Fonts\Arial\arial.ttf').generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()


