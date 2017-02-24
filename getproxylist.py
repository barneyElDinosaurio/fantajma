
import requests
import json
from urllib import urlopen

ip = ""
port = ""
clean1 = ""
primera = False
paso = 1


def getProxyList(nProxys):

	global ip, port, clean1, primera,paso
	#url = json.loads(url)
	
	if(primera==True):#Si ya paso la primera vez
		ip = clean1[3+42*paso]
		port = clean1[7+42*paso]	
	else:
		url = urlopen('http://proxy.tekbreak.com/'+str(nProxys)).read()
		clean1 = url.split('"')
		print(clean1)
		
		ip = clean1[3]
		port = clean1[7]

	primera = True
	paso+=1
	print (ip+":"+port)

def getIp():
	global ip, port, clean1, primera
	#if(primera==True):
	#	ip = clean1[3+7]	
	return ip

def getPort() :
	global ip, port, clean1 , primera
	#if(primera==True):
	#	ip = clean1[7+7]	
	return port

