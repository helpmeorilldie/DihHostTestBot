import os
import sys
import time
import json
import random 
import requests
import threading 
from flask import Flask, send_from_directory
from threading import Thread
try:from colorama import Fore,Style,init;init()
except:os.system('pip install colorama');from colorama import Fore,Style,init



app = Flask(__name__)
@app.route("/")
def home():
    return send_from_directory(
        os.path.dirname(os.path.abspath(__file__)),
        "index.html"
    )

@app.route("/health")
def health():
    return "OK", 200

def run():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    server = Thread(target=run, daemon=True)
    server.start()
keep_alive()
import os


BOT_TOKEN= "8554922121:AAEjcD9bvFk-0k_S30gApSAxQqTcc4w6Drg"
API_URL=f"https://api.telegram.org/bot{BOT_TOKEN}"

_l='Cʜᴀɴɴᴇʟ🪭'
_k='mode_bulk'
_j='mode_single'
_i='reply_markup'
_h='parse_mode'
_g='chat_id'
_f='result'
_e='application/x-www-form-urlencoded'
_d='Origin'
_c='Content-Type'
_b='https://hi2.in/'
_a='en-US,en;q=0.5'
_Z='application/json, text/plain, */*'
_Y='Accept-Language'
_X='Accept'
_W='hi2.in'
_V='\x1b[38;5;195m'
_U='\x1b[38;5;159m'
_T='\x1b[38;5;117m'
_S='\x1b[38;5;213m'
_R='\x1b[38;5;183m'
_Q='\x1b[1m'
_P='\x1b[0m'
_O='back_menu'
_N='https://t.me/linksfromerebus'
_M='url'
_L='message_id'
_K='Referer'
_J='callback_data'
_I=True
_H='inline_keyboard'
_G='not_taken'
_F='User-Agent'
_E='taken'
_D='@'
_C='id'
_B='text'
_A=None

reset=_P
bold=_Q
spy1=_R
spy2=_S
spy3=_T
spy4='\x1b[38;5;157m'
spy5='\x1b[38;5;219m'
spy6='\x1b[38;5;147m'
spy7=_U
spy8='\x1b[38;5;225m'
spy9=_V
spy10='\x1b[38;5;121m'
spy11='\x1b[38;5;216m'
spy12='\x1b[38;5;222m'
spy13='\x1b[38;5;189m'
spy14='\x1b[38;5;211m'
spy15='\x1b[38;5;151m'
spy16='\x1b[38;5;223m'
spy17='\x1b[38;5;200m'
spy18=_V
spy19='\x1b[38;5;230m'
spy20=_S
spy21='\x1b[38;5;105m'
spy22=_T
spy23='\x1b[38;5;228m'
spy24='\x1b[38;5;170m'
spy25='\x1b[38;5;114m'
spy26='\x1b[38;5;224m'
spy27=_R
spy28='\x1b[38;5;208m'
spy29=_U
spy30='\x1b[38;5;220m'
reset=_P
bold=_Q
SUPPORTED_DOMAINS=[_W,'telegmail.com']
RECAPTCHA_SITEKEY='6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct'
RECAPTCHA_CO='aHR0cHM6Ly9oaTIuaW46NDQz'
RECAPTCHA_V='XrIDux0s7SoNe6_IHkjGC92W'
USER_AGENTS=['Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0','Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36']
DEFAULT_COOKIES={'__eoi':'ID=84791c9b377760ae:T=1785815548:RT=1792303549:S=AA-AfjbAwxHu8AEDm58GilHT3t8P','__gads':'ID=d35d042016429679:T=1785815548:RT=1792303548:S=ALNI_MZSbvQNM9tUxE_CmZnXbUQWGG3kdQ','__gpi':'UID=0000145fbef21f84:T=1785815548:RT=1792303549:S=ALNI_MY_LJgZNcPDvOPq2U5kNuOWvCQotQ','_ga':'GA1.1.1815008449.1785815546','_ga_02VF9D5F26':'GS2.1.s1792303540$o18$g0$t1792303540$j60$l0$h0','FCCDCF':'[null,null,null,null,null,null,[[32,"[\\"42eb93fe-68c7-4034-96db-c13bb605dd03\\",[1785815556,751000000]]"]]]','FCNEC':'[["AKsRol8RF5LPgmRao6cebT6eoNufsXC40Wwgytn794ql_B5zzX--7wmkvDU6Esk0nXehFzYvJZ2jRdoE9CPO20HK1fSnQ8aIrv0vxQGTzJXI38I3eBti2LaIXRtHZiYACNxOjS3mWLkn0GetUYHYnWDfEOvrLJkhyQ=="]]'}
def build_session(seed_cookies=_I):
	A=requests.Session();A.headers.update({_F:random.choice(USER_AGENTS),_X:_Z,_Y:_a,'Accept-Encoding':'gzip, deflate, br','Connection':'keep-alive','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','TE':'trailers'})
	if seed_cookies:
		for(B,C)in DEFAULT_COOKIES.items():A.cookies.set(B,C,domain=_W)
	return A
def solve_recaptcha_hi2(session):
	F='resp","';E='recaptcha-token" value="';A=session
	try:
		B=f"https://www.google.com/recaptcha/api2/anchor?ar=1&k={RECAPTCHA_SITEKEY}&co={RECAPTCHA_CO}&hl=en&v={RECAPTCHA_V}&size=invisible";C=A.get(B,timeout=12,headers={_F:random.choice(USER_AGENTS),_K:_b})
		if E not in C.text:return
		G=C.text.split(E)[1].split('"')[0];H=f"v={RECAPTCHA_V}&reason=q&c={G}&k={RECAPTCHA_SITEKEY}&co={RECAPTCHA_CO}&hl=en&size=invisible";I={_F:random.choice(USER_AGENTS),_K:B,_c:_e,_d:'https://www.google.com'};D=A.post('https://www.google.com/recaptcha/enterprise/reload',data=H,headers=I,timeout=12)
		if F not in D.text:return
		return D.text.split(F)[1].split('"')[0]
	except Exception:return
def check_hi2_email(email):
	J='available';I='already taken';F=email;E='unknown'
	if _D not in F:return E
	K,C=F.split(_D,1);C=C.lower();D=build_session();G=solve_recaptcha_hi2(D)
	if not G:return E
	L={_F:D.headers[_F],_X:_Z,_Y:_a,_c:_e,'Authorization':'Basic bnVsbA==',_d:'https://hi2.in',_K:_b};M={'domain':C,'prefix':K,'recaptcha':G}
	try:
		H=D.post('https://hi2.in/api/custom',headers=L,data=M,timeout=15);B=H.text.lower()
		if I in B or _E in B and'"error"'not in B:
			try:
				A=H.json()
				if isinstance(A,dict):
					if A.get('error')and _E in str(A).lower():return _E
					if A.get(J)is False:return _E
					if A.get(J)is _I:return _G
			except Exception:0
			if I in B:return _E
			return _G
		return _G
	except Exception:return E
SPINNER = ['◜', '◠', '◝', '◞', '◡', '◟']
def animate_check(chat_id,email,stop_event,frames_per_sec=0.5):
	C=stop_event;B=chat_id;A={_C:_A}
	def E():
		D=0
		while not C.is_set():
			F=SPINNER[D%len(SPINNER)];E=f"◌ 𝑪𝒉𝒆𝒄𝒌𝒊𝒏𝒈❕‣ <code>{email}</code> {F}"
			if A[_C]is _A:G=send_message(B,E);A[_C]=G
			else:edit_message(B,A[_C],E)
			D+=1;time.sleep(1/frames_per_sec)
	D=threading.Thread(target=E,daemon=_I);D.start()
	def F(result_text):
		E=result_text;C.set();D.join(timeout=2)
		if A[_C]is _A:send_message(B,E)
		else:edit_message(B,A[_C],E)
	return F
def get_updates(offset=_A):
	try:A=requests.get(f"{API_URL}/getUpdates",params={'timeout':30,'offset':offset},timeout=35);return A.json().get(_f,[])
	except Exception:return[]
def send_message(chat_id,text,parse_mode='HTML',reply_markup=_A):
	A=reply_markup;B={_g:chat_id,_B:text,_h:parse_mode}
	if A:B[_i]=json.dumps(A)
	try:C=requests.post(f"{API_URL}/sendMessage",data=B,timeout=10).json();return C.get(_f,{}).get(_L)
	except Exception:return
def edit_message(chat_id,message_id,text,parse_mode='HTML',reply_markup=_A):
	A=reply_markup;B={_g:chat_id,_L:message_id,_B:text,_h:parse_mode}
	if A:B[_i]=json.dumps(A)
	try:requests.post(f"{API_URL}/editMessageText",data=B,timeout=10)
	except Exception:0
def answer_callback(callback_query_id,text=_A,show_alert=False):
	A={'callback_query_id':callback_query_id}
	if text:A[_B]=text;A['show_alert']=show_alert
	try:requests.post(f"{API_URL}/answerCallbackQuery",data=A,timeout=10)
	except Exception:0
def send_welcome(chat_id):
    text = (
		"𝑬𝒓𝒆𝒃𝒖𝒔°\n"
        "&#160;&#160;&#160;╭───────────╮\n"
        "&#160;&#160;&#160;│🎫  Hɪ2 Mᴀɪʟ Cʜᴇᴄᴋᴇʀ \n"
        "&#160;&#160;&#160;╰───────────╯\n\n"
        "&#160;&#160;<b>Wᴇʟᴄᴏᴍᴇ💐 Tᴏ 𝑬𝒓𝒆𝒃𝒖𝒔\n" 
		"&#160;&#160;Fᴀᴋᴇ Mᴀɪʟ Cʜᴇᴄᴋᴇʀ Bᴏᴛ👾</b>\n\n"
        "╭───<b>Mᴀɪʟ Cʜᴇᴄᴋ Mᴏᴅᴇs</b>───╮\n"
        "&#160;&#160;╭─ 1 · Sɪɴɢʟᴇ Cʜᴇᴄᴋ\n"
        "&#160;&#160;╰➤ Check one email address\n"
        "&#160;&#160;╭─ 2 · Bᴜʟᴋ Cʜᴇᴄᴋ\n"
        "&#160;&#160;╰➤ Process multiple addresses\n"
        "╰───────────────╯\n"
        "Bʏ ‣ 𝑯𝒂𝒛𝒆 @Noxmirage  \n"
    )

    keyboard = {
        _H: [
            [
                {
                    _B: "◈ Sɪɴɢʟᴇ Mᴏᴅᴇ",
                    _J: _j
                },
                {
                    _B: "▤ Bᴜʟᴋ Mᴏᴅᴇ",
                    _J: _k
                }
            ],
            [
                {
                    _B: "Jᴏɪɴ Cʜᴀɴɴᴇʟ🪭",
                    _M: _N
                }
            ]
        ]
    }

    send_message(chat_id, text, reply_markup=keyboard)
def send_single_prompt(chat_id, message_id=_A):

    text = (
        "&#160;&#160;&#160;&#160;╭──────╮\n"
        "&#160;&#160;&#160;&#160;│Sɪɴɢʟᴇ Mᴏᴅᴇ\n"
        "&#160;&#160;&#160;&#160;╰──────╯\n\n"
        "╭───<b>Iɴᴘᴜᴛ Dᴇᴛᴀɪʟs</b>───╮\n"
		"&#160;&#160;&#160;Sᴇɴᴅ A Uꜱᴇʀɴᴀᴍᴇ\n"
		"&#160;&#160;&#160;Oʀ Eᴍᴀɪʟ Aᴅᴅʀᴇꜱꜱ\n"
		"&#160;⌁ <b>Exᴀᴍᴘʟᴇ</b>\n"
		"&#160;&#160;╭─ · <code>john</code>\n"
		"&#160;&#160;╰➤· <code>john@hi2.in</code>\n"
		"╰─────────────╯\n"
        "◈ Yᴏᴜʀ Rᴇǫᴜᴇꜱᴛ Wɪʟʟ Bᴇ Pʀᴏᴄᴇꜱꜱᴇᴅ\n"
		"&#160; Aꜰᴛᴇʀ Yᴏᴜ Sᴜʙᴍɪᴛ Yᴏᴜʀ Iɴᴘᴜᴛ.\n\n"
	    "Bʏ ‣ 𝑯𝒂𝒛𝒆 @Noxmirage")

    keyboard = {
        _H: [
            [
                {
                    _B: "₰ Bᴀᴄᴋ Tᴏ Mᴇɴᴜ",
                    _J: _O
                }
            ]
        ]
    }

    if message_id:
        edit_message(
            chat_id,
            message_id,
            text,
            reply_markup=keyboard
        )
    else:
        send_message(
            chat_id,
            text,
            reply_markup=keyboard
        )
def send_bulk_prompt(chat_id,message_id=_A):
	B=message_id;A=chat_id;C="&#160;&#160;&#160;&#160;&#160;&#160;╭──────╮\n&#160;&#160;&#160;&#160;&#160;&#160;│Bᴜʟᴋ Mᴏᴅᴇ\n&#160;&#160;&#160;&#160;&#160;&#160;╰──────╯\n\n╭───<b>Iɴᴘᴜᴛ Dᴇᴛᴀɪʟs</b>───╮\n&#160;&#160;&#160;Sᴇɴᴅ Eᴍᴀɪʟs Sᴇᴘᴀʀᴀᴛᴇᴅ Bʏ\n&#160;&#160;&#160;Sᴘᴀᴄᴇs\n&#160;⌁ <b>Exᴀᴍᴘʟᴇ</b>\n&#160;&#160;╭─ · <code>john@hi2.in</code>\n&#160;&#160;╰➤· <code>jane@hi2.in</code> <code>Haze@hi2.in</code>\n╰─────────────╯\n◈ Yᴏᴜʀ Rᴇǫᴜᴇꜱᴛ Wɪʟʟ Bᴇ Pʀᴏᴄᴇꜱꜱᴇᴅ\n&#160;Aꜰᴛᴇʀ Yᴏᴜ Sᴜʙᴍɪᴛ Yᴏᴜʀ Iɴᴘᴜᴛ.\n&#160;⌁ <i>Uꜱᴇ /start Tᴏ Rᴇᴛᴜʀɴ Tᴏ Mᴀɪɴ Mᴇɴᴜ.</i>\n\nBʏ ‣ 𝑯𝒂𝒛𝒆 @Noxmirage";D={_H:[[{_B:'‹ Bᴀᴄᴋ Tᴏ Mᴇɴᴜ',_J:_O}]]}
	if B:edit_message(A,B,C,reply_markup=D)
	else:send_message(A,C,reply_markup=D)
def process_single(chat_id,raw_input):
	D=chat_id;A=raw_input.strip().lower()
	if not A:return
	if _D in A:
		H,E=A.split(_D,1)
		if E not in SUPPORTED_DOMAINS:send_message(D,f"❌ <b>Iɴᴠᴀʟɪᴅ Dᴏᴍᴀɪɴ</b>\n\n<b>Pʟᴇᴀsᴇ Uꜱᴇ Oɴᴇ Oꜰ Tʜᴇ Sᴜᴘᴘᴏʀᴛᴇᴅ Dᴏᴍᴀɪɴs</b>\n<code>{", ".join(_D+A for A in SUPPORTED_DOMAINS)}</code>");return
		B=f"{H}@{E}"
	else:B=f"{A}@hi2.in"
	F=threading.Event();I=animate_check(D,B,F);G=check_hi2_email(B);F.set()
	if G==_E:C='❌ <b>Tᴀᴋᴇɴ</b>'
	elif G==_G:C='✅ <b>Nᴏᴛ Tᴀᴋᴇɴ</b>'
	else:C='💭 <b>Uɴᴋɴᴏᴡɴ</b>'
	J=f"""📊 <b>Aᴠᴀɪʟᴀʙɪʟɪᴛʏ Rᴇᴘᴏʀᴛ</b> 💐

📧 <b>Eᴍᴀɪʟ:</b> <code>{B}</code>
🎃 <b>Sᴛᴀᴛᴜs:</b> {C}
 
""";K={_H:[[{_B:_l,_M:_N}]]};I(J)
def process_bulk(chat_id,text):
	C=chat_id;M=text.replace(',',' ').split();H,B,D=set(),[],[]
	for A in M:
		A=A.strip().lower()
		if not A or A in H:continue
		H.add(A)
		if _D in A:
			R,N=A.split(_D,1)
			if N in SUPPORTED_DOMAINS:B.append(A)
			else:D.append(f"{A} (bad domain)")
		else:B.append(f"{A}@hi2.in")
	if not B:send_message(C,'❌ <b>Nᴏ Vᴀʟɪᴅ Mᴀɪʟ Fᴏᴜɴᴅ</b>\n\n💡 <b>Exᴀᴍᴘʟᴇ:</b>\n<code>user@hi2.in user2</code>');return
	send_message(C,f"🔎 <b>Bᴜʟᴋ Cʜᴇᴄᴋ Sᴛᴀʀᴛᴇᴅ</b> — {len(B)} emails\n\n⏳ <b>Pʟᴇᴀsᴇ Wᴀɪᴛ..🤏🏻</b>");I=[]
	for(O,E)in enumerate(B,1):
		J=threading.Event();P=animate_check(C,E,J);K=check_hi2_email(E);J.set()
		if K==_E:F,G='❌','Tᴀᴋᴇɴ'
		elif K==_G:F,G='🍀','Fʀᴇᴇ'
		else:F,G='❔','Uɴᴋɴᴏᴡɴ'
		L=f"{O}. {F} <code>{E}</code> → <b>{G}</b>";I.append(L);P(L);time.sleep(1.)
	Q='📊 <b>Aᴠᴀɪʟᴀʙɪʟɪᴛʏ Rᴇᴘᴏʀᴛ</b> 💐\n\n'+'\n'.join(I)+f"\n\n✅ <b>Tᴏᴛᴀʟ Cʜᴇᴄᴋᴇᴅ ‣</b> {len(B)}\n📢 <b>Cʜᴀɴɴᴇʟ ‣</b> @ErebusRedirect";send_message(C,Q,reply_markup={_H:[[{_B:_l,_M:_N}]]})
	if D:send_message(C,'⚠️ <b>Invalid Skipped</b>\n\n'+'\n'.join(f"• {A}"for A in D))
def run_bot():
	P='bulk';O='single';N='chat';M='callback_query';F='message';G=0;C={}
	while _I:
		try:
			Q=get_updates(offset=G+1)
			for D in Q:
				H=D.get('update_id')
				if H and H>=G:G=H
				if M in D:
					E=D[M];A=E[F][N][_C];J=E[F][_L];I=E.get('data','');answer_callback(E[_C])
					if I==_j:C[A]=O;send_single_prompt(A,J)
					elif I==_k:C[A]=P;send_bulk_prompt(A,J)
					elif I==_O:C.pop(A,_A);send_welcome(A)
				elif F in D:
					K=D[F];A=K[N][_C];B=(K.get(_B)or'').strip()
					if B=='/start'or B=='/help':C.pop(A,_A);send_welcome(A);continue
					if not B or B.startswith('/'):continue
					L=C.get(A)
					if L==O:process_single(A,B)
					elif L==P:process_bulk(A,B)
					else:send_welcome(A)
			time.sleep(0.1)
		except KeyboardInterrupt:print(f"\n{spy28}[!] shutdown{reset}");break
		except Exception as R:print(f"{spy28}[!] error: {R}{reset}");time.sleep(4)
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

print(f"""
{spy1}{bold}
    ╭─────────────────────────────╮
    │                             │
    │      Hɪ2 Mᴀɪʟ Cʜᴇᴄᴋᴇʀ       │
    │                             │
    ╰─────────────────────────────╯

    ⌁ Sᴛᴀᴛᴜs     : {spy4}Rᴜɴɴɪɴɢ{spy1}
    ⌁ Cʜᴀɴɴᴇʟ    : {spy2}@Noxmirage{spy1}
    ⌁ Iɴᴛᴇʀꜰᴀᴄᴇ  : Tᴇʟᴇɢʀᴀᴍ Bᴏᴛ

    ╭──────────────────────────────╮
      ◈ Sʏꜱᴛᴇᴍ Iɴɪᴛɪᴀʟɪᴢᴇᴅ
      ◈ Wᴀɪᴛɪɴɢ Fᴏʀ Iɴᴄᴏᴍɪɴɢ Uᴘᴅᴀᴛᴇs
    ╰──────────────────────────────╯
{reset}""")


# ═══════════════════════════════════════════════════════════════════════════
#  EREBUS UI + ACCOUNTS LAYER  (same UI kit as botV6.py)
#  The checking engine (solve_recaptcha_hi2 / check_hi2_email) and the
#  run_bot() loop above are NOT edited. Everything below only changes how the
#  bot looks, and adds limits / premium / admin / logging around them.
# ═══════════════════════════════════════════════════════════════════════════
import re as _re
import html as _html
import queue as _queue
import sqlite3
import contextlib as _ctx
import datetime as _dt
from io import BytesIO
from urllib.parse import quote as _quote
try:
    import qrcode
except Exception:
    os.system(f'"{sys.executable}" -m pip install "qrcode[pil]"')
    try:
        import qrcode
    except Exception:
        qrcode = None

# ─────────────────────────── CONFIG — EDIT THESE ───────────────────────────
OWNER_ID    = 6592441427          # your numeric Telegram id (admin)
ADMIN_IDS   = []                                       # optional extra admin ids
LOG_CHANNEL = "-1004331130989"            # e.g. -1001234567890  (bot must be admin there)
UPI_ID      = os.getenv("UPI_ID", "Ahmadammar@fam")    # same UPI as botV6
UPI_NAME    = os.getenv("UPI_NAME", "Erebus Premium")
DB_PATH     = os.getenv("DB_PATH", "erebus_checker.sqlite3")
EMOJI_FILE  = os.getenv("EMOJI_FILE", "emoji_ids.json")
USE_CUSTOM_EMOJI = os.getenv("USE_CUSTOM_EMOJI", "1") == "1"   # set 0 if animated emojis fail

FREE_DAILY  = 40      # free checks per day
BULK_MAX    = 500     # emails per bulk request (checked in chunks with cooldowns)
CHUNK_SIZE          = 20    # emails per chunk
CHUNK_COOLDOWN      = 10    # seconds of cooldown after every chunk of 20 (free / premium)
LONG_COOLDOWN_EVERY = 60    # after every 60 mails ...
LONG_COOLDOWN       = 20    # ... cooldown of 20 seconds instead of 10 (free / premium)
UNL_COOLDOWN_EVERY  = 100   # unlimited users: cooldown only after every 100 mails
UNL_COOLDOWN        = 20    # unlimited users: cooldown seconds
BACKUP_EVERY        = 30 * 60   # automatic database backup to the log channel (seconds)
MAX_PENDING = 3       # pending payment screenshots per user
PLANS = {             # key: name, checks/day (None = unlimited), days, price in INR
    'p100': {'name': 'Premium 100',       'limit': 100,  'days': 7, 'price': 21},
    'p200': {'name': 'Premium 200',       'limit': 200,  'days': 7, 'price': 31},
    'unl':  {'name': 'Premium Unlimited', 'limit': None, 'days': 7, 'price': 49},
}
CHANNEL_URL = 'https://t.me/linksfromerebus'
try:    LOG_CHANNEL = int(LOG_CHANNEL)
except Exception: pass
if LOG_CHANNEL == 0: LOG_CHANNEL = None

# ─────────────────────────── UI KIT (copied from botV6) ────────────────────
_SMALL_CAPS = str.maketrans("abcdefghijklmnopqrstuvwxyz", "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ")

def sc(text):
    """'free plan' -> 'Fʀᴇᴇ Pʟᴀɴ'. ACRONYMS, numbers, @names, /commands stay untouched."""
    def word(w):
        if any(c.isdigit() or c in "@/₹_<>&" for c in w) or (w.isupper() and len(w) > 1):
            return w
        m = _re.search(r"[A-Za-z]", w)
        if not m: return w
        i = m.end()
        return w[:i - 1] + w[i - 1].upper() + w[i:].translate(_SMALL_CAPS)
    return "".join(p if p.isspace() else word(p) for p in _re.split(r"(\s+)", text))

EMOJI = {
    "title": "✨", "star": "⭐", "camera": "📸", "bolt": "⚡", "user": "👤", "id": "🆔",
    "bot": "👾", "dev": "👨‍💻", "ok": "✅", "err": "❌", "warn": "⚠️", "time": "⏱",
    "pay": "💳", "box": "📦", "money": "💰", "calendar": "📅", "bell": "🔔", "ban": "🚫",
    "admin": "🛠", "mail": "✉️", "link": "🔗", "channel": "📢", "group": "👥",
    "stats": "📊", "lock": "🔒", "ghost": "👻", "home": "🏠", "bank": "🏦",
    "party": "🎉", "pin": "📝", "spin": "🌀",
}
DEFAULT_EMOJI_IDS = {
    "title": "5424972470023104089", "star": "5438496463044752972", "bolt": "5224607267797606837",
    "ok": "5206607081334906820", "err": "5210952531676504517", "warn": "5447644880824181073",
    "time": "5440621591387980068", "pay": "5444856076954520455", "box": "6046233639644042899",
    "money": "5278467510604160626", "calendar": "5413879192267805083", "bell": "5458603043203327669",
    "ban": "5260293700088511294", "admin": "5341715473882955310", "mail": "5253742260054409879",
    "link": "5271604874419647061", "channel": "5424818078833715060", "group": "5332724926216428039",
    "stats": "5231200819986047254", "lock": "5296369303661067030", "ghost": "5431609822288033666",
    "bank": "5332455502917949981", "party": "5276032951342088188", "pin": "5397782960512444700",
    "spin": "5375338737028841420",
}
EMOJI_IDS = {}
def load_emoji_ids():
    EMOJI_IDS.clear()
    if not USE_CUSTOM_EMOJI: return
    EMOJI_IDS.update(DEFAULT_EMOJI_IDS)
    try:
        with open(EMOJI_FILE, 'r', encoding='utf-8') as f:
            EMOJI_IDS.update({k: str(v) for k, v in json.load(f).items() if k in EMOJI})
    except Exception:
        pass
load_emoji_ids()

def E(name):
    """Emoji for HTML text (animated one when configured)."""
    fb = EMOJI.get(name, "•"); cid = EMOJI_IDS.get(name)
    return f'<tg-emoji emoji-id="{cid}">{fb}</tg-emoji>' if cid else fb
def P(name):
    """Plain emoji (used for channel logs)."""
    return EMOJI.get(name, "•")

def btn(text, emoji=None, style=None, **kw):
    """Inline button in the bot font. style: primary (blue) / success (green) / danger (red)."""
    b = {'text': sc(text), '_fb': EMOJI.get(emoji, '') if emoji else ''}
    cid = EMOJI_IDS.get(emoji) if emoji else None
    if cid: b['icon_custom_emoji_id'] = cid
    elif emoji: b['text'] = f"{EMOJI.get(emoji, '')} {b['text']}"
    if style: b['style'] = style
    b.update(kw)
    return b

def kb(*rows):
    return {'inline_keyboard': [list(r) for r in rows]}

def _mk(markup, plain=False):
    """Serialise a keyboard. plain=True drops animated icons / colours (fallback)."""
    if not markup: return None
    out = []
    for r in markup['inline_keyboard']:
        nr = []
        for b in r:
            b = dict(b); fb = b.pop('_fb', '')
            if plain:
                if b.pop('icon_custom_emoji_id', None) and fb: b['text'] = f"{fb} {b['text']}"
                b.pop('style', None)
            nr.append(b)
        out.append(nr)
    return json.dumps({'inline_keyboard': out})

SEP = "──────────────────"
def bq(t):   return f"<blockquote>{t}</blockquote>"
def head(emoji, title, tail=""): return f"{E(emoji)} <b>{sc(title)}</b>{tail}"
def row(emoji, label, value):    return f"{E(emoji)} <b>{sc(label)}</b> ➛ {value}"
def esc(v):  return _html.escape(str(v))

# ─────────────────────────── telegram plumbing ─────────────────────────────
_TG_EMO = _re.compile(r'<tg-emoji emoji-id="\d+">(.*?)</tg-emoji>', _re.S)
def _plainify(t): return _TG_EMO.sub(r'\1', t or '')

def _call(method, data=None, files=None, timeout=20):
    try:
        d = {k: v for k, v in (data or {}).items() if v is not None}
        r = requests.post(f"{API_URL}/{method}", data=d, files=files, timeout=timeout).json()
        ra = (r.get('parameters') or {}).get('retry_after') if not r.get('ok') else None
        if ra and int(ra) <= 5:                      # Telegram flood control: wait, then retry once
            time.sleep(int(ra) + 0.5)
            if files:                                # file handles can't be re-read safely
                return r
            r = requests.post(f"{API_URL}/{method}", data=d, files=files, timeout=timeout).json()
        return r
    except Exception:
        return {}

def _desc(r): return str(r.get('description', '')).lower()

def send_message(chat_id, text, parse_mode='HTML', reply_markup=None, **kw):
    d = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode,
         'link_preview_options': json.dumps({'is_disabled': True})}
    d.update(kw)
    if reply_markup: d['reply_markup'] = _mk(reply_markup)
    r = _call('sendMessage', d)
    if not r.get('ok') and r.get('error_code') == 400:       # animated emoji / colour not accepted -> plain
        d['text'] = _plainify(text)
        if reply_markup: d['reply_markup'] = _mk(reply_markup, True)
        r2 = _call('sendMessage', d)
        if r2.get('ok'): r = r2
    return (r.get('result') or {}).get('message_id')

def _edit_raw(chat_id, message_id, text, reply_markup=None, parse_mode='HTML'):
    d = {'chat_id': chat_id, 'message_id': message_id, 'text': text, 'parse_mode': parse_mode,
         'link_preview_options': json.dumps({'is_disabled': True})}
    if reply_markup is not None: d['reply_markup'] = _mk(reply_markup)
    r = _call('editMessageText', d)
    if not r.get('ok') and r.get('error_code') == 400 and 'not modified' not in _desc(r):
        d['text'] = _plainify(text)
        if reply_markup is not None: d['reply_markup'] = _mk(reply_markup, True)
        r = _call('editMessageText', d)
    return r

def edit_message(chat_id, message_id, text, parse_mode='HTML', reply_markup=None):
    _edit_raw(chat_id, message_id, text, reply_markup, parse_mode)

def send_photo(chat_id, photo, caption, reply_markup=None):
    """photo = bytes (generated image) or a Telegram file_id."""
    def go(plain):
        d = {'chat_id': chat_id, 'caption': _plainify(caption) if plain else caption, 'parse_mode': 'HTML'}
        if reply_markup: d['reply_markup'] = _mk(reply_markup, plain)
        if isinstance(photo, (bytes, bytearray)):
            return _call('sendPhoto', d, files={'photo': ('upi_qr.png', bytes(photo))}, timeout=30)
        d['photo'] = photo
        return _call('sendPhoto', d, timeout=30)
    r = go(False)
    if not r.get('ok') and r.get('error_code') == 400: r = go(True)
    return (r.get('result') or {}).get('message_id')

def send_document(chat_id, filename, content, caption=''):
    if isinstance(content, str): content = content.encode('utf-8')
    return _call('sendDocument', {'chat_id': chat_id, 'caption': caption, 'parse_mode': 'HTML'},
                 files={'document': (filename, content)}, timeout=60)

def _del(chat_id, message_id):
    _call('deleteMessage', {'chat_id': chat_id, 'message_id': message_id}, timeout=10)

# ── auto-cleaning of messages that are no longer important (as in V6) ──
_TRASH, _PANEL, _CB, _LAST = {}, {}, {}, {}
_tl = threading.Lock()

def remember(chat_id, mid):
    if mid:
        with _tl: _TRASH.setdefault(chat_id, []).append(mid)
    return mid

def sweep(chat_id, keep=None):
    with _tl: ids = _TRASH.pop(chat_id, [])
    for m in ids:
        if m != keep: _del(chat_id, m)

def tidy(chat_id, mid):
    if mid: _del(chat_id, mid)

def tidy_last(chat_id):
    with _tl: mid = _LAST.pop(chat_id, None)
    if mid: _del(chat_id, mid)

def notice(chat_id, text, ttl=8, reply_markup=None):
    mid = send_message(chat_id, text, reply_markup=reply_markup)
    if mid:
        t = threading.Timer(ttl, _del, args=(chat_id, mid)); t.daemon = True; t.start()
    return mid

def show_panel(chat_id, text, markup):
    old = _PANEL.pop(chat_id, None)
    if old: _del(chat_id, old)
    mid = send_message(chat_id, text, reply_markup=markup)
    if mid: _PANEL[chat_id] = mid
    return mid

def safe_edit(cb, text, markup=None):
    """Edit the menu in place. A photo message (the QR) is replaced instead."""
    msg = cb.get('message') or {}; chat = msg.get('chat', {}).get('id'); mid = msg.get('message_id')
    if msg.get('photo'):
        _del(chat, mid)
        new = send_message(chat, text, reply_markup=markup)
        if new: _PANEL[chat] = new
        return
    r = _edit_raw(chat, mid, text, markup)
    if not r.get('ok') and 'not modified' not in _desc(r):
        new = send_message(chat, text, reply_markup=markup)
        if new: _PANEL[chat] = new

# ─────────────────────────── database ──────────────────────────────────────
@_ctx.contextmanager
def db():
    con = sqlite3.connect(DB_PATH, timeout=15); con.row_factory = sqlite3.Row
    try:
        yield con; con.commit()
    except Exception:
        con.rollback(); raise
    finally:
        con.close()

def init_db():
    with db() as con:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY, username TEXT, name TEXT,
            joined_at INTEGER NOT NULL, last_seen INTEGER NOT NULL,
            banned INTEGER NOT NULL DEFAULT 0, custom_limit INTEGER);
        CREATE TABLE IF NOT EXISTS premium(
            user_id INTEGER PRIMARY KEY, plan TEXT NOT NULL, expires_at INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS usage_daily(
            user_id INTEGER NOT NULL, day TEXT NOT NULL, count INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY(user_id, day));
        CREATE TABLE IF NOT EXISTS payments(
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, plan TEXT NOT NULL,
            days INTEGER NOT NULL, amount INTEGER NOT NULL, file_id TEXT,
            status TEXT NOT NULL DEFAULT 'pending', created_at INTEGER NOT NULL, reviewed_at INTEGER);
        CREATE TABLE IF NOT EXISTS broadcasts(
            id INTEGER PRIMARY KEY AUTOINCREMENT, admin_id INTEGER, sent INTEGER, failed INTEGER, created_at INTEGER);
        CREATE TABLE IF NOT EXISTS check_log(
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, email TEXT NOT NULL,
            result TEXT NOT NULL, ts INTEGER NOT NULL);
        CREATE INDEX IF NOT EXISTS idx_check_log_ts ON check_log(ts);
        CREATE TABLE IF NOT EXISTS tokens(
            code TEXT PRIMARY KEY, checks INTEGER NOT NULL, max_uses INTEGER NOT NULL,
            used INTEGER NOT NULL DEFAULT 0, expires_at INTEGER, created_at INTEGER NOT NULL,
            active INTEGER NOT NULL DEFAULT 1);
        CREATE TABLE IF NOT EXISTS token_uses(
            code TEXT NOT NULL, user_id INTEGER NOT NULL, used_at INTEGER NOT NULL, PRIMARY KEY(code, user_id));
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT NOT NULL,
            reward INTEGER NOT NULL, active INTEGER NOT NULL DEFAULT 1, created_at INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS task_subs(
            id INTEGER PRIMARY KEY AUTOINCREMENT, task_id INTEGER NOT NULL, user_id INTEGER NOT NULL,
            file_id TEXT, status TEXT NOT NULL DEFAULT 'pending', created_at INTEGER NOT NULL, reviewed_at INTEGER);
        """)
        for _col, _typ in (("bonus", "INTEGER NOT NULL DEFAULT 0"), ("bonus_used", "INTEGER NOT NULL DEFAULT 0"),
                           ("referred_by", "INTEGER"), ("ref_count", "INTEGER NOT NULL DEFAULT 0")):
            try: con.execute(f"ALTER TABLE users ADD COLUMN {_col} {_typ}")
            except Exception: pass

_IST = _dt.timezone(_dt.timedelta(hours=5, minutes=30))
def _now():   return int(time.time())
def _today(): return _dt.datetime.now(_IST).strftime('%Y-%m-%d')
def _fmt(ts): return _dt.datetime.fromtimestamp(ts, _IST).strftime('%d %b %Y, %I:%M %p IST') if ts else '-'
def _dshort(ts): return _dt.datetime.fromtimestamp(ts, _IST).strftime('%d %b %Y')

def is_admin(uid): return bool(uid) and (uid == OWNER_ID or uid in ADMIN_IDS)

def get_user(uid):
    with db() as con: return con.execute("SELECT * FROM users WHERE user_id=?", (uid,)).fetchone()

def is_banned(uid):
    r = get_user(uid); return bool(r and r['banned'])

def find_user(token):
    """@username (must have started the bot) or numeric id -> row / None"""
    token = token.strip()
    with db() as con:
        if token.lstrip('-').isdigit():
            return con.execute("SELECT * FROM users WHERE user_id=?", (int(token),)).fetchone()
        return con.execute("SELECT * FROM users WHERE lower(username)=?", (token.lstrip('@').lower(),)).fetchone()

def _label(r): return f"@{r['username']}" if r['username'] else (r['name'] or str(r['user_id']))

def _utag(uid, name='', username=''):
    n = esc(name or 'User'); u = f" (@{esc(username)})" if username else ''
    return f'<a href="tg://user?id={uid}">{n}</a>{u} <code>{uid}</code>'

def _utag_id(uid):
    r = get_user(uid)
    return _utag(uid, r['name'] if r else '', r['username'] if r else '')

def plan_info(uid):
    with db() as con: r = con.execute("SELECT plan,expires_at FROM premium WHERE user_id=?", (uid,)).fetchone()
    if r and r['expires_at'] > _now() and r['plan'] in PLANS: return r['plan'], r['expires_at']
    return None, 0

def user_limit(uid):
    """checks/day for this user. None = unlimited."""
    if is_admin(uid): return None
    key, _x = plan_info(uid)
    if key: return PLANS[key]['limit']
    r = get_user(uid)
    if r and r['custom_limit'] is not None: return r['custom_limit']
    return FREE_DAILY

def used_today(uid):
    with db() as con:
        r = con.execute("SELECT count FROM usage_daily WHERE user_id=? AND day=?", (uid, _today())).fetchone()
    return r['count'] if r else 0

def bonus_of(uid):
    r = get_user(uid)
    return int(r['bonus'] or 0) if r else 0

def remaining(uid):
    """daily checks left + bonus checks (redeem / referral / tasks). None = unlimited."""
    lim = user_limit(uid)
    return None if lim is None else max(0, lim - used_today(uid)) + bonus_of(uid)

def add_usage(uid, n=1):
    """Uses the daily allowance first, then the bonus balance."""
    if n <= 0: return
    lim = user_limit(uid); daily_part, bonus_part = n, 0
    if lim is not None:
        daily_part = min(n, max(0, lim - used_today(uid))); bonus_part = n - daily_part
    with db() as con:
        if daily_part:
            con.execute("INSERT INTO usage_daily(user_id,day,count) VALUES(?,?,?) "
                        "ON CONFLICT(user_id,day) DO UPDATE SET count=count+excluded.count", (uid, _today(), daily_part))
        if bonus_part:
            con.execute("UPDATE users SET bonus=MAX(0,COALESCE(bonus,0)-?), bonus_used=COALESCE(bonus_used,0)+? WHERE user_id=?",
                        (bonus_part, bonus_part, uid))

def total_checks(uid):
    with db() as con:
        n = con.execute("SELECT COALESCE(SUM(count),0) n FROM usage_daily WHERE user_id=?", (uid,)).fetchone()['n']
        r = con.execute("SELECT bonus_used FROM users WHERE user_id=?", (uid,)).fetchone()
    return n + (int(r['bonus_used'] or 0) if r else 0)

def grant(uid, key, days=None, extend=True):
    days = days or PLANS[key]['days']; base = _now()
    cur, exp = plan_info(uid)
    if extend and cur == key and exp > base: base = exp
    expiry = base + days * 86400
    with db() as con:
        con.execute("INSERT INTO premium(user_id,plan,expires_at) VALUES(?,?,?) "
                    "ON CONFLICT(user_id) DO UPDATE SET plan=excluded.plan, expires_at=excluded.expires_at",
                    (uid, key, expiry))
    return expiry

def pending_payments(uid=None):
    with db() as con:
        if uid is None: return con.execute("SELECT COUNT(*) n FROM payments WHERE status='pending'").fetchone()['n']
        return con.execute("SELECT COUNT(*) n FROM payments WHERE user_id=? AND status='pending'", (uid,)).fetchone()['n']

# ─────────────────────────── channel logging queue ─────────────────────────
_LOGQ = _queue.Queue()
def log(text):
    if LOG_CHANNEL: _LOGQ.put(('m', text))
def log_photo(file_id, caption):
    if LOG_CHANNEL: _LOGQ.put(('p', file_id, caption))
def log_doc(name, content, caption=''):
    if LOG_CHANNEL: _LOGQ.put(('d', name, content, caption))

def _log_worker():
    while True:
        item = _LOGQ.get()
        for _try in range(3):
            try:
                if item[0] == 'm':
                    r = _call('sendMessage', {'chat_id': LOG_CHANNEL, 'text': item[1], 'parse_mode': 'HTML',
                                              'link_preview_options': json.dumps({'is_disabled': True})})
                elif item[0] == 'p':
                    r = _call('sendPhoto', {'chat_id': LOG_CHANNEL, 'photo': item[1], 'caption': item[2], 'parse_mode': 'HTML'})
                else:
                    r = send_document(LOG_CHANNEL, item[1], item[2], item[3])
                if r.get('ok'): break
                ra = (r.get('parameters') or {}).get('retry_after')
                if ra: time.sleep(min(int(ra), 30)); continue
                if r.get('description'): print(f"{spy28}[!] log channel: {r.get('description')}{reset}")
                break
            except Exception:
                break
        time.sleep(1.2)       # channels allow ~20 msgs / minute

def backup_now(reason='backup', chat_id=None):
    """Consistent copy of the database -> log channel (and optionally to an admin chat)."""
    try:
        tmp = DB_PATH + '.bak'
        s = sqlite3.connect(DB_PATH); d = sqlite3.connect(tmp); s.backup(d); d.close(); s.close()
        with open(tmp, 'rb') as f: data = f.read()
        os.remove(tmp)
        stamp = _dt.datetime.now(_IST).strftime('%Y%m%d_%H%M')
        name = f'erebus_backup_{stamp}.sqlite3'
        cap = (f"💾 <b>{sc('Database backup')}</b> ‣ {esc(reason)}\n"
               f"{P('calendar')} {_fmt(_now())}\n{P('box')} {len(data) // 1024} KB")
        log_doc(name, data, cap)
        if chat_id: send_document(chat_id, name, data, cap)
        return True
    except Exception as e:
        print(f"{spy28}[!] backup failed: {e}{reset}")
        return False

def _backup_worker():
    time.sleep(60)
    while True:
        backup_now('auto · every 30 min')
        time.sleep(BACKUP_EVERY)

def _download_file(file_id):
    r = _call('getFile', {'file_id': file_id})
    path = (r.get('result') or {}).get('file_path')
    if not path: return None
    try:
        resp = requests.get(f"https://api.telegram.org/file/bot{BOT_TOKEN}/{path}", timeout=90)
        return resp.content if resp.ok else None
    except Exception:
        return None

def restore_from_bytes(data):
    """Validate an uploaded backup and load it into the live database. -> (ok, message)"""
    tmp = DB_PATH + '.restore'
    try:
        with open(tmp, 'wb') as f: f.write(data)
        src = sqlite3.connect(tmp)
        try:
            if src.execute("PRAGMA integrity_check").fetchone()[0] != 'ok':
                return False, 'The file is corrupted.'
            names = {r[0] for r in src.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            if not {'users', 'premium', 'usage_daily', 'payments'} <= names:
                return False, 'This is not an Erebus backup file.'
            # safety copy of the current data first
            cur = sqlite3.connect(DB_PATH); sf = sqlite3.connect(DB_PATH + '.before_restore')
            cur.backup(sf); sf.close(); cur.close()
            dst = sqlite3.connect(DB_PATH, timeout=30)
            try: src.backup(dst)
            finally: dst.close()
        finally:
            src.close()
        init_db()          # adds any table an older backup does not have
        return True, ''
    except Exception as e:
        return False, str(e)
    finally:
        try: os.remove(tmp)
        except Exception: pass

# ─────────────────────────── check log + admin report ──────────────────────
def log_check(uid, email, result):
    try:
        with db() as con:
            con.execute("INSERT INTO check_log(user_id,email,result,ts) VALUES(?,?,?,?)", (uid, email, result, _now()))
    except Exception as e:
        print(f"{spy28}[!] check log: {e}{reset}")

def _check_counts(since=None):
    with db() as con:
        if since is None:
            rs = con.execute("SELECT result, COUNT(*) n FROM check_log GROUP BY result").fetchall()
        else:
            rs = con.execute("SELECT result, COUNT(*) n FROM check_log WHERE ts>=? GROUP BY result", (since,)).fetchall()
    d = {r['result']: r['n'] for r in rs}
    t, f, u = d.get('taken', 0), d.get('not_taken', 0), d.get('unknown', 0)
    return t + f + u, t, f, u

def check_report_text():
    now = _now(); day0 = now - (now + 19800) % 86400
    lines = [bq(f"{E('stats')} {sc('Check report')}"), ""]
    for name, since in (('Last 1 hour', now - 3600), ('Today', day0), ('All time', None)):
        tot, t, f, u = _check_counts(since)
        lines += [f"{E('calendar')} <b>{sc(name)}</b>",
                  row('mail', 'Checks Done', tot),
                  f"{E('err')} {sc('Taken')} ➛ <b>{t}</b>  ·  {E('ok')} {sc('Free')} ➛ <b>{f}</b>  ·  ❔ {sc('Unknown')} ➛ <b>{u}</b>",
                  ""]
    with db() as con:
        rs = con.execute("SELECT email, MAX(ts) AS lt FROM check_log WHERE result='not_taken' AND ts>=? "
                         "GROUP BY email ORDER BY lt DESC LIMIT 10", (now - 3600,)).fetchall()
    lines += [SEP, f"{E('ok')} <b>{sc('Latest free mails (last 1 hour)')}</b>"]
    if rs:
        for i, r in enumerate(rs, 1):
            tm = _dt.datetime.fromtimestamp(r['lt'], _IST).strftime('%I:%M %p')
            lines.append(f"{i}. <code>{esc(r['email'])}</code> · {tm}")
    else:
        lines.append(sc('None found in the last hour.'))
    lines += ["", f"{E('time')} {sc('Updated')} {_fmt(now)}"]
    return "\n".join(lines)

# ─────────────────────────── users: register / export ──────────────────────
def register(frm, ref=None):
    uid = frm.get('id')
    if not uid: return
    name = ((frm.get('first_name') or '') + ' ' + (frm.get('last_name') or '')).strip()
    un = frm.get('username') or ''
    new = False; credited = None
    with db() as con:
        if con.execute("SELECT 1 FROM users WHERE user_id=?", (uid,)).fetchone():
            con.execute("UPDATE users SET username=?, name=?, last_seen=? WHERE user_id=?", (un, name, _now(), uid))
        else:
            rb = ref if (ref and ref != uid and con.execute("SELECT 1 FROM users WHERE user_id=?", (ref,)).fetchone()) else None
            con.execute("INSERT INTO users(user_id,username,name,joined_at,last_seen,referred_by) VALUES(?,?,?,?,?,?)",
                        (uid, un, name, _now(), _now(), rb)); new = True
            if rb:      # brand-new user came through a referral link -> reward the referrer
                con.execute("UPDATE users SET bonus=COALESCE(bonus,0)+?, ref_count=COALESCE(ref_count,0)+1 WHERE user_id=?",
                            (REF_BONUS, rb)); credited = rb
        total = con.execute("SELECT COUNT(*) n FROM users").fetchone()['n']
    if credited:
        send_message(credited, "\n".join([
            bq(f"{E('party')} {sc('New referral!')}"), "",
            row('user', 'Joined', esc(name or 'User')),
            row('bolt', 'You Got', f"+{REF_BONUS} {sc('bonus checks')}"),
            row('star', 'Bonus Balance', bonus_of(credited))]),
            reply_markup=kb([btn('Free Checks', 'party', callback_data='free')]))
    if new:
        log(f"{P('title')} <b>{sc('New user')}</b> #{total}\n{_utag(uid, name, un)}\n"
            f"{P('calendar')} {_fmt(_now())}")

def users_csv():
    out = ["id,username,name,plan,plan_expires,used_today,total_checks,joined,last_seen,banned"]
    with db() as con: rs = con.execute("SELECT * FROM users ORDER BY joined_at").fetchall()
    for r in rs:
        key, exp = plan_info(r['user_id'])
        nm = (r['name'] or '').replace('"', "'")
        out.append(f"{r['user_id']},{r['username'] or ''},\"{nm}\",{PLANS[key]['name'] if key else 'Free'},"
                   f"{_fmt(exp) if key else ''},{used_today(r['user_id'])},{total_checks(r['user_id'])},"
                   f"{_fmt(r['joined_at'])},{_fmt(r['last_seen'])},{r['banned']}")
    return "\n".join(out), len(rs)

def export_users(chat_id):
    csv_, n = users_csv()
    cap = f"{P('group')} <b>{sc('All users')}</b> ‣ {n}"
    send_document(chat_id, 'erebus_users.csv', csv_, cap)
    log_doc('erebus_users.csv', csv_, cap)

# ─────────────────────────── screens ───────────────────────────────────────
def _lim_txt(uid):
    lim = user_limit(uid); b = bonus_of(uid)
    base = f"{min(used_today(uid), lim) if lim is not None else used_today(uid)} / {'∞' if lim is None else lim}"
    return base + (f"  (+{b} {sc('bonus')})" if b and lim is not None else '')

def home_text(uid, name):
    key, exp = plan_info(uid)
    if is_admin(uid): plan = sc('Admin')
    elif key:         plan = f"{sc(PLANS[key]['name'])} ({_dshort(exp)})"
    else:             plan = sc('Free')
    return "\n".join([
        bq(f"{E('user')} {sc('Welcome')}, {esc(name or 'friend')}"),
        head('title', 'Hi2 Mail Checker', ' ❗️'),
        "",
        row('star', 'Plan', plan),
        row('mail', 'Today', _lim_txt(uid)),
        row('box', 'Bulk Limit', f"{BULK_MAX} / {sc('batch')}"),
        SEP,
        f"{E('bolt')} {sc('Pick a mode to start checking')}",
        "", "Bʏ ‣ 𝑯𝒂𝒛𝒆 @Noxmirage",
    ])

def home_kb(uid):
    rows = [
        [btn('Single Mode', 'mail', callback_data='mode_single'), btn('Bulk Mode', 'box', callback_data='mode_bulk')],
        [btn('My Premium', 'star', callback_data='mypremium'), btn('My Statistics', 'stats', callback_data='mystats')],
        [btn('Buy Premium', 'pay', style='primary', callback_data='buy')],
        [btn('Redeem', 'bolt', callback_data='redeem'), btn('Free Checks', 'party', callback_data='free')],
        [btn('Updates', 'channel', url=CHANNEL_URL)],
    ]
    if is_admin(uid): rows.append([btn('Admin Panel', 'admin', callback_data='admin')])
    return kb(*rows)

def back_kb(*top):
    return kb(*top, [btn('Main Menu', 'home', callback_data='back_menu')])

def send_welcome(chat_id):
    r = get_user(chat_id)
    text = home_text(chat_id, (r['name'] if r else '') or '')
    markup = home_kb(chat_id)
    cbm = _CB.pop(chat_id, None)
    if cbm:
        mid, is_photo = cbm
        if not is_photo:
            res = _edit_raw(chat_id, mid, text, markup)
            if res.get('ok') or 'not modified' in _desc(res):
                _PANEL[chat_id] = mid; return
        _del(chat_id, mid)
    show_panel(chat_id, text, markup)

def send_single_prompt(chat_id, message_id=None):
    text = "\n".join([
        bq(f"{E('mail')} {sc('Single mode')}"), "",
        row('pin', 'Input', sc('Send a username or email address')),
        row('pin', 'Example', "<code>john</code>  <code>john@hi2.in</code>"),
        row('mail', 'Today', _lim_txt(chat_id)),
        SEP,
        f"{E('bolt')} {sc('Your request is processed after you submit your input.')}",
        "", "Bʏ ‣ 𝑯𝒂𝒛𝒆 @Noxmirage",
    ])
    markup = back_kb()
    if message_id: _edit_raw(chat_id, message_id, text, markup)
    else: send_message(chat_id, text, reply_markup=markup)

def send_bulk_prompt(chat_id, message_id=None):
    text = "\n".join([
        bq(f"{E('box')} {sc('Bulk mode')}"), "",
        row('pin', 'Input', sc('Send emails separated by spaces')),
        row('pin', 'Example', "<code>john@hi2.in jane Haze@hi2.in</code>"),
        row('box', 'Max Per Batch', BULK_MAX),
        row('time', 'Cooldown', f"{CHUNK_COOLDOWN}s / {CHUNK_SIZE} {sc('mails')}"),
        row('mail', 'Today', _lim_txt(chat_id)),
        SEP,
        f"{E('bolt')} {sc('Your request is processed after you submit your input.')}",
        f"{E('pin')} {sc('Use /start to return to the main menu.')}",
        "", "Bʏ ‣ 𝑯𝒂𝒛𝒆 @Noxmirage",
    ])
    markup = back_kb()
    if message_id: _edit_raw(chat_id, message_id, text, markup)
    else: send_message(chat_id, text, reply_markup=markup)

def limit_text(uid):
    return "\n".join([
        bq(f"{E('ban')} {sc('Daily limit reached')}"), "",
        row('mail', 'Used Today', _lim_txt(uid)),
        row('time', 'Resets', f"{sc('Midnight')} IST"),
        SEP,
        f"{E('star')} {sc('Go premium or earn free checks to keep checking today.')}",
    ])

def send_limit(chat_id):
    send_message(chat_id, limit_text(chat_id),
                 reply_markup=back_kb([btn('Buy Premium', 'pay', style='primary', callback_data='buy')],
                                      [btn('Free Checks', 'party', callback_data='free')]))

def plans_text():
    lines = [bq(f"{E('pay')} {sc('Premium plans')}"), "",
             row('user', 'Free', f"{FREE_DAILY} / {sc('day')}")]
    for k, p in PLANS.items():
        lim = sc('Unlimited') if p['limit'] is None else f"{p['limit']} / {sc('day')}"
        lines.append(row('star', p['name'], f"₹{p['price']} · {lim} · {p['days']} {sc('days')}"))
    lines += [SEP, f"{E('pay')} {sc('Select a plan to get your payment QR.')}"]
    return "\n".join(lines)

def plans_kb():
    rows = [[btn(f"{p['name']} — ₹{p['price']}", 'star', callback_data=f"plan:{k}")] for k, p in PLANS.items()]
    rows.append([btn('Free Checks', 'party', callback_data='free')])
    rows.append([btn('Main Menu', 'home', callback_data='back_menu')])
    return kb(*rows)

def upi_link(price, note):
    return f"upi://pay?pa={UPI_ID}&pn={_quote(UPI_NAME)}&am={price}&cu=INR&tn={_quote(note)}"

def make_qr(data):
    if qrcode is None: return None
    try:
        q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
        q.add_data(data); q.make(fit=True)
        buf = BytesIO(); q.make_image(fill_color="black", back_color="white").save(buf)
        return buf.getvalue()
    except Exception:
        return None

def _my_premium_text(uid):
    key, exp = plan_info(uid)
    if key:
        lim = PLANS[key]['limit']
        return "\n".join([
            bq(f"{E('star')} {sc('Premium member')}"), "",
            row('star', 'Plan', sc(PLANS[key]['name'])),
            row('calendar', 'Active Until', _fmt(exp)),
            row('bolt', 'Daily Limit', sc('Unlimited') if lim is None else lim),
            row('mail', 'Used Today', _lim_txt(uid)),
        ]), True
    return "\n".join([
        bq(f"{E('user')} {sc('You are on the free plan')}"), "",
        row('bolt', 'Daily Limit', user_limit(uid)),
        row('mail', 'Used Today', _lim_txt(uid)),
        SEP, f"{E('star')} {sc('Go premium for 100, 200 or unlimited checks a day.')}",
    ]), False

# ─────────────────────────── checking UI (engine untouched) ────────────────
_STATUS = {'taken': ('err', 'Tᴀᴋᴇɴ'), 'not_taken': ('ok', 'Nᴏᴛ Tᴀᴋᴇɴ')}

def animate_check(chat_id, email, stop_event, frames_per_sec=0.5):
    """live spinner message; returned function turns it into the final report"""
    holder = {'id': None}
    def loop():
        i = 0
        while not stop_event.is_set():
            f = SPINNER[i % len(SPINNER)]
            t = f"{E('spin')} <b>{sc('Checking')}</b> ➛ <code>{esc(email)}</code> {f}"
            if holder['id'] is None: holder['id'] = send_message(chat_id, t)
            else: edit_message(chat_id, holder['id'], t)
            i += 1
            stop_event.wait(1 / frames_per_sec)
    th = threading.Thread(target=loop, daemon=True); th.start()
    def finish(result_text, reply_markup=None):
        stop_event.set(); th.join(timeout=3)
        if holder['id'] is None: send_message(chat_id, result_text, reply_markup=reply_markup)
        else: _edit_raw(chat_id, holder['id'], result_text, reply_markup)
    return finish

_BUSY, _bl = set(), threading.Lock()
def _acquire(uid):
    with _bl:
        if uid in _BUSY: return False
        _BUSY.add(uid); return True
def _release(uid):
    with _bl: _BUSY.discard(uid)

def _result_kb():
    return back_kb([btn('Channel', 'channel', url=CHANNEL_URL)])

def _single_job(chat, email):
    try:
        stop = threading.Event(); fin = animate_check(chat, email, stop)
        res = check_hi2_email(email); stop.set()
        log_check(chat, email, res)
        if res != 'unknown': add_usage(chat, 1)
        if res in _STATUS: e, label = _STATUS[res]; status = f"{E(e)} <b>{label}</b>"
        else: status = "💭 <b>Uɴᴋɴᴏᴡɴ</b>"
        rem = remaining(chat)
        text = "\n".join([
            bq(f"{E('stats')} {sc('Availability report')} 💐"), "",
            row('mail', 'Email', f"<code>{esc(email)}</code>"),
            row('star', 'Status', status),
            row('bolt', 'Left Today', '∞' if rem is None else rem),
        ])
        fin(text, _result_kb())
        log(f"{P('mail')} <b>{sc('Single check')}</b>\n{_utag_id(chat)}\n"
            f"{P('mail')} <code>{esc(email)}</code> ➛ <b>{res}</b>")
    except Exception as ex:
        print(f"{spy28}[!] single job: {ex}{reset}")
    finally:
        _release(chat)

def process_single(chat_id, raw_input):
    tidy_last(chat_id)
    A = (raw_input or '').strip().lower()
    if not A: return
    if '@' in A:
        h, d = A.split('@', 1)
        if d not in SUPPORTED_DOMAINS:
            send_message(chat_id, "\n".join([
                bq(f"{E('err')} {sc('Invalid domain')}"), "",
                sc('Please use one of the supported domains'),
                "<code>" + ", ".join('@' + x for x in SUPPORTED_DOMAINS) + "</code>"]),
                reply_markup=back_kb())
            return
        email = f"{h}@{d}"
    else:
        email = f"{A}@hi2.in"
    rem = remaining(chat_id)
    if rem is not None and rem < 1: return send_limit(chat_id)
    if not _acquire(chat_id):
        return notice(chat_id, f"{E('warn')} {sc('Your previous check is still running, please wait.')}", ttl=6)
    threading.Thread(target=_single_job, args=(chat_id, email), daemon=True).start()

def _bulk_render(lines, header_extra=''):
    return "\n".join([bq(f"{E('stats')} {sc('Availability report')} 💐"), ""] + lines + ([header_extra] if header_extra else []))

def _cooldown_secs(done, total, unlimited):
    """Cooldown to apply after `done` mails of `total` (0 = none).
    Free/premium: 10s after every 20, 20s after every 60.  Unlimited: 20s after every 100."""
    if done >= total: return 0
    if unlimited:
        return UNL_COOLDOWN if done % UNL_COOLDOWN_EVERY == 0 else 0
    if done % LONG_COOLDOWN_EVERY == 0: return LONG_COOLDOWN
    if done % CHUNK_SIZE == 0: return CHUNK_COOLDOWN
    return 0

def _bulk_job(chat, items):
    try:
        n = len(items); unlimited = user_limit(chat) is None
        cnt = {'t': 0, 'f': 0, 'u': 0}; all_lines = []; chunk_lines = []; mid = None
        parts = (n + CHUNK_SIZE - 1) // CHUNK_SIZE

        def render(part, extra=''):
            tail = f" · {part}/{parts}" if parts > 1 else ''
            return "\n".join([bq(f"{E('stats')} {sc('Availability report')} 💐{tail}"), ""]
                             + chunk_lines + ([extra] if extra else []))

        for i, em in enumerate(items, 1):
            part = (i - 1) // CHUNK_SIZE + 1
            cur = f"{E('spin')} <b>{sc('Checking')}</b> ➛ <code>{esc(em)}</code> ({i}/{n})"
            if (i - 1) % CHUNK_SIZE == 0:                      # new chunk -> new message
                chunk_lines = []; mid = send_message(chat, render(part, cur))
            elif mid:
                _edit_raw(chat, mid, render(part, cur))
            res = check_hi2_email(em)
            log_check(chat, em, res)
            if res == 'taken':       a, b_ = '❌', 'Tᴀᴋᴇɴ'; cnt['t'] += 1
            elif res == 'not_taken': a, b_ = '🍀', 'Fʀᴇᴇ';  cnt['f'] += 1
            else:                    a, b_ = '❔', 'Uɴᴋɴᴏᴡɴ'; cnt['u'] += 1
            if res != 'unknown': add_usage(chat, 1)
            line = f"{i}. {a} <code>{esc(em)}</code> ➛ <b>{b_}</b>"
            chunk_lines.append(line); all_lines.append(line)
            time.sleep(1.0)
            wait = _cooldown_secs(i, n, unlimited)
            if wait and mid:                                   # cooldown with a live countdown
                end = time.time() + wait
                last_left = None
                while True:
                    left = int(end - time.time() + 0.99)
                    if left <= 0: break
                    if left != last_left:
                        last_left = left
                        done_blocks = int(10 * (wait - left) / wait)
                        bar = '█' * done_blocks + '░' * (10 - done_blocks)
                        _edit_raw(chat, mid, render(part, "\n".join([
                            SEP,
                            f"{E('time')} <b>{sc('Cooldown')}</b> ➛ <b>{left}s</b>",
                            f"<code>{bar}</code>",
                            f"{E('bolt')} {sc('Next')} {CHUNK_SIZE} {sc('mails start automatically')}"])))
                    time.sleep(0.3)
            elif wait:
                time.sleep(wait)
            if mid and (i % CHUNK_SIZE == 0 or i == n):        # chunk finished -> final text of this chunk
                _edit_raw(chat, mid, render(part))
        rem = remaining(chat)
        final = "\n".join([
            bq(f"{E('stats')} {sc('Bulk summary')} 💐"), "",
            row('ok', 'Total Checked', n),
            row('err', 'Taken', cnt['t']) + "  ·  " + row('ok', 'Free', cnt['f']),
            row('bolt', 'Left Today', '∞' if rem is None else rem),
            row('channel', 'Channel', '@ErebusRedirect'),
        ] + ([f"{E('warn')} {sc('Unknown results are not counted against your limit.')}"] if cnt['u'] else []))
        send_message(chat, final, reply_markup=_result_kb())
        body = ''
        for l in all_lines:
            if len(body) + len(l) > 3200: break
            body += l + "\n"
        log(f"{P('box')} <b>{sc('Bulk check')}</b> ‣ {n}\n{_utag_id(chat)}\n" + body)
    except Exception as ex:
        print(f"{spy28}[!] bulk job: {ex}{reset}")
    finally:
        _release(chat)

def process_bulk(chat_id, text):
    tidy_last(chat_id)
    C = chat_id; M = text.replace(',', ' ').split(); H, B, D = set(), [], []
    for A in M:
        A = A.strip().lower()
        if not A or A in H: continue
        H.add(A)
        if '@' in A:
            _h, N = A.split('@', 1)
            if N in SUPPORTED_DOMAINS: B.append(A)
            else: D.append(f"{A} (bad domain)")
        else:
            B.append(f"{A}@hi2.in")
    if not B:
        return send_message(C, "\n".join([
            bq(f"{E('err')} {sc('No valid mail found')}"), "",
            row('pin', 'Example', "<code>user@hi2.in user2</code>")]), reply_markup=back_kb())
    rem = remaining(C)
    if rem is not None and rem < 1: return send_limit(C)
    allowed = BULK_MAX if rem is None else min(BULK_MAX, rem)
    total = len(B)
    if total > allowed:
        why = (f"{sc('Max')} {BULK_MAX} {sc('emails per batch')}" if allowed == BULK_MAX
               else f"{sc('Only')} {rem} {sc('checks left today')}")
        send_message(C, "\n".join([
            bq(f"{E('warn')} {sc('Limit applied')}"), "",
            f"{E('pin')} {why}",
            f"{E('ok')} {sc('Checking first')} <b>{allowed}</b> {sc('of')} <b>{total}</b>"]),
            reply_markup=None if allowed == BULK_MAX else kb([btn('Buy Premium', 'pay', style='primary', callback_data='buy')]))
        B = B[:allowed]
    if not _acquire(C):
        return notice(C, f"{E('warn')} {sc('Your previous check is still running, please wait.')}", ttl=6)
    threading.Thread(target=_bulk_job, args=(C, B), daemon=True).start()
    if D:
        notice(C, "\n".join([bq(f"{E('warn')} {sc('Invalid skipped')}"), ""] + [f"• {esc(a)}" for a in D]), ttl=20)

# ─────────────────────────── admin screens ─────────────────────────────────
def admin_text():
    return "\n".join([bq(f"{E('admin')} {sc('Admin panel')}"), "",
                      row('pay', 'Pending Payments', pending_payments())])

def admin_kb():
    return kb(
        [btn('Statistics', 'stats', callback_data='astats'), btn('Users', 'user', callback_data='ausers')],
        [btn('Premium Users', 'star', callback_data='apremium'), btn('Broadcast', 'channel', callback_data='abroadcast')],
        [btn('Export Users', 'group', callback_data='aexport'), btn('Ban / Unban', 'ban', style='danger', callback_data='aban')],
        [btn('User Info', 'id', callback_data='auserinfo'), btn('Message One User', 'mail', callback_data='amsg')],
        [btn('Check Report', 'stats', style='primary', callback_data='acheck')],
        [btn('Backup Now', 'box', callback_data='abackup'), btn('Restore Backup', 'lock', style='danger', callback_data='arestore')],
        [btn('Create Token', 'lock', callback_data='atoken'), btn('Tokens', 'box', callback_data='atokens')],
        [btn('Tasks', 'pin', callback_data='atasks')],
        [btn('Main Menu', 'home', callback_data='back_menu')])

def _admin_stats_text():
    day0 = _now() - (_now() + 19800) % 86400
    with db() as con:
        total = con.execute("SELECT COUNT(*) n FROM users").fetchone()['n']
        active = con.execute("SELECT COUNT(*) n FROM users WHERE last_seen>=?", (_now() - 7 * 86400,)).fetchone()['n']
        prem = con.execute("SELECT COUNT(*) n FROM premium WHERE expires_at>?", (_now(),)).fetchone()['n']
        banned = con.execute("SELECT COUNT(*) n FROM users WHERE banned=1").fetchone()['n']
        joined = con.execute("SELECT COUNT(*) n FROM users WHERE joined_at>=?", (day0,)).fetchone()['n']
        checks = con.execute("SELECT COALESCE(SUM(count),0) n FROM usage_daily WHERE day=?", (_today(),)).fetchone()['n']
        rev = con.execute("SELECT COALESCE(SUM(amount),0) n FROM payments WHERE status='approved'").fetchone()['n']
    return "\n".join([
        bq(f"{E('stats')} {sc('Admin statistics')}"), "",
        row('group', 'Total Users', total), row('bolt', 'Active 7 Days', active),
        row('star', 'Premium Users', prem), row('ban', 'Banned Users', banned),
        row('title', 'Joined Today', joined), row('mail', 'Checks Today', checks),
        row('money', 'Revenue', f"₹{rev}"), row('pay', 'Pending Payments', pending_payments())])

def _restore_prompt():
    return "\n".join([bq(f"{E('lock')} {sc('Restore backup')}"), "",
        f"{E('pin')} {sc('Send the backup file (erebus_backup_*.sqlite3) as a document now.')}",
        f"{E('warn')} {sc('This replaces the current database. A safety copy is kept on the server.')}",
        sc('Send /cancel to stop.')])

def _admin_help_text():
    return "\n".join([bq(f"{E('id')} {sc('Admin commands')}"), "",
        "<code>/userinfo @username</code>",
        "<code>/premium @username days [p100|p200|unl]</code>",
        "<code>/removepremium @username</code>",
        "<code>/setlimit @username number|default</code>",
        "<code>/msg @username your message</code>",
        "<code>/ban @username</code>  <code>/unban @username</code>",
        "<code>/users</code>  <code>/stats</code>  <code>/admin</code>",
        "<code>/backup</code>  <code>/restore</code>",
        "<code>/token [CODE] checks max_users [days]</code>",
        "<code>/tokens</code>  <code>/deltoken CODE</code>  <code>/tasks</code>",
        "<code>/givechecks @username number</code>"])

def _userinfo_text(r):
    uid = r['user_id']; key, exp = plan_info(uid)
    return "\n".join([
        bq(f"{E('user')} {sc('User info')}"), "",
        row('user', 'Name', esc(r['name'] or '-') + (f" (@{esc(r['username'])})" if r['username'] else '')),
        row('id', 'ID', f"<code>{uid}</code>"),
        row('star', 'Plan', sc(PLANS[key]['name']) + f" ({_dshort(exp)})" if key else sc('Free')),
        row('mail', 'Today', _lim_txt(uid)), row('box', 'Total Checks', total_checks(uid)),
        row('calendar', 'Joined', _fmt(r['joined_at'])), row('time', 'Last Seen', _fmt(r['last_seen'])),
        row('ban', 'Banned', sc('Yes') if r['banned'] else sc('No'))])

# ─────────────────────────── payments ──────────────────────────────────────
def _pay_caption(pid, verdict=''):
    with db() as con:
        p = con.execute("SELECT * FROM payments WHERE id=?", (pid,)).fetchone()
        u = con.execute("SELECT * FROM users WHERE user_id=?", (p['user_id'],)).fetchone()
    handle = f"@{u['username']}" if u and u['username'] else 'no username'
    t = "\n".join([
        bq(f"{E('pay')} {sc('New payment request')} #{pid}"), "",
        row('user', 'User', f"{esc(u['name'] if u else '')} ({esc(handle)})"),
        row('id', 'ID', f"<code>{p['user_id']}</code>"),
        row('box', 'Plan', sc(PLANS[p['plan']]['name']) + f" ({p['days']} {sc('days')})"),
        row('money', 'Amount', f"₹{p['amount']}"), SEP,
        verdict or sc('Check the screenshot, then approve or reject.')])
    return t

def _pay_submit(uid, chat, m, st):
    key = st['plan']; p = PLANS[key]; fid = m['photo'][-1]['file_id']
    with db() as con:
        pid = con.execute("INSERT INTO payments(user_id,plan,days,amount,file_id,status,created_at) VALUES(?,?,?,?,?,'pending',?)",
                          (uid, key, p['days'], p['price'], fid, _now())).lastrowid
    STATE.pop(uid, None)
    markup = kb([btn('Approve', 'ok', style='success', callback_data=f"payok:{pid}"),
                 btn('Reject', 'err', style='danger', callback_data=f"payno:{pid}")])
    fwd = send_photo(OWNER_ID, fid, _pay_caption(pid), markup) if OWNER_ID else None
    log_photo(fid, _plainify(_pay_caption(pid)))
    sweep(chat)
    if fwd: tidy(chat, m['message_id'])
    send_message(chat, "\n".join([
        bq(f"{E('ok')} {sc('Screenshot received')}"), "",
        row('pin', 'Payment', f"#{pid}"), row('time', 'Status', sc('Waiting for approval')), SEP,
        f"{E('bell')} {sc('You will get a message here as soon as it is approved.')}"]),
        reply_markup=back_kb())

def notify_premium(uid, key, expiry):
    lim = PLANS[key]['limit']
    t = "\n".join([bq(f"{E('party')} {sc('Congratulations!')}"),
                   head('star', 'Premium Activated', ' ❗️'), "",
                   row('box', 'Plan', sc(PLANS[key]['name'])),
                   row('calendar', 'Valid Till', _fmt(expiry)),
                   row('bolt', 'Daily Limit', sc('Unlimited') if lim is None else lim)])
    return bool(send_message(uid, t, reply_markup=back_kb()))

def _review(cb, approve):
    uid = cb['from']['id']
    if not is_admin(uid): return answer_callback(cb['id'], 'Not allowed.', True)
    pid = int(cb['data'].split(':')[1]); status = 'approved' if approve else 'rejected'
    with db() as con:
        done = con.execute("UPDATE payments SET status=?, reviewed_at=? WHERE id=? AND status='pending'",
                           (status, _now(), pid)).rowcount
        p = con.execute("SELECT * FROM payments WHERE id=?", (pid,)).fetchone()
    if not done or not p: return answer_callback(cb['id'], 'Already reviewed.', True)
    target = p['user_id']
    if approve:
        exp = grant(target, p['plan']); ok = notify_premium(target, p['plan'], exp)
        verdict = f"{E('ok')} <b>{sc('Approved')}</b> — {sc('until')} {_dshort(exp)}"
        log(f"{P('ok')} <b>{sc('Payment approved')}</b> #{pid}\n{_utag_id(target)}\n"
            f"{sc(PLANS[p['plan']]['name'])} · ₹{p['amount']} · {sc('until')} {_dshort(exp)}")
        threading.Thread(target=backup_now, args=('payment',), daemon=True).start()
    else:
        ok = bool(send_message(target, "\n".join([
            bq(f"{E('err')} {sc('Payment rejected')}"), "", sc('Your payment could not be verified.'),
            f"{sc('If you think this is a mistake, contact')} @Noxmirage"]), reply_markup=back_kb()))
        verdict = f"{E('err')} <b>{sc('Rejected')}</b>"
        log(f"{P('err')} <b>{sc('Payment rejected')}</b> #{pid}\n{_utag_id(target)}")
    if not ok: verdict += f"\n{E('warn')} {sc('User could not be notified.')}"
    msg = cb.get('message') or {}
    _call('editMessageCaption', {'chat_id': msg['chat']['id'], 'message_id': msg['message_id'],
          'caption': _pay_caption(pid, verdict), 'parse_mode': 'HTML',
          'reply_markup': json.dumps({'inline_keyboard': []})})
    answer_callback(cb['id'], 'Done.')

# ─────────────────────────── broadcast ─────────────────────────────────────
def _broadcast_job(admin_chat, src, status_mid):
    with db() as con: ids = [r['user_id'] for r in con.execute("SELECT user_id FROM users WHERE banned=0")]
    sent = failed = 0; n = len(ids)
    for i, u in enumerate(ids, 1):
        ok = False
        for _t in range(3):
            r = _call('copyMessage', {'chat_id': u, 'from_chat_id': src[0], 'message_id': src[1]})
            if r.get('ok'): ok = True; break
            ra = (r.get('parameters') or {}).get('retry_after')
            if ra: time.sleep(min(int(ra), 30)); continue
            break
        sent += ok; failed += (not ok)
        if i % 25 == 0 and status_mid:
            edit_message(admin_chat, status_mid, f"{E('spin')} {sc('Broadcasting')} {i}/{n}")
        time.sleep(0.05)
    with db() as con:
        con.execute("INSERT INTO broadcasts(admin_id,sent,failed,created_at) VALUES(?,?,?,?)", (OWNER_ID, sent, failed, _now()))
    rep = "\n".join([head('ok', 'Broadcast Finished', ' ❗️'), "", row('ok', 'Delivered', sent),
                     row('err', 'Failed', failed), row('group', 'Total', n)])
    if status_mid: _edit_raw(admin_chat, status_mid, rep, back_kb())
    else: send_message(admin_chat, rep, reply_markup=back_kb())
    _del(*src)
    log(f"{P('channel')} <b>{sc('Broadcast finished')}</b>\n{P('ok')} {sent} · {P('err')} {failed} · {P('group')} {n}")

# ─────────────────────────── update interceptor ────────────────────────────
STATE = {}      # uid -> {'k': ...}   multi-step flows (payment screenshot, broadcast, message one user)

# ═══════════ FREE CHECKS: redeem tokens · referrals · tasks ═══════════
import secrets as _secrets
REF_BONUS = 40          # bonus checks the referrer gets for every new user who joins via their link
_BOT_USER = {}
_RFAIL = {}             # uid -> timestamps of wrong redeem codes

def bot_username():
    if not _BOT_USER.get('n'):
        r = _call('getMe'); _BOT_USER['n'] = (r.get('result') or {}).get('username') or ''
    return _BOT_USER['n']

def _ref_link(uid):
    u = bot_username()
    return f"https://t.me/{u}?start=ref_{uid}" if u else ''

def _go_free_kb(*top):
    return kb(*top, [btn('Free Checks', 'party', callback_data='free')], [btn('Main Menu', 'home', callback_data='back_menu')])

def free_text(uid):
    r = get_user(uid)
    return "\n".join([
        bq(f"{E('party')} {sc('Free checks')}"), "",
        row('bolt', 'Bonus Balance', bonus_of(uid)),
        row('group', 'Referrals', int(r['ref_count'] or 0) if r else 0), SEP,
        f"{E('bolt')} {sc('Redeem')} ➛ {sc('use a token code')}",
        f"{E('group')} {sc('Refer')} ➛ +{REF_BONUS} {sc('checks per friend')}",
        f"{E('pin')} {sc('Tasks')} ➛ {sc('complete tasks, earn checks')}",
        "", f"{E('star')} {sc('Bonus checks are used after your daily checks.')}"])

def free_kb():
    return kb([btn('Redeem Code', 'bolt', callback_data='redeem'), btn('Refer & Earn', 'group', callback_data='refer')],
              [btn('Tasks', 'pin', callback_data='tasks')],
              [btn('Main Menu', 'home', callback_data='back_menu')])

def redeem_prompt():
    return "\n".join([bq(f"{E('bolt')} {sc('Redeem code')}"), "",
                      f"{E('pin')} {sc('Send your token code now.')}", sc('Send /cancel to stop.')])

def _redeem_locked(uid):
    now = time.time(); l = [t for t in _RFAIL.get(uid, []) if now - t < 600]; _RFAIL[uid] = l
    return len(l) >= 5

def redeem_token(uid, code):
    """-> ('ok', checks) | ('invalid'|'expired'|'used'|'exhausted', None). One transaction."""
    code = (code or '').strip().upper()
    with db() as con:
        t = con.execute("SELECT * FROM tokens WHERE code=? AND active=1", (code,)).fetchone()
        if not t: return 'invalid', None
        if t['expires_at'] and t['expires_at'] < _now(): return 'expired', None
        if con.execute("SELECT 1 FROM token_uses WHERE code=? AND user_id=?", (code, uid)).fetchone(): return 'used', None
        if con.execute("UPDATE tokens SET used=used+1 WHERE code=? AND used<max_uses", (code,)).rowcount == 0:
            return 'exhausted', None
        con.execute("INSERT INTO token_uses(code,user_id,used_at) VALUES(?,?,?)", (code, uid, _now()))
        con.execute("UPDATE users SET bonus=COALESCE(bonus,0)+? WHERE user_id=?", (t['checks'], uid))
    return 'ok', t['checks']

def create_token(a):
    """args: [CODE] checks max_uses [days]  -> (code, err)"""
    a = list(a); code = None
    if a and not a[0].isdigit():
        code = _re.sub(r'[^A-Za-z0-9_-]', '', a[0]).upper()[:24]; a = a[1:]
        if len(code) < 3: return None, 'format'
    if len(a) not in (2, 3) or not all(x.isdigit() for x in a): return None, 'format'
    checks, maxu = int(a[0]), int(a[1]); days = int(a[2]) if len(a) == 3 else 0
    if checks < 1 or maxu < 1: return None, 'format'
    if not code: code = 'ER' + _secrets.token_hex(3).upper()
    with db() as con:
        if con.execute("SELECT 1 FROM tokens WHERE code=?", (code,)).fetchone(): return None, 'exists'
        con.execute("INSERT INTO tokens(code,checks,max_uses,used,expires_at,created_at,active) VALUES(?,?,?,0,?,?,1)",
                    (code, checks, maxu, _now() + days * 86400 if days else None, _now()))
    return code, ''

def token_created_text(code):
    with db() as con: t = con.execute("SELECT * FROM tokens WHERE code=?", (code,)).fetchone()
    return "\n".join([bq(f"{E('ok')} {sc('Token created')}"), "",
        row('lock', 'Code', f"<code>{esc(code)}</code>"), row('bolt', 'Checks', t['checks']),
        row('group', 'Max Users', t['max_uses']),
        row('calendar', 'Expires', _dshort(t['expires_at']) if t['expires_at'] else sc('Never'))])

def admin_tokens_screen():
    with db() as con:
        ts = con.execute("SELECT * FROM tokens WHERE active=1 ORDER BY created_at DESC LIMIT 12").fetchall()
    lines = [bq(f"{E('lock')} {sc('Tokens')}"), ""]
    if not ts: lines.append(sc('No active tokens.'))
    for t in ts:
        exp = _dshort(t['expires_at']) if t['expires_at'] else sc('Never')
        lines.append(f"<code>{esc(t['code'])}</code> ➛ {t['checks']} {sc('checks')} · {t['used']}/{t['max_uses']} · {exp}")
    rows = [[btn(f"Delete {t['code']}", 'err', style='danger', callback_data=f"tokdel:{t['code']}")] for t in ts[:8]]
    rows += [[btn('Create Token', 'ok', style='success', callback_data='atoken')], [btn('Admin Panel', 'admin', callback_data='admin')]]
    return "\n".join(lines), kb(*rows)

def token_prompt():
    return "\n".join([bq(f"{E('lock')} {sc('Create token')}"), "",
        f"{E('pin')} {sc('Send')}: <code>checks max_users [days]</code>",
        f"{sc('Example')}: <code>50 10 7</code> ({sc('50 checks, 10 users, valid 7 days')})",
        f"{sc('Custom code')}: <code>PROMO 50 10</code>", sc('Send /cancel to stop.')])

def refer_text(uid):
    r = get_user(uid); link = _ref_link(uid)
    lines = [bq(f"{E('group')} {sc('Refer & earn')}"), "",
             row('bolt', 'Per Referral', f"+{REF_BONUS} {sc('checks')}"),
             row('group', 'Referred', int(r['ref_count'] or 0) if r else 0),
             row('star', 'Bonus Balance', bonus_of(uid)), SEP]
    if link: lines += [f"{E('link')} {sc('Your link')}", f"<code>{esc(link)}</code>", "",
                       f"{E('pin')} {sc('You get the bonus when a NEW user starts the bot with your link.')}"]
    else:    lines.append(f"{E('warn')} {sc('Link is unavailable right now, try again later.')}")
    return "\n".join(lines)

def refer_kb(uid):
    link = _ref_link(uid); rows = []
    if link:
        share = "https://t.me/share/url?url=" + _quote(link) + "&text=" + _quote("Check Hi2 mail availability free!")
        rows.append([btn('Share Link', 'channel', url=share)])
    rows.append([btn('Back', 'home', callback_data='free')])
    return kb(*rows)

# ── tasks ──
def task_status(uid, tid):
    with db() as con:
        r = con.execute("SELECT status FROM task_subs WHERE task_id=? AND user_id=? ORDER BY "
                        "CASE status WHEN 'approved' THEN 0 WHEN 'pending' THEN 1 ELSE 2 END, id DESC LIMIT 1", (tid, uid)).fetchone()
    return r['status'] if r else None

def tasks_screen(uid):
    with db() as con: ts = con.execute("SELECT * FROM tasks WHERE active=1 ORDER BY id DESC LIMIT 20").fetchall()
    lines = [bq(f"{E('pin')} {sc('Tasks')}"), "", row('bolt', 'Bonus Balance', bonus_of(uid)), SEP]
    if not ts: lines.append(sc('No tasks right now. Check back soon!'))
    else: lines.append(f"{E('pin')} {sc('Pick a task, finish it and send a screenshot as proof.')}")
    rows = []
    for t in ts:
        mark = {'approved': '✅ ', 'pending': '⏳ '}.get(task_status(uid, t['id']), '')
        rows.append([btn(f"{mark}{t['title']} (+{t['reward']})", 'pin', callback_data=f"task:{t['id']}")])
    rows.append([btn('Back', 'home', callback_data='free')])
    return "\n".join(lines), kb(*rows)

def task_detail(uid, tid):
    with db() as con: t = con.execute("SELECT * FROM tasks WHERE id=? AND active=1", (tid,)).fetchone()
    if not t: return None, None
    st = task_status(uid, tid)
    stline = {'approved': f"{E('ok')} {sc('Completed')}", 'pending': f"{E('time')} {sc('Waiting for approval')}"}.get(st, '')
    text = "\n".join([bq(f"{E('pin')} {sc('Task')}"), "", row('pin', 'Title', esc(t['title'])),
                      row('bolt', 'Reward', f"+{t['reward']} {sc('checks')}"), SEP, esc(t['description'])]
                     + (["", stline] if stline else []))
    rows = []
    if st not in ('approved', 'pending'):
        rows.append([btn('Submit Proof', 'camera', style='success', callback_data=f"tsub:{tid}")])
    rows.append([btn('Back To Tasks', 'home', callback_data='tasks')])
    return text, kb(*rows)

def _task_caption(sid, verdict=''):
    with db() as con:
        s = con.execute("SELECT * FROM task_subs WHERE id=?", (sid,)).fetchone()
        t = con.execute("SELECT * FROM tasks WHERE id=?", (s['task_id'],)).fetchone()
        u = con.execute("SELECT * FROM users WHERE user_id=?", (s['user_id'],)).fetchone()
    handle = f"@{u['username']}" if u and u['username'] else 'no username'
    return "\n".join([bq(f"{E('pin')} {sc('Task proof')} #{sid}"), "",
        row('user', 'User', f"{esc(u['name'] if u else '')} ({esc(handle)})"),
        row('id', 'ID', f"<code>{s['user_id']}</code>"),
        row('pin', 'Task', esc(t['title'] if t else '?')),
        row('bolt', 'Reward', f"+{t['reward'] if t else 0} {sc('checks')}"), SEP,
        verdict or sc('Check the screenshot, then approve or reject.')])

def _task_submit(uid, chat, m, st):
    tid = st['task']; fid = m['photo'][-1]['file_id']
    with db() as con: t = con.execute("SELECT * FROM tasks WHERE id=? AND active=1", (tid,)).fetchone()
    if not t:
        STATE.pop(uid, None); tidy(chat, m['message_id'])
        return notice(chat, f"{E('err')} {sc('This task is no longer available.')}", ttl=8)
    if task_status(uid, tid) in ('approved', 'pending'):
        STATE.pop(uid, None); tidy(chat, m['message_id'])
        return notice(chat, f"{E('warn')} {sc('You already submitted this task.')}", ttl=8)
    with db() as con:
        sid = con.execute("INSERT INTO task_subs(task_id,user_id,file_id,status,created_at) VALUES(?,?,?,'pending',?)",
                          (tid, uid, fid, _now())).lastrowid
    STATE.pop(uid, None)
    markup = kb([btn('Approve', 'ok', style='success', callback_data=f"tkok:{sid}"),
                 btn('Reject', 'err', style='danger', callback_data=f"tkno:{sid}")])
    fwd = send_photo(OWNER_ID, fid, _task_caption(sid), markup) if OWNER_ID else None
    log_photo(fid, _plainify(_task_caption(sid)))
    sweep(chat)
    if fwd: tidy(chat, m['message_id'])
    send_message(chat, "\n".join([bq(f"{E('ok')} {sc('Proof received')}"), "",
        row('pin', 'Task', esc(t['title'])), row('time', 'Status', sc('Waiting for approval')), SEP,
        f"{E('bell')} {sc('You will get your checks here as soon as it is approved.')}"]),
        reply_markup=kb([btn('Tasks', 'pin', callback_data='tasks')], [btn('Main Menu', 'home', callback_data='back_menu')]))

def _review_task(cb, approve):
    uid = cb['from']['id']
    if not is_admin(uid): return answer_callback(cb['id'], 'Not allowed.', True)
    sid = int(cb['data'].split(':')[1]); dup = False
    with db() as con:
        s = con.execute("SELECT * FROM task_subs WHERE id=?", (sid,)).fetchone()
        t = con.execute("SELECT * FROM tasks WHERE id=?", (s['task_id'],)).fetchone() if s else None
        if s and approve and con.execute("SELECT 1 FROM task_subs WHERE task_id=? AND user_id=? AND status='approved' AND id!=?",
                                         (s['task_id'], s['user_id'], sid)).fetchone():
            dup = True
        status = 'approved' if (approve and not dup) else 'rejected'
        done = con.execute("UPDATE task_subs SET status=?, reviewed_at=? WHERE id=? AND status='pending'",
                           (status, _now(), sid)).rowcount if s else 0
        if done and status == 'approved':
            con.execute("UPDATE users SET bonus=COALESCE(bonus,0)+? WHERE user_id=?", (t['reward'], s['user_id']))
    if not done: return answer_callback(cb['id'], 'Already reviewed.', True)
    target = s['user_id']
    if status == 'approved':
        ok = bool(send_message(target, "\n".join([bq(f"{E('party')} {sc('Task approved!')}"), "",
            row('pin', 'Task', esc(t['title'])), row('bolt', 'You Got', f"+{t['reward']} {sc('checks')}"),
            row('star', 'Bonus Balance', bonus_of(target))]), reply_markup=_go_free_kb()))
        verdict = f"{E('ok')} <b>{sc('Approved')}</b> — +{t['reward']} {sc('checks')}"
    else:
        ok = bool(send_message(target, "\n".join([bq(f"{E('err')} {sc('Task proof rejected')}"), "",
            row('pin', 'Task', esc(t['title'] if t else '?')),
            sc('Your proof could not be verified. You can submit it again.')]), reply_markup=_go_free_kb()))
        verdict = f"{E('err')} <b>{sc('Rejected')}</b>" + (f" ({sc('already rewarded')})" if dup else '')
    log(f"{P('ok') if status == 'approved' else P('err')} <b>{sc('Task ' + status)}</b> #{sid}\n{_utag_id(target)}")
    if not ok: verdict += f"\n{E('warn')} {sc('User could not be notified.')}"
    msg = cb.get('message') or {}
    _call('editMessageCaption', {'chat_id': msg['chat']['id'], 'message_id': msg['message_id'],
          'caption': _plainify(_task_caption(sid, verdict)), 'parse_mode': 'HTML',
          'reply_markup': json.dumps({'inline_keyboard': []})})
    answer_callback(cb['id'], 'Done.')

def admin_tasks_screen():
    with db() as con: ts = con.execute("SELECT * FROM tasks WHERE active=1 ORDER BY id DESC LIMIT 15").fetchall()
    with db() as con: pend = con.execute("SELECT COUNT(*) n FROM task_subs WHERE status='pending'").fetchone()['n']
    lines = [bq(f"{E('pin')} {sc('Tasks')}"), "", row('time', 'Pending Proofs', pend), SEP]
    if not ts: lines.append(sc('No active tasks.'))
    for t in ts: lines.append(f"#{t['id']} <b>{esc(t['title'])}</b> ➛ +{t['reward']} {sc('checks')}")
    rows = [[btn(f"Delete #{t['id']} {t['title'][:20]}", 'err', style='danger', callback_data=f"tkdel:{t['id']}")] for t in ts]
    rows += [[btn('Add Task', 'ok', style='success', callback_data='atkadd')], [btn('Admin Panel', 'admin', callback_data='admin')]]
    return "\n".join(lines), kb(*rows)

def _resolve_msg(uid_token):
    r = find_user(uid_token); return r

def _admin_command(uid, chat, m, text):
    parts = text.split(); cmd = parts[0].split('@')[0].lower(); a = parts[1:]
    tidy(chat, m['message_id'])
    usage = lambda s: notice(chat, "Usage: <code>" + s + "</code>", ttl=10)
    nf = lambda: notice(chat, f"{E('warn')} {sc('User not found. They must have started the bot.')}", ttl=8)
    if cmd == '/admin':
        show_panel(chat, admin_text(), admin_kb()); return True
    if cmd == '/stats':
        notice(chat, _admin_stats_text(), ttl=30); return True
    if cmd == '/backup':
        threading.Thread(target=backup_now, args=('manual', chat), daemon=True).start()
        notice(chat, f"{E('ok')} {sc('Backup is being sent.')}", ttl=6); return True
    if cmd == '/restore':
        STATE[uid] = {'k': 'restore'}
        remember(chat, send_message(chat, _restore_prompt())); return True
    if cmd == '/token':
        code, err = create_token(a)
        if code: notice(chat, token_created_text(code), ttl=60)
        elif err == 'exists': notice(chat, f"{E('warn')} {sc('That code already exists.')}", ttl=8)
        else: usage('/token [CODE] checks max_users [days]')
        return True
    if cmd == '/tokens':
        t_, k_ = admin_tokens_screen(); show_panel(chat, t_, k_); return True
    if cmd == '/deltoken':
        if len(a) != 1: usage('/deltoken CODE'); return True
        with db() as con: n = con.execute("UPDATE tokens SET active=0 WHERE code=?", (a[0].upper(),)).rowcount
        notice(chat, f"{E('ok')} {sc('Token deleted.')}" if n else f"{E('warn')} {sc('Token not found.')}", ttl=8); return True
    if cmd == '/tasks':
        t_, k_ = admin_tasks_screen(); show_panel(chat, t_, k_); return True
    if cmd == '/givechecks':
        if len(a) != 2 or not a[1].isdigit() or int(a[1]) < 1: usage('/givechecks @username number'); return True
        r = find_user(a[0])
        if not r: nf(); return True
        with db() as con: con.execute("UPDATE users SET bonus=COALESCE(bonus,0)+? WHERE user_id=?", (int(a[1]), r['user_id']))
        send_message(r['user_id'], "\n".join([bq(f"{E('party')} {sc('Bonus checks added!')}"), "",
            row('bolt', 'You Got', f"+{a[1]} {sc('checks')}"), row('star', 'Bonus Balance', bonus_of(r['user_id']))]),
            reply_markup=back_kb())
        notice(chat, f"{E('ok')} +{a[1]} {sc('checks for')} {esc(_label(r))}", ttl=10); return True
    if cmd == '/users':
        export_users(chat); return True
    if cmd == '/userinfo':
        if len(a) != 1: usage('/userinfo @username'); return True
        r = find_user(a[0]); notice(chat, _userinfo_text(r), ttl=30) if r else nf(); return True
    if cmd == '/premium':
        if len(a) not in (2, 3) or not a[1].isdigit() or int(a[1]) < 1 or (len(a) == 3 and a[2] not in PLANS):
            usage('/premium @username days [p100|p200|unl]'); return True
        r = find_user(a[0])
        if not r: nf(); return True
        key = a[2] if len(a) == 3 else 'unl'
        exp = grant(r['user_id'], key, int(a[1]), extend=False); ok = notify_premium(r['user_id'], key, exp)
        notice(chat, f"{E('star')} {sc('Premium granted to')} {esc(_label(r))} {sc('until')} {_dshort(exp)} ❗️\n"
               + (f"{E('bell')} {sc('User has been notified.')}" if ok else f"{E('warn')} {sc('Could not notify the user.')}"), ttl=15)
        log(f"{P('star')} <b>{sc('Premium granted')}</b>\n{_utag_id(r['user_id'])}\n{sc(PLANS[key]['name'])} · {sc('until')} {_dshort(exp)}")
        return True
    if cmd == '/removepremium':
        r = find_user(a[0]) if len(a) == 1 else None
        if len(a) != 1: usage('/removepremium @username'); return True
        if not r: nf(); return True
        with db() as con: con.execute("DELETE FROM premium WHERE user_id=?", (r['user_id'],))
        notice(chat, f"{E('ok')} {sc('Premium removed for')} {esc(_label(r))}", ttl=10); return True
    if cmd == '/setlimit':
        if len(a) != 2 or not (a[1].isdigit() or a[1].lower() == 'default'): usage('/setlimit @username number|default'); return True
        r = find_user(a[0])
        if not r: nf(); return True
        v = None if a[1].lower() == 'default' else int(a[1])
        with db() as con: con.execute("UPDATE users SET custom_limit=? WHERE user_id=?", (v, r['user_id']))
        notice(chat, f"{E('ok')} {sc('Daily limit for')} {esc(_label(r))} ➛ {f'{v}/day' if v is not None else f'default ({FREE_DAILY}/day)'}", ttl=10); return True
    if cmd in ('/ban', '/unban'):
        if len(a) != 1: usage(cmd + ' @username'); return True
        r = find_user(a[0])
        if not r: nf(); return True
        if is_admin(r['user_id']): notice(chat, f"{E('warn')} {sc('You cannot ban an admin.')}", ttl=6); return True
        with db() as con: con.execute("UPDATE users SET banned=? WHERE user_id=?", (1 if cmd == '/ban' else 0, r['user_id']))
        notice(chat, f"{E('ok')} {esc(_label(r))} ➛ {sc('banned') if cmd == '/ban' else sc('unbanned')}", ttl=10)
        log(f"{P('ban')} <b>{sc('Banned') if cmd == '/ban' else sc('Unbanned')}</b>\n{_utag_id(r['user_id'])}"); return True
    if cmd == '/msg':
        p3 = text.split(maxsplit=2)
        if len(p3) != 3: usage('/msg @username your message'); return True
        r = find_user(p3[1])
        if not r: nf(); return True
        ok = bool(send_message(r['user_id'], p3[2], parse_mode=None))
        notice(chat, (f"{E('ok')} {sc('Message delivered to')} " if ok else f"{E('err')} {sc('Could not deliver to')} ") + esc(_label(r)), ttl=10)
        return True
    return False

def _handle_state_message(uid, chat, m, st):
    k = st['k']; text = (m.get('text') or '').strip(); mid = m['message_id']
    if k == 'shot':
        if m.get('photo'): _pay_submit(uid, chat, m, st)
        else:
            tidy(chat, mid)
            notice(chat, f"{E('warn')} {sc('Please send the screenshot as a photo, or /cancel to stop.')}", ttl=6)
    elif k == 'bc' and is_admin(uid):
        with db() as con: n = con.execute("SELECT COUNT(*) n FROM users WHERE banned=0").fetchone()['n']
        STATE[uid] = {'k': 'bcok', 'src': (chat, mid)}
        sweep(chat)
        remember(chat, send_message(chat, "\n".join([
            bq(f"{E('channel')} {sc('Confirm broadcast')}"), "",
            row('group', 'Recipients', n), SEP, sc('Send this message to every user?')]),
            reply_markup=kb([btn('Send', 'ok', style='success', callback_data='abc_go'),
                             btn('Cancel', 'err', style='danger', callback_data='abc_no')])))
    elif k == 'dm_t' and is_admin(uid):
        tidy(chat, mid)
        r = find_user(text) if text else None
        if not r: return notice(chat, f"{E('warn')} {sc('User not found. They must have started the bot. Try again or /cancel.')}", ttl=8)
        sweep(chat); STATE[uid] = {'k': 'dm_x', 'to': r['user_id'], 'label': _label(r)}
        remember(chat, send_message(chat, f"{E('pin')} {sc('Now send the message for')} {esc(_label(r))}"))
    elif k == 'dm_x' and is_admin(uid):
        tidy(chat, mid); STATE.pop(uid, None); sweep(chat)
        ok = bool(send_message(st['to'], text, parse_mode=None)) if text else False
        notice(chat, (f"{E('ok')} {sc('Message delivered to')} " if ok else f"{E('err')} {sc('Could not deliver to')} ") + esc(st['label']), ttl=10)
    elif k == 'restore' and is_admin(uid):
        doc = m.get('document'); tidy(chat, mid)
        if not doc:
            return notice(chat, f"{E('warn')} {sc('Send the backup file as a document, or /cancel to stop.')}", ttl=8)
        if (doc.get('file_size') or 0) > 20 * 1024 * 1024:
            return notice(chat, f"{E('err')} {sc('File is too big (max 20 MB).')}", ttl=8)
        STATE.pop(uid, None); sweep(chat)
        wait_mid = send_message(chat, f"{E('spin')} {sc('Restoring backup...')}")
        data = _download_file(doc['file_id'])
        ok, err = restore_from_bytes(data) if data else (False, 'Could not download the file.')
        if wait_mid: _del(chat, wait_mid)
        if ok:
            notice(chat, f"{E('ok')} <b>{sc('Backup restored')}</b>\n{sc('Users, premium, payments and logs were loaded.')}", ttl=20)
            log(f"{P('ok')} <b>{sc('Backup restored')}</b> ‣ {esc(doc.get('file_name') or '')}")
        else:
            notice(chat, f"{E('err')} {sc('Restore failed')}: {esc(err)}\n{sc('Your current data was not changed.')}", ttl=15)
    elif k == 'redeem':
        tidy(chat, mid)
        if not text: return
        if _redeem_locked(uid):
            return notice(chat, f"{E('ban')} {sc('Too many wrong codes. Try again in 10 minutes.')}", ttl=8)
        status, val = redeem_token(uid, text)
        if status == 'ok':
            STATE.pop(uid, None); _RFAIL.pop(uid, None)
            show_panel(chat, "\n".join([bq(f"{E('party')} {sc('Code redeemed!')}"), "",
                row('bolt', 'Added', f"+{val} {sc('checks')}"), row('star', 'Bonus Balance', bonus_of(uid))]), _go_free_kb())
        else:
            if status == 'invalid': _RFAIL.setdefault(uid, []).append(time.time())
            msg = {'invalid': 'This code is invalid.', 'expired': 'This code has expired.',
                   'used': 'You already used this code.', 'exhausted': 'This code has reached its limit.'}[status]
            notice(chat, f"{E('err')} {sc(msg)}\n{sc('Send another code or /cancel.')}", ttl=8)
    elif k == 'tshot':
        if m.get('photo'): _task_submit(uid, chat, m, st)
        else:
            tidy(chat, mid)
            notice(chat, f"{E('warn')} {sc('Please send the proof as a photo, or /cancel to stop.')}", ttl=6)
    elif k == 'tkn' and is_admin(uid):
        tidy(chat, mid); code, err = create_token(text.split())
        if not code:
            return notice(chat, f"{E('warn')} " + (sc('That code already exists.') if err == 'exists'
                          else sc('Wrong format. Example: 50 10 7')), ttl=8)
        STATE.pop(uid, None); sweep(chat)
        show_panel(chat, token_created_text(code), kb([btn('Tokens', 'lock', callback_data='atokens')],
                                                      [btn('Admin Panel', 'admin', callback_data='admin')]))
    elif k == 'tk_t' and is_admin(uid):
        tidy(chat, mid)
        if not text: return
        STATE[uid] = {'k': 'tk_d', 'title': text[:60]}; sweep(chat)
        remember(chat, send_message(chat, f"{E('pin')} {sc('Now send the task description (include the link).')}\n{sc('Send /cancel to stop.')}"))
    elif k == 'tk_d' and is_admin(uid):
        tidy(chat, mid)
        if not text: return
        STATE[uid] = {'k': 'tk_r', 'title': st['title'], 'desc': text[:800]}; sweep(chat)
        remember(chat, send_message(chat, f"{E('bolt')} {sc('How many checks should this task give? Send a number.')}"))
    elif k == 'tk_r' and is_admin(uid):
        tidy(chat, mid)
        if not text.isdigit() or int(text) < 1:
            return notice(chat, f"{E('warn')} {sc('Send a number like 25.')}", ttl=6)
        with db() as con:
            con.execute("INSERT INTO tasks(title,description,reward,active,created_at) VALUES(?,?,?,1,?)",
                        (st['title'], st['desc'], int(text), _now()))
        STATE.pop(uid, None); sweep(chat)
        t_, k_ = admin_tasks_screen(); show_panel(chat, t_, k_)
    # 'bcok' waits for the buttons; other messages are ignored

def _handle_callback(cb):
    frm = cb.get('from', {}); uid = frm.get('id'); data = cb.get('data', '') or ''
    msg = cb.get('message') or {}; chat = msg.get('chat', {}).get('id'); mid = msg.get('message_id')
    register(frm)
    if is_banned(uid) and not is_admin(uid):
        answer_callback(cb['id'], 'Access disabled.', True); return True
    if data in ('mode_single', 'mode_bulk', 'back_menu'):
        STATE.pop(uid, None)
        if chat: sweep(chat, keep=mid)
        if data == 'back_menu': _CB[chat] = (mid, bool(msg.get('photo')))
        return False                                   # run_bot handles these exactly as before
    admin_data = data in ('admin', 'astats', 'ausers', 'apremium', 'abroadcast', 'aexport', 'aban', 'auserinfo',
                          'amsg', 'abc_go', 'abc_no', 'acheck', 'abackup', 'arestore', 'atoken', 'atokens', 'atasks', 'atkadd') \
                 or data.startswith(('payok:', 'payno:', 'tkok:', 'tkno:', 'tkdel:', 'tokdel:'))
    if admin_data and not is_admin(uid):
        answer_callback(cb['id'], 'Not allowed.', True); return True
    if data.startswith('payok:') or data.startswith('payno:'):
        _review(cb, data.startswith('payok:')); return True
    if data.startswith(('tkok:', 'tkno:')):
        _review_task(cb, data.startswith('tkok:')); return True
    answer_callback(cb['id'])
    if data not in ('abc_go', 'abc_no'): STATE.pop(uid, None)      # leaving a screen cancels any open input step
    if data == 'buy':
        STATE.pop(uid, None); sweep(chat, keep=mid); safe_edit(cb, plans_text(), plans_kb())
    elif data.startswith('plan:') and data[5:] in PLANS:
        key = data[5:]; p = PLANS[key]; lim = sc('Unlimited') if p['limit'] is None else f"{p['limit']} / {sc('day')}"
        caption = "\n".join([
            bq(f"{E('pay')} {sc('Pay')} ₹{p['price']} ➛ {sc(p['name'])}"), "",
            row('bank', 'UPI ID', f"<code>{esc(UPI_ID)}</code>"), row('money', 'Amount', f"₹{p['price']}"),
            row('bolt', 'Limit', lim), row('calendar', 'Validity', f"{p['days']} {sc('days')}"), SEP,
            f"1️⃣ {sc('Scan this QR with any UPI app')}", f"2️⃣ {sc('Pay the exact amount')}",
            f"3️⃣ {sc('Tap the button below and send the screenshot')}"])
        markup = kb([btn("I've Paid — Send Screenshot", 'ok', style='success', callback_data=f"paid:{key}")],
                    [btn('Back To Plans', 'home', callback_data='buy')])
        sweep(chat)
        qr = make_qr(upi_link(p['price'], p['name']))
        if qr: sent = send_photo(chat, qr, caption, markup)
        else:  sent = send_message(chat, caption + f"\n\n{E('warn')} {sc('QR is unavailable, please pay to the UPI ID above.')}", reply_markup=markup)
        remember(chat, sent); _del(chat, mid)
    elif data.startswith('paid:') and data[5:] in PLANS:
        if pending_payments(uid) >= MAX_PENDING:
            return answer_callback(cb['id'], 'You already have pending payments. Please wait for approval.', True) or True
        STATE[uid] = {'k': 'shot', 'plan': data[5:]}
        remember(chat, send_message(chat, f"{E('camera')} {sc('Send your payment screenshot now as a photo.')}\n{sc('Send /cancel to stop.')}"))
    elif data == 'mypremium':
        t, has = _my_premium_text(uid)
        safe_edit(cb, t, back_kb([btn('Extend Premium' if has else 'Buy Premium', 'pay', style='primary', callback_data='buy')]))
    elif data == 'mystats':
        key, exp = plan_info(uid); r = get_user(uid)
        safe_edit(cb, "\n".join([bq(f"{E('stats')} {sc('Your statistics')}"), "",
            row('box', 'Total Checked', total_checks(uid)), row('mail', 'Today', _lim_txt(uid)),
            row('star', 'Plan', sc(PLANS[key]['name']) if key else sc('Free')),
            row('calendar', 'Joined', _dshort(r['joined_at']) if r else '-')]), back_kb())
    elif data == 'admin':   safe_edit(cb, admin_text(), admin_kb())
    elif data == 'astats':  safe_edit(cb, _admin_stats_text(), admin_kb())
    elif data == 'ausers':
        with db() as con:
            rs = con.execute("SELECT * FROM users ORDER BY joined_at DESC LIMIT 25").fetchall()
            n = con.execute("SELECT COUNT(*) n FROM users").fetchone()['n']
        lines = [bq(f"{E('group')} {sc('Latest 25 users')} ({n} {sc('total')})"), ""]
        lines += [f"{E('user')} {esc(_label(r))} ➛ <code>{r['user_id']}</code>" for r in rs]
        safe_edit(cb, "\n".join(lines), admin_kb())
    elif data == 'apremium':
        with db() as con:
            rs = con.execute("SELECT u.user_id,u.username,u.name,p.plan,p.expires_at FROM premium p JOIN users u ON u.user_id=p.user_id "
                             "WHERE p.expires_at>? ORDER BY p.expires_at", (_now(),)).fetchall()
        lines = [bq(f"{E('star')} {sc('Active premium users')}"), ""]
        if not rs: lines.append(sc('None yet.'))
        for r in rs[:40]:
            lines.append(f"{E('star')} {esc(_label(r))} ➛ {sc(PLANS[r['plan']]['name'])} · {_dshort(r['expires_at'])}")
        safe_edit(cb, "\n".join(lines), admin_kb())
    elif data == 'aexport':
        export_users(chat)
    elif data == 'acheck':
        safe_edit(cb, check_report_text(), kb([btn('Refresh', 'spin', callback_data='acheck')],
                                              [btn('Admin Panel', 'admin', callback_data='admin')]))
    elif data == 'abackup':
        threading.Thread(target=backup_now, args=('manual', chat), daemon=True).start()
        notice(chat, f"{E('ok')} {sc('Backup is being sent.')}", ttl=6)
    elif data == 'arestore':
        STATE[uid] = {'k': 'restore'}
        remember(chat, send_message(chat, _restore_prompt()))
    elif data == 'free':
        sweep(chat, keep=mid); safe_edit(cb, free_text(uid), free_kb())
    elif data == 'redeem':
        sweep(chat, keep=mid); STATE[uid] = {'k': 'redeem'}
        safe_edit(cb, redeem_prompt(), kb([btn('Back', 'home', callback_data='free')]))
    elif data == 'refer':
        safe_edit(cb, refer_text(uid), refer_kb(uid))
    elif data == 'tasks':
        sweep(chat, keep=mid); t_, k_ = tasks_screen(uid); safe_edit(cb, t_, k_)
    elif data.startswith('task:') and data[5:].isdigit():
        t_, k_ = task_detail(uid, int(data[5:]))
        if t_: safe_edit(cb, t_, k_)
        else: notice(chat, f"{E('err')} {sc('This task is no longer available.')}", ttl=6)
    elif data.startswith('tsub:') and data[5:].isdigit():
        tid = int(data[5:])
        if task_status(uid, tid) in ('approved', 'pending'):
            return answer_callback(cb['id'], 'You already submitted this task.', True) or True
        with db() as con: ok_t = con.execute("SELECT 1 FROM tasks WHERE id=? AND active=1", (tid,)).fetchone()
        if not ok_t: return answer_callback(cb['id'], 'Task is no longer available.', True) or True
        STATE[uid] = {'k': 'tshot', 'task': tid}
        remember(chat, send_message(chat, f"{E('camera')} {sc('Send your proof screenshot now as a photo.')}\n{sc('Send /cancel to stop.')}"))
    elif data == 'atoken':
        STATE[uid] = {'k': 'tkn'}; remember(chat, send_message(chat, token_prompt()))
    elif data == 'atokens':
        t_, k_ = admin_tokens_screen(); safe_edit(cb, t_, k_)
    elif data.startswith('tokdel:'):
        with db() as con: con.execute("UPDATE tokens SET active=0 WHERE code=?", (data[7:],))
        t_, k_ = admin_tokens_screen(); safe_edit(cb, t_, k_)
    elif data == 'atasks':
        t_, k_ = admin_tasks_screen(); safe_edit(cb, t_, k_)
    elif data == 'atkadd':
        STATE[uid] = {'k': 'tk_t'}
        remember(chat, send_message(chat, f"{E('pin')} {sc('Send the task title (example: Watch our video).')}\n{sc('Send /cancel to stop.')}"))
    elif data.startswith('tkdel:') and data[6:].isdigit():
        with db() as con: con.execute("UPDATE tasks SET active=0 WHERE id=?", (int(data[6:]),))
        t_, k_ = admin_tasks_screen(); safe_edit(cb, t_, k_)
    elif data == 'aban':
        safe_edit(cb, "\n".join([bq(f"{E('ban')} {sc('Ban / unban')}"), "", "<code>/ban @username</code>", "<code>/unban @username</code>"]), admin_kb())
    elif data == 'auserinfo':
        safe_edit(cb, _admin_help_text(), admin_kb())
    elif data == 'abroadcast':
        STATE[uid] = {'k': 'bc'}
        remember(chat, send_message(chat, f"{E('channel')} {sc('Send the message to broadcast to all users.')}\n"
                                          f"{sc('Text, photo or any media works.')} {sc('Send /cancel to stop.')}"))
    elif data == 'amsg':
        STATE[uid] = {'k': 'dm_t'}
        remember(chat, send_message(chat, f"{E('mail')} {sc('Send the @username or numeric ID of the person to message.')}\n{sc('Send /cancel to stop.')}"))
    elif data == 'abc_go':
        st = STATE.pop(uid, None)
        if not st or st.get('k') != 'bcok': return True
        sweep(chat)
        smid = send_message(chat, f"{E('spin')} {sc('Broadcasting...')}")
        threading.Thread(target=_broadcast_job, args=(chat, st['src'], smid), daemon=True).start()
    elif data == 'abc_no':
        st = STATE.pop(uid, None); sweep(chat)
        if st and st.get('src'): _del(*st['src'])
        notice(chat, f"{E('err')} {sc('Broadcast cancelled.')}", ttl=5)
    else:
        return False
    return True

def _handle_message(m):
    frm = m.get('from', {}); uid = frm.get('id'); chat = m.get('chat', {}).get('id')
    if not uid or m.get('chat', {}).get('type') != 'private': return True
    text = (m.get('text') or '').strip(); mid = m['message_id']
    ref = None
    if text.startswith('/start'):                 # /start ref_<userid>  (referral link)
        pp = text.split()
        if len(pp) > 1 and pp[1].startswith('ref_') and pp[1][4:].isdigit(): ref = int(pp[1][4:])
    register(frm, ref)
    if is_banned(uid) and not is_admin(uid):
        if text == '/start': tidy(chat, mid)
        notice(chat, f"{E('ban')} {sc('Your access has been disabled.')}", ttl=15); return True
    cmd = text.split()[0].split('@')[0].lower() if text.startswith('/') else ''
    if cmd in ('/start', '/help'):
        STATE.pop(uid, None); tidy(chat, mid); sweep(chat)
        if len(text.split()) > 1:                 # "/start payload" is not matched by run_bot -> show home here
            send_welcome(chat); return True
        return False                              # run_bot shows the home panel
    if cmd == '/cancel':
        st = STATE.pop(uid, None); tidy(chat, mid); sweep(chat)
        if st and st.get('src'): _del(*st['src'])
        if st:
            notice(chat, f"{E('err')} {sc('Cancelled.')}", ttl=5)
            if st['k'] == 'shot': send_welcome(chat)
        return True
    if cmd in ('/premium', '/buy', '/plan') and not (is_admin(uid) and len(text.split()) > 1):
        tidy(chat, mid); STATE.pop(uid, None); sweep(chat)
        old = _PANEL.pop(chat, None)
        if old: _del(chat, old)
        _PANEL[chat] = send_message(chat, plans_text(), reply_markup=plans_kb()); return True
    if cmd and is_admin(uid):
        if _admin_command(uid, chat, m, text): return True
    st = STATE.get(uid)
    if st: _handle_state_message(uid, chat, m, st); return True
    if m.get('photo') or m.get('document') or m.get('sticker'):
        tidy(chat, mid); return True
    if text and not cmd:
        with _tl: _LAST[chat] = mid           # processed (and tidied) by process_single / process_bulk
    return False

def _handle_extra(u):
    if 'callback_query' in u: return _handle_callback(u['callback_query'])
    if 'message' in u:        return _handle_message(u['message'])
    return False

def _poll(offset=None):
    """getUpdates that reports API errors instead of silently returning nothing."""
    try:
        r = requests.get(f"{API_URL}/getUpdates", params={'timeout': 25, 'offset': offset,
                         'allowed_updates': json.dumps(['message', 'callback_query'])}, timeout=35).json()
    except Exception as e:
        print(f"{spy28}[!] network: {e}{reset}"); time.sleep(2); return []
    if not r.get('ok'):
        print(f"{spy28}[!] getUpdates failed: {r.get('description')}{reset}")
        if r.get('error_code') == 409:
            print(f"{spy28}[!] ANOTHER copy of this bot is running with the same token - stop the old one.{reset}")
        time.sleep(3); return []
    return r.get('result', [])

_orig_get_updates = _poll
def get_updates(offset=None):
    keep = []
    for u in _orig_get_updates(offset):
        try:    consumed = _handle_extra(u)
        except Exception as e:
            print(f"{spy28}[!] ui error: {e}{reset}"); consumed = True
            if 'callback_query' in u: answer_callback(u['callback_query'].get('id'), 'Something went wrong, please try again.', True)
        keep.append({'update_id': u.get('update_id')} if consumed else u)
    return keep

init_db()
if LOG_CHANNEL:
    threading.Thread(target=_log_worker, daemon=True).start()
    threading.Thread(target=_backup_worker, daemon=True).start()
if not OWNER_ID:
    print(f"{spy28}[!] OWNER_ID not set - admin panel and payment approval are disabled{reset}")
if not LOG_CHANNEL:
    print(f"{spy28}[!] LOG_CHANNEL not set - channel logging is off{reset}")
if qrcode is None:
    print(f"{spy28}[!] qrcode missing (pip install \"qrcode[pil]\") - users will only see the UPI id{reset}")



run_bot()
