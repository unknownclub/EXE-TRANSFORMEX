import sys
import subprocess
from time import sleep
def getSize(fileobject):
    fileobject.seek(0,2) 
    size = fileobject.tell()
    return size
    file = open('myfile.bin', 'rb')
print '''
################################################################
#                      EXE-TRANSFORMEX                         #
# Simple Python script for convert EXE files to Array of HEX   #
# By un4ckn0wl3z | https://haxtivitiez.wordpress.com           #
################################################################
'''
if len(sys.argv) == 2:
	try:
		target_file = sys.argv[1]
		print subprocess.check_output(['powershell','-noprofile','-command','[byte[]] $hexdump = get-content -encoding byte -path "'+target_file+'"; [System.IO.File]::WriteAllLines("hex-payload.txt", ([string]$hexdump))'])
		print "Now!! Converting...."
		print "Successful converting.... | Payloaded in 'hex-payload.txt'"
		sleep(3)
		file = open("hex-payload.txt",'rb')
		print "Payload size : %d KB" % (getSize(file)/1024)
		file.close
		print "Let's check your Payload"
	except Exception as e:
		print e 
else:
	print "Usage: ./exe-transformex <.EXE file>"


