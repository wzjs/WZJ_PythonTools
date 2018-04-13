import requests
import json
import os
HEADRS = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

}
POSITION = "1(35,39),2(98,45),3(183,44),4(253,42),5(47,119),6(95,125),7(200,125),8(265,128)"
URL_YANZHENGMA = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.5004204286123859"
URL_LOGIN = "https://kyfw.12306.cn/passport/web/login"
URL_CHECK = "https://kyfw.12306.cn/passport/captcha/captcha-check"
FROM_DATA = {
	'answer':'',
	'login_site':'E',
	'rand':'sjrand'

}

Login_DATA = {
	'username':'wzj357280973',
	'password':'2018nian',
	'appid':'otn'
}

class Loginer12306(object):
	"""docstring for Loginer"""
	def __init__(self):
		self.session = requests.Session()
		self.session.headers = HEADRS
		self.urlCaptcha = URL_YANZHENGMA
		self.urlCheck = URL_CHECK

	def Checkcaptcha(self):
		rsp = self.session.get(self.urlCaptcha)
		# print("cookie befor:%s"%self.session.cookies)
		with open("D://captcha.png",'wb') as op:
			op.write(rsp.content)
		os.startfile("D://captcha.png")
		position = input("请输入验证码...")
		FROM_DATA.update({'answer':position})
		rsp = self.session.post(self.urlCheck,data=FROM_DATA)
		# print("cookie after:%s"%self.session.cookies)
		print(rsp.text)
		jsn = json.loads(rsp.text)
		print(type(jsn))
		if jsn["result_code"] == '4':
			return True
		else:
			return False

	def Login(self):
		rsp  = self.session.post(URL_LOGIN,data=Login_DATA)
		js = json.loads(rsp.text)
		print(js)
		if js["result_code"] == 0:
			print("登录成功")
		else:
			print("登录失败")

if __name__ == '__main__':
	print(POSITION)
	loginer = Loginer12306()
	while  True:
		if loginer.Checkcaptcha():
			loginer.Login()
			break;
	

#https://kyfw.12306.cn/otn/login/checkUser
# _json_att:



# https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest
# secretStr:WqWMokPjARk0wnw8wmnj6OoV+A2cSOvVWh24W0WsvLsLeOqn5jbYkj5Tp6m4lNrrd0229jrIetuO
# 2i3IaCaIDCU3F13NhH3KpJNCqKbGKT7EfOJhKOYlN/AA+foPMnUqeYOVpHguocChySS1unIztwAj
# z3oqV9bBN49+yNmaGgV+AkQjAGs3W0Rtzhj2EN6YNS1yXFgs3pPum9iPBMk2QZQ1lMRSKmwzZI88
# dkeYtGy9jIAmBGgHZ5Fvnfze2n0mvcvixAH3dZo=
# train_date:2018-04-13
# back_train_date:2018-04-13
# tour_flag:dc
# purpose_codes:ADULT
# query_from_station_name:上海
# query_to_station_name:嘉兴
# undefined:


# https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs
# _json_att:
# REPEAT_SUBMIT_TOKEN:79638e3637f2cb3e3ca26ca26fc3ce29


# https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo
# cancel_flag:2
# bed_level_order_num:000000000000000000000000000000
# passengerTicketStr:3,0,1,吴镇翦,1,330304199607046312,15557555143,N
# oldPassengerStr:吴镇翦,1,330304199607046312,1_
# tour_flag:dc
# randCode:
# whatsSelect:1
# _json_att:
# REPEAT_SUBMIT_TOKEN:79638e3637f2cb3e3ca26ca26fc3ce29

# https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount
# train_date:Fri Apr 13 2018 00:00:00 GMT+0800 (中国标准时间)
# train_no:540000K52530
# stationTrainCode:K525
# seatType:3
# fromStationTelecode:SNH
# toStationTelecode:JXH
# leftTicket:MO4iv8pO%2FqJtpqfxNZ5lb7I%2BiyHCiVmU9WJPGnOj3S%2FqVz0U7Zx9H5yFMig%3D
# purpose_codes:00
# train_location:H6
# _json_att:
# REPEAT_SUBMIT_TOKEN:79638e3637f2cb3e3ca26ca26fc3ce29

# https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue
# passengerTicketStr:3,0,1,吴镇翦,1,330304199607046312,15557555143,N
# oldPassengerStr:吴镇翦,1,330304199607046312,1_
# randCode:
# purpose_codes:00
# key_check_isChange:0C56AED9DF94F656B885CAE61141C841E53E8746CF5900EF3D65D030
# leftTicketStr:MO4iv8pO%2FqJtpqfxNZ5lb7I%2BiyHCiVmU9WJPGnOj3S%2FqVz0U7Zx9H5yFMig%3D
# train_location:H6
# choose_seats:
# seatDetailType:000
# whatsSelect:1
# roomType:00
# dwAll:N
# _json_att:
# REPEAT_SUBMIT_TOKEN:79638e3637f2cb3e3ca26ca26fc3ce29

# https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random=1523607430114&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=79638e3637f2cb3e3ca26ca26fc3ce29
# random:1523607430114
# tourFlag:dc
# _json_att:
# REPEAT_SUBMIT_TOKEN:79638e3637f2cb3e3ca26ca26fc3ce29