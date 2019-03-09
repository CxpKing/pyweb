#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os	

def gitCmd(cmd):
	f = os.popen(cmd,"r")
	log = f.read()
	f.close()
	print(log)
update = ["git clean -f",
		  "git checkout master",
		  "git reset --hard",
		  "git fetch --all",
		  "git reset --hard origin/master",
		  "git pull"]
for cmd in update:
	gitCmd(cmd)
