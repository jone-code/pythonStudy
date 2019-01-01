# -*- coding:utf-8 -*-
# Author:Jone
import os
import sys
BASH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASH_PATH)

from core import main
main.first()