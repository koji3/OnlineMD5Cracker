#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Online MD5 Crack Tool
#
#

__author__ = "Black Viking"
__date__ = "11.26.2016"
__version__ = "v.2"

import mechanize
import sys
import os
import re
import time

br = mechanize.Browser()
br.set_handle_robots(False)


def usage():
	usage = """[+] Coded By Black Viking
[+] Online MD5 Cracker Tool
[+] Version: V.2

	Usage:
	    -f/--file   Import MD5 hashs from a file
	    -h/--hashs	For a single hash

	Example
		$ ./md5.py -h d8578edf8458ce06fbc5bb76a58c5ca4
		$ ./md5.py -f hashs.txt"""

	print usage
	sys.exit()

def from_opt(hash):
	print"\n[*] Hash: %s"%(hash)
	def site():
		br.open("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php")
		br.select_form(nr=0)
		br.form["md5"] = hash
		source = br.submit().read()
		if 'Hash "'+hash+'" not found in database' in source:
			print"[-] Hash '%s' not found in database"%(hash)
			pass
		elif 'String "'+hash+'" is not MD5 hash' in source:
			print"[!] String '%s' is not MD5 hash"%(hash)
			sys.exit()
		elif 'Result:' in source:
			print "[+] Hashed string: %s"%(re.findall("""<span class='middle_title'>Hashed string</span>: (.*?)</div>""", source)[0])
			sys.exit()
		else:
			pass
	def site2():
		br.open("http://md5decryption.com/")
		br.select_form(nr=0)
		br.form["hash"] = hash
		source1 = br.submit("submit").read()
		if "Decrypted Text:" in source1:
			print "[+] Hashed string: %s"%(re.findall('Decrypted Text: </b>(.*?))</font>', source1)[0])
			sys.exit()
		else:
			print"[-] Hash '%s' not found in database"%(hash)
			sys.exit()

	site()
	site2()

def from_file(hash):
	def site():
		print"\n[*] Hash: %s"%(hash)
		br.open("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php")
		br.select_form(nr=0)
		br.form["md5"] = hash
		source = br.submit().read()
		if 'Hash "'+hash+'" not found in database' in source:
			print"[-] Hash '%s' not found in database"%(hash)
			pass
		elif 'String "'+hash+'" is not MD5 hash' in source:
			print"[!] String '%s' is not MD5 hash"%(hash)
			pass
		elif 'Result:' in source:
			print "[+] Hashed string: %s"%(re.findall("""<span class='middle_title'>Hashed string</span>: (.*?)</div>""", source)[0])
			pass
		else:
			pass
	def site2():
		br.open("http://md5decryption.com/")
		br.select_form(nr=0)
		br.form["hash"] = hash
		source1 = br.submit("submit").read()
		if "Decrypted Text:" in source1:
			print "[+] Hashed string: %s"%(re.findall('Decrypted Text: </b>(.*?))</font>', source1)[0])
			pass
		else:
			print"[-] Hash '%s' not found in database"%(hash)
			pass

	site()
	site2()




def main():
	print"""[+] Coded By Black Viking
[+] Online MD5 Crack Tool
[+] Version: V.1"""
	print "-"*30
	if len(sys.argv) == 3:
		if sys.argv[1] == "-h" or sys.argv[1] == "--hash":
			try:
				from_opt(sys.argv[2])
			except:
				pass

		elif sys.argv[1] == "-f" or sys.argv[1] == "--file":
			try:
				md5ler = open(sys.argv[2], "r").read().split("\n")
			except IOError:
				print "\nI/O Error"
				time.sleep(2)
				sys.exit()

			for i in md5ler:
				try:
					from_file(i)
				except:
					pass

		else:
			usage()
	else:
		usage()

if __name__ == "__main__":
	main()
