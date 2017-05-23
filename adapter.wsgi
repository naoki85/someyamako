# -*- coding:utf-8 -*-
import sys, os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
sys.path.append(dirpath + '/classes')
sys.path.append(dirpath + '/config')
sys.path.append('/usr/lib64/python3.6/site-packages')
os.chdir(dirpath)
import bottle
import someyamako
application = bottle.default_app()