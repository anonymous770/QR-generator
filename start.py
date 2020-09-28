import pyqrcode
import os, glob
import sys

dir_name = ('/sdcard/DCIM/QR codes')
if not os.path.exists(dir_name):
  try:
    os.mkdir('/sdcard/DCIM/QR codes')
  except FileExistsError:
    pass