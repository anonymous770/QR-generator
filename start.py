import pyqrcode
import os, glob
import sys
    
  # Creating png directory
  dir_name = ('/sdcard/DCIM/QR codes')
  if not os.path.exists(dir_name):
    try:
      os.mkdir('/sdcard/DCIM/QR codes')
    except FileExistsError:
      pass
  # Finished creating directory
