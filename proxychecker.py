import urllib2, socket, getproxylist, json


socket.setdefaulttimeout(180)

nUsuarios = input("Cuantos usuario deseas crear? ")

  

def is_bad_proxy(pip):    
    try:        
        
        proxy_handler = urllib2.ProxyHandler({'http': pip})        
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)        
        req=urllib2.Request('http://www.gnu.org')  # The url can be refused after a time
        sock=urllib2.urlopen(req)

    except urllib2.HTTPError, e:        
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:

        print "ERROR:", detail
        return 1
    return 0


#my program
#for item in proxyList:
i = 0
while(i<nUsuarios):
    getproxylist.getProxyList(nUsuarios*5)#Obteniendo la lista de proxys
    ip = getproxylist.getIp()#Sacando la ip 
    port = getproxylist.getPort()#El puerto

    proxyip= ip+":"+port #ip and port to evaluate

    print("El proxy a evaluar: "+proxyip)

    if is_bad_proxy(proxyip):
        print "Bad Proxy", proxyip
    else:
        print proxyip, "is working"
        i+=1

