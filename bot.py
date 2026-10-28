import os
import sys
import time
import json
import random
import sqlite3
import requests
import threading

from datetime import datetime, timezone
from flask import Flask, send_from_directory
from threading import Thread
try:from colorama import Fore,Style,init;init()
except:os.system('pip install colorama');from colorama import Fore,Style,init




app = Flask(__name__)
# ==============================
# DATABASE CONFIGURATION
# ==============================

DATABASE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "bot_database.sqlite3"
)


def get_db():
    """Create a new SQLite connection."""
    connection = sqlite3.connect(
        DATABASE_PATH,
        timeout=30
    )

    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA busy_timeout = 30000")

    return connection


def init_database():
    """Create the database tables if they don't exist."""

    with get_db() as db:

        # Store registered Telegram users.
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                points INTEGER NOT NULL DEFAULT 0,
                referred_by INTEGER,
                joined_at TEXT NOT NULL,
                last_seen TEXT NOT NULL,
                start_count INTEGER NOT NULL DEFAULT 1,
                command_count INTEGER NOT NULL DEFAULT 0,
                is_blocked INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (referred_by)
                    REFERENCES users(user_id)
            )
        """)

        # Record point changes for future admin auditing.
        db.execute("""
            CREATE TABLE IF NOT EXISTS point_transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount INTEGER NOT NULL,
                reason TEXT NOT NULL,
                admin_id INTEGER,
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id)
                    REFERENCES users(user_id)
            )
        """)

        # Track successful referral rewards.
        db.execute("""
            CREATE TABLE IF NOT EXISTS referrals (
                referral_id INTEGER PRIMARY KEY AUTOINCREMENT,
                referrer_id INTEGER NOT NULL,
                referred_user_id INTEGER NOT NULL UNIQUE,
                reward INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                FOREIGN KEY (referrer_id)
                    REFERENCES users(user_id),
                FOREIGN KEY (referred_user_id)
                    REFERENCES users(user_id)
            )
        """)

    print("[DATABASE] Database initialized successfully.")


def current_timestamp():
    """Return the current UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()



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

BOT_TOKEN = os.environ.get("BOT_TOKEN")
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
def animate_check(chat_id,email,stop_event,frames_per_sec=1):
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
		if E not in SUPPORTED_DOMAINS:send_message(D,f"❌ <b>Iɴᴠᴀʟɪᴅ Dᴏᴍᴀɪɴ</b>\n\n<b>Pʟᴇᴀsᴇ Uꜱᴇ Oɴᴇ Oꜰ Tʜᴇ Sᴜᴘᴘᴏʀᴛᴇᴅ Dᴏᴍᴀɪɴs</b>\n<code>{', '.join(_D+A for A in SUPPORTED_DOMAINS)}</code>");return
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
			time.sleep(1)
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

init_database()
run_bot()

