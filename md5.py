#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Online MD5 Cracker Tool
#
#

__author__ = "Black Viking"
__date__ = "11.21.2016"
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
------------------------------
	Usage:
		-f/--file   Import MD5 hashs from a file
		-h/--hash   For a single hash
		-q/--quiet	Read a single from standard input

	Example
		$ ./md5.py -h d8578edf8458ce06fbc5bb76a58c5ca4
		$ ./md5.py -f hashs.txt
		$ echo "d8578edf8458ce06fbc5bb76a58c5ca4" | ./md5.py -q"""

	print usage
	sys.exit()

def decrypt_online(hash):
	print"\n[*] Hash: %s"%(hash)
	def site():
		br.open("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php")
		br.select_form(nr=0)
		br.form["md5"] = hash
		source = br.submit().read()
		if 'Hash "'+hash+'" not found in database' in source:
			print"[-] Hash '%s' not found in database"%(hash)
			site2()
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


def main():
	if len(sys.argv) <= 3:
		print"""[+] Coded By Black Viking
[+] Online MD5 Cracker Tool
[+] Version: V.2"""
		print "-"*30

		if sys.argv[1] == "-h" or sys.argv[1] == "--hash":
			try:
				decrypt_online(sys.argv[2])
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
					decrypt_online(i)
				except:
					pass

		elif sys.argv[1] == "-q" or sys.argv[1] == "--quiet":
			try:
				input_str = sys.stdin.read()
				decrypt_online(input_str[:-1]);		#This [:-1] is to remove the last \n in the string
			except:
				pass
		else:
			usage()
	else:
		usage()

if __name__ == "__main__":
	main()
