#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os	

def gitCmd(cmd):
	f = os.popen(cmd,"r")
	log = f.read()
	f.close()
	print(log)
push = ["git add -A",
		  "git commit -m",
		  "git push origin master",
		]
for cmd in push:
	gitCmd(cmd)
