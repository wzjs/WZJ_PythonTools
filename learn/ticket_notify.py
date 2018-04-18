import time
import requests
import json
import os
import re
import urllib.parse
HEADRS = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

}

#请求车次信息
URL_QUERYINFO = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-04-20&leftTicketDTO.from_station=HZH&leftTicketDTO.to_station=EPH&purpose_codes=ADULT"

URL_CHECKUSER = "https://kyfw.12306.cn/otn/login/checkUser"
# 请求doc,目的是获取某些字段
URL_INIT = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"

URL_GETPASSENGERDTOS = "https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"

URL_WAITTIME = "https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random=%s&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=%s"
URL_BACK = "https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue"

URL_Location = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9051"

# 验证码请求
POSITION = "1(35,39),2(98,45),3(183,44),4(253,42),5(47,119),6(95,125),7(200,125),8(265,128)"
URL_YANZHENGMA = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.5004204286123859"
URL_CHECK = "https://kyfw.12306.cn/passport/captcha/captcha-check"
FROM_DATA = {
	'answer':'',
	'login_site':'E',
	'rand':'sjrand'
}

# 登陆
URL_LOGIN = "https://kyfw.12306.cn/passport/web/login"
Login_DATA = {
	'username':'xxx',
	'password':'xxx',
	'appid':'otn'
}
# 提交下单
URL_SUBMITORDERREQUEST = "https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
SUMMIT_DATA = {
	'secretStr':'',
	'train_date':'2018-04-19',
	'back_train_date':'2018-04-19',
	'tour_flag':'dc',
	'purpose_codes':'ADULT',
	'query_from_station_name':'杭州',
	'query_to_station_name':'嘉兴南',
	'undefined':''
}
# 乘客信息
URL_CHECKORDER = "https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo"
CHECKORDER_DATA = {
	'cancel_flag':'2',
	'bed_level_order_num':'000000000000000000000000000000',
	'passengerTicketStr':'1,0,1,邱青苗,1,330723199604236429,13023231290,N',
	'oldPassengerStr':'邱青苗,1,330723199604236429,1_',
	'tour_flag':'dc',
	'randCode':'',
	'whatsSelect':'1',
	'_json_att':'',
	'REPEAT_SUBMIT_TOKEN':''
}
# 检查订单信息
URL_GETQUEUE = "https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount"
ORDER_DATA = {
	'train_date':'Mon Apr 16 2018 00:00:00 GMT+0800 (中国标准时间)',
	'train_no':'56000K8372C0',
	'stationTrainCode':'K8372',
	'seatType':'1',
	'fromStationTelecode':'HZH',
	'toStationTelecode':'JXH',
	'leftTicket':'',
	'purpose_codes':'00',
	'train_location':'H6',
	'_json_att':'',
	'REPEAT_SUBMIT_TOKEN':''
}

#
URL_CONFIRM = "https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue"
COMFIM_DATA = {
	'passengerTicketStr':'1,0,1,邱青苗,1,330723199604236429,13023231290,N',
	'oldPassengerStr':'邱青苗,1,330723199604236429,1_',
	'randCode':'',
	'purpose_codes':'00',
	'key_check_isChange':'',
	'leftTicketStr':'',
	'train_location':'G1',
	'choose_seats':'',
	'seatDetailType':'000',
	'whatsSelect':'1',
	'roomType':'00',
	'dwAll':'N',
	'_json_att':'',
	'REPEAT_SUBMIT_TOKEN':'',
}

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'kyfw.12306.cn',
'Origin':'https://kyfw.12306.cn',
'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
class Ticketer12306(object):
	"""docstring for Loginer"""
	location_info = ""
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
		jsn = json.loads(rsp.text)
		if jsn["result_code"] == '4':
			return True
		else:
			return False

	def Login(self):
		rsp  = self.session.post(URL_LOGIN,data=Login_DATA)
		js = json.loads(rsp.text)
		if js["result_code"] == 0:
			print("登录成功")
			rsp = self.session.post("https://kyfw.12306.cn/passport/web/auth/uamtk",data={'appid':'otn'},headers=headers)
			dic = json.loads(rsp.text)
			rsp = self.session.post("https://kyfw.12306.cn/otn/uamauthclient",data={'tk':dic['newapptk']},headers=headers)
			self.HandleTicketInfo()
			self.GetTicket()
		else:
			print("登录失败")

	def HandleTicketInfo(self):
		rsp = self.session.get(URL_QUERYINFO)
		dic = json.loads(rsp.text)
		info = dic['data']['result'][5]
		print("info:" + info)
		self.arr = info.split('|')
		source = self.arr[6]

		source_ = re.findall("\|([\u4e00-\u9fa5]*)\|%s"%source,Ticketer12306.location_info)[0]
		destination = self.arr[7]
		destination_ = re.findall("\|([\u4e00-\u9fa5]*)\|%s"%destination,Ticketer12306.location_info)[0]
		train_date = self.arr[13]
		train_date1 = "%s-%s-%s"%(train_date[0:4],train_date[4:6],train_date[6:8])
		train_no = self.arr[2]
		stationTrainCode = self.arr[3]
		secretStr = urllib.parse.unquote(self.arr[0]) 
		train_location = self.arr[15]
		
		print(secretStr)
		# print(train_date)
		SUMMIT_DATA.update({'secretStr':secretStr,
							'train_date':train_date1,
							'back_train_date':train_date1,
							'tour_flag':'dc',
							'purpose_codes':'ADULT',
							'query_from_station_name':source_,
							'query_to_station_name':destination_,
							})
		ORDER_DATA.update({
			'train_date':'Mon Apr %s 2018 00:00:00 GMT+0800 (中国标准时间)'%train_date[-2:],
			'train_no':train_no,
			'stationTrainCode':stationTrainCode,
			'fromStationTelecode':source,
			'toStationTelecode':destination,
			'train_location':train_location
			}) 
		ORDER_DATA.update({
			'train_location':train_location
		}
		)

	def FindLocationInfo():
		rsp = requests.get(URL_Location)
		Ticketer12306.location_info = rsp.text
		# print(location_info)

	def GetTicket(self):
		# csr = self.session.post(URL_CHECKUSER,{'_json_att':''})

		print(SUMMIT_DATA)

		smt = self.session.post(URL_SUBMITORDERREQUEST,SUMMIT_DATA)
		print(smt.text)
		# print("summit rsp:"+smt.text)
		idt = self.session.post(URL_INIT,{'_json_att':''})
		# print("idt:"+idt.text)
		# 正则拿到token
		# print(idt.text)
		result = re.findall("globalRepeatSubmitToken = '(\w*)'",idt.text)[0]
		key = re.findall("key_check_isChange':'(\w*)'",idt.text)[0]
		gpd = self.session.post(URL_GETPASSENGERDTOS,{'_json_att':'',
								'REPEAT_SUBMIT_TOKEN':result})
		print("gpd:"+gpd.text)
		CHECKORDER_DATA.update({'REPEAT_SUBMIT_TOKEN':result})
		cko = self.session.post(URL_CHECKORDER,CHECKORDER_DATA)
		print("cko:"+cko.text)
		ORDER_DATA.update({'REPEAT_SUBMIT_TOKEN':result,'leftTicket':urllib.parse.unquote(self.arr[12])})
		getq = self.session.post(URL_GETQUEUE,ORDER_DATA)
		print('getQueueCount:'+getq.text)
		COMFIM_DATA.update({'REPEAT_SUBMIT_TOKEN':result,'leftTicketStr':urllib.parse.unquote(self.arr[12]),'key_check_isChange':key,''})
		print(COMFIM_DATA)
		print("------"+urllib.parse.unquote(self.arr[12]))
		cnfm = self.session.post(URL_CONFIRM,COMFIM_DATA)
		print('cnfm:'+cnfm.text)
		self.session.get(URL_WAITTIME%(time.time()* 1000,result))
		wait = self.session.get(URL_WAITTIME%(time.time()* 1000,result))
		print(wait.text)
		odr = json.loads(wait.text)
		order = odr['data']['orderId']
		rsul = self.session.post(URL_BACK,{'orderSequence_no':order,
									'_json_att':'',
									'REPEAT_SUBMIT_TOKEN':result})
		print(rsul.text)

if __name__ == '__main__':
	print(POSITION)
	loginer = Ticketer12306()
	Ticketer12306.FindLocationInfo()
	while  True:
		if loginer.Checkcaptcha():
			loginer.Login()
			break;
	

#https://kyfw.12306.cn/otn/login/checkUser
# _json_att:

# checkG1234('sxQkSz%2BAUt9WIQk4%2FRF%2BK5U5CfR08H8MV8cgFrxL6cvOEMkvVCgThJxpbY5MmgbvPYcE%2FqFw5znN%0ABGKXH04lxhBR1Cp9ae%2FGXo5aBY2%2FbgZKU9IC4OxEJ55kZZ41Q3y0MAztmxAg2YIWd0POfj5CGfqQ%0An71021e0aUXZzAReb%2Bfee%2BEpYQzsJe7rumwQBwOJ%2BTG3JKuVOrH3Rwyqd2GuhtEebUHvbL7ZUyAp%0Afy0m7nlk3fsMJFjNhbvnQvublx9OIBkpHFX92V0%3D','19:15','540000K527A5','SNH','JXH')

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