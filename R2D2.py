from termcolor import colored
from datetime import datetime
import json

def log(para,color=0):
	
	print datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
	if(color == 0):
		print para
	elif(color == 1):
		print colored(para, 'green')
	else:
		print colored(para, 'red')
	return

def custom_print(para,color=0):
	if(color == 0):
		print para
	elif(color == 1):
		print colored(para, 'green')
	else:
		print colored(para, 'red')
	return

def pretty_print(str):
	print json.dumps(str, indent=4, sort_keys=True)

def pretty(str):
	return json.dumps(str, indent=4, sort_keys=True)
