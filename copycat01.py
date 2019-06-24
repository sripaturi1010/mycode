#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode')
shutil.copy('5g_researh2/sdn_network.txt','5g_researh2/sdn.network.txt.copy')
shutil.copytree('5g_researh2','5g_researh2_backup/')
