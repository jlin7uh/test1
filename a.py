import configparser


## rfid_demo1 -> rfid_demo_2 file moves the login creditential to config.ini file 20160608 NL
## This was written on python 3.5
## Added import configparser to allow reading config file
## Original credintials are listed below:
#thehost="localhost"
#theuser="admin"
#thepasswd="Moonshot1"
#thedb="rfid_demo_1"

## Create error code to check for file presense.
class eCode(Exception):
    ## Define specail error codes & messages here
    em = {1101: "Config.ini file not present. Please verify", \
          1102: "DEFAULT section missing in the config file.", \
          1103: "Host information missing in config file.", \
          1104: "Login username missing in the config file.", \
		  1105: "Password info missing in the config file.", \
		  1106: "SQL database name missing in the config file."
		  }	

config = configparser.ConfigParser()
try:
	readCheck = config.read('config.ini')
	
	if len(readCheck) == 0:
		raise eCode(1101)
	elif not('DEFAULT' in config):
		raise eCode(1102)
	elif (not ('thehost' in config['DEFAULT']) or len(config['DEFAULT']['thehost'])==0):
		raise eCode(1103)
	elif (not ('theuser' in config['DEFAULT'])or len(config['DEFAULT']['theuser'])==0):
		raise eCode(1104)
	elif (not ('thepasswd' in config['DEFAULT']) or len(config['DEFAULT']['thepasswd'])==0):
		raise eCode(1105)
	elif (not ('thedb' in config['DEFAULT'])or len(config['DEFAULT']['thedb'])==0):
		raise eCode(1106)	
		
except eCode as e:
    print(e.args[0], e.em[e.args[0]])
else:
	thehost = config['DEFAULT']['thehost']
	theuser = config['DEFAULT']['theuser']
	thepasswd = config['DEFAULT']['thepasswd']
	thedb = config['DEFAULT']['thedb']
	
	print('\nthehost: ' + thehost)
	print('\ntheuser: ' + theuser)
	print('\nthepasswd: ' + thepasswd)
	print('\nthedb: ' + thedb)
	
finally:
	pass
	
