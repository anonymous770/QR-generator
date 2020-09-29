# Author :- AslamMiya
# github id :- https://github.com/anonymous770
# Package link :- https://github.com/anonymous770/QR-generator

import pyqrcode
import os, sys
import subprocess as sub

# Create folder

dir_name = ('/sdcard/DCIM/QR codes')
if not os.path.exists(dir_name):
  try:
    os.mkdir('/sdcard/DCIM/QR codes')
  except FileExistsError:
    pass
    
# Folder creating finished
# Get input

sub.call('clear')
try:
	text = input("\033[1;37mEnter a text :-\n\n\033[0m")
	if text=="":
		print('\033[0;33mInvalid input. Text is blank.\033[0m')
		sys.exit()
except KeyboardInterrupt:
	print('\n\033[1;31mProcess cancled by user.\n\033[0m')
	sys.exit()

# Geting input finished
# Get text in code

while True:
	try:
		file_name = input('\n\033[1;37mEnter a file name :-\033[0m ')
		if file_name=="" :
		  			print("\033[0;33mInvalid input. File name cannot be blank.\n\033[0m ")
		else:
		  			pass
		  			break
	except KeyboardInterrupt:
			print('\n\033[1;31mProcess cancled by user.\033[0m\n')
			sys.exit()
try:
	store_location = (f'/sdcard/DCIM/QR codes/{file_name}.png')
	code = pyqrcode.create(text)
	code.png(store_location, scale=4)
except Exception:
	print("\n\033[1;31mIt's to long.\033[0m")