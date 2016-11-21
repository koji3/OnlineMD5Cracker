#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Online MD5 Crack Tool
#
#

__author__ = "Black Viking"
__date__ = "11.21.2016"
__version__ = "v.1"

import mechanize
import sys
import os
import re
import time

br = mechanize.Browser()
br.set_handle_robots(False)

site = "http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"

def usage():
	usage = """[+] Coded By Black Viking
[+] Online MD5 Crack Tool
[+] Version: V.1

Usage:
	python md5.py -h/--hash <hash>

Example:
	python md5.py --hash d8578edf8458ce06fbc5bb76a58c5ca4"""

	print usage
	sys.exit()

def md5(hash):
	print"""[+] Coded By Black Viking
[+] Online MD5 Crack Tool
[+] Version: V.1"""
	print "-"*30
	print"\n[*] Hash: %s"%(hash)
	br.open(site)
	br.select_form(nr=0)
	br.form["md5"] = hash
	source = br.submit().read()
	if 'Hash "'+hash+'" not found in database' in source:
		print"[-] Hash '%s' not found in database"%(hash)
		sys.exit()
	elif 'String "'+hash+'" is not MD5 hash' in source:
		print"[!] String '%s' is not MD5 hash"%(hash)
		sys.exit()
	elif 'Result:' in source:
		print "[+] Hashed string: %s"%(re.findall("""<span class='middle_title'>Hashed string</span>: (.*?)</div>""", source)[0])
		sys.exit()
	else:
		pass


def main():
	if len(sys.argv) == 3:
		if sys.argv[1] == "-h" or sys.argv[1] == "--hash":
			md5(sys.argv[2])
		else:
			usage()
	else
		usage()

if __name__ == "__main__":
	main()