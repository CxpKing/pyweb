#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os	

def gitCmd(cmd):
	f = os.popen(cmd,"r")
	log = f.read()
	f.close()
	print(log)
update = ["git reset --hard && git clean -f"]
for cmd in update:
	gitCmd(cmd)
