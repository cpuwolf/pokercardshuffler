# -*- coding: utf-8 -*-
"""
Created on Nov 2018

@author: Wei Shuai <cpuwolf@gmail.com>
"""

import os
import shutil, errno
import sys
import configparser
import time
import datetime
from appdirs import *


def internal_path(relative_path):
	base_path = "."
	return os.path.join(base_path, relative_path)

def buidtimestamp():
	config = configparser.RawConfigParser()
	config.read(internal_path('WinLogInspect.cfg'))

	ts = datetime.datetime.utcnow()
	st = ts.strftime('%Y-%m-%d_%H_%M_%SUTC')
	config.set('info', 'ts', st)
	with open(internal_path('WinLogInspect.cfg'), 'w') as configfile:
		config.write(configfile)

buidtimestamp()