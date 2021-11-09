#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Wei Shuai"
__copyright__ = "Copyright 2021 Wei Shuai <cpuwolf@gmail.com>"
__version__ = "1.0"
__email__ = "cpuwolf@gmail.com"
"""
Created on Nov. 9 2021
@author: Wei Shuai <cpuwolf@gmail.com>

redirect prompt command stdout,stderr to pywebview

"""

import os
import time
import shutil
import sys
import ray
import logging
import logging.handlers
import errno
import webview

window = webview.create_window('cpuwolf@gmail.com', 'pokerrandom/index.html')
webview.start()