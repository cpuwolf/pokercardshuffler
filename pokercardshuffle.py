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
import sys
import webview

def resource_path(relative_path):  # needed for bundling
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

window = webview.create_window('cpuwolf@gmail.com', resource_path('index.html'), fullscreen=True)
webview.start()