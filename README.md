<div align="center">

# ✨ Erebus · Hi2 Mail Checker Bot 👾

**A Telegram bot that checks whether `@hi2.in` (and `@telegmail.com`) addresses are free or taken.**
Single & bulk checks · Daily limits · Premium plans · Referrals · Tokens · Tasks · Auto-backups · Admin panel

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-26A5E4?logo=telegram&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success)

*By Haze · [@Noxmirage](https://t.me/Noxmirage) · Channel: [@ErebusRedirect](https://t.me/linksfromerebus)*

</div>

---

## 📑 Table of contents

1. [Features](#-features)
2. [Quick start](#-quick-start)
3. [Configuration](#-configuration)
4. [How users use the bot](#-how-users-use-the-bot)
5. [Bulk checking & cooldowns](#-bulk-checking--cooldowns)
6. [Plans & limits](#-plans--limits)
7. [Free checks: Redeem · Referrals · Tasks](#-free-checks-redeem--referrals--tasks)
8. [Admin panel & commands](#-admin-panel--commands)
9. [Backups & restore](#-backups--restore)
10. [Project files](#-project-files)
11. [Troubleshooting](#-troubleshooting)
12. [Security notes](#-security-notes)

---

## 🌟 Features

| Area | What you get |
|---|---|
| 🔎 **Checking** | Single mode and bulk mode, live spinner, per-mail results (Taken / Free / Unknown) |
| ⏱ **Cooldowns** | Bulk runs are checked in chunks of 20 with a live countdown timer between chunks |
| 📊 **Limits** | Daily free limit, 100 / 200 / unlimited premium plans, resets at midnight IST |
| 💳 **Payments** | UPI QR code is generated in the bot, user sends a screenshot, admin approves with one tap |
| 🎁 **Free checks** | Redeem tokens, refer friends (+40 checks each), complete admin-made tasks with photo proof |
| 🛠 **Admin panel** | Statistics, users, premium users, broadcast, ban / unban, message one user, export users |
| 📈 **Check report** | Total checks, Taken / Free / Unknown, plus the latest 10 free mails from the last hour |
| 💾 **Backups** | Database sent to your log channel every 30 minutes, one-tap restore |
| 📝 **Logging** | New users, checks, payments, tasks, bans and backups are logged to a channel |
| 🎨 **UI** | Small-caps font, animated custom emojis (with automatic plain fallback), self-cleaning chat |

---

## 🚀 Quick start

### 1. Requirements

- Python **3.9 or newer**
- A bot token from [@BotFather](https://t.me/BotFather)
- (Optional) a private Telegram channel for logs and backups, with the bot added as **admin**

### 2. Install

```bash
pip install requests colorama "qrcode[pil]"
```

> The script also tries to install `colorama` and `qrcode` by itself on first run.

### 3. Configure

Open `FakeMailCheckerBotv2.py` and set the values listed in [Configuration](#-configuration):
at minimum `BOT_TOKEN`, `OWNER_ID`, and your log channel ID.

### 4. Run

```bash
python FakeMailCheckerBotv2.py
```

You should see the "Running" banner. Open your bot in Telegram and send `/start`.

> ⚠️ **Run only ONE copy of the bot per token.** If an old copy is still running, Telegram splits updates between
> the two and buttons become slow or unreliable. The bot prints a clear warning when it detects this.

---

## ⚙️ Configuration

Everything lives at the top of the second half of `FakeMailCheckerBotv2.py`.

### Required

| Setting | Where | Meaning |
|---|---|---|
| `BOT_TOKEN` | top of file | Your bot token from @BotFather |
| `OWNER_ID` | config block | Your numeric Telegram ID. Receives payment and task proofs and is the main admin |
| `LOG_CHANNEL` | config block | Channel ID such as `-1001234567890`. Needed for logs and **automatic backups** |

### Optional

| Setting | Default | Meaning |
|---|---|---|
| `ADMIN_IDS` | `[]` | Extra admin IDs (full admin access) |
| `UPI_ID` / `UPI_NAME` | in file | UPI address and display name used for the payment QR |
| `DB_PATH` | `erebus_checker.sqlite3` | Database file |
| `EMOJI_FILE` | `emoji_ids.json` | Optional file to override animated emoji IDs |
| `USE_CUSTOM_EMOJI` | `1` | Set `0` if animated emojis don't show for your bot |
| `FREE_DAILY` | `30` | Free checks per day |
| `BULK_MAX` | `500` | Maximum mails accepted in one bulk request |
| `MAX_PENDING` | `3` | Maximum pending payment screenshots per user |
| `PLANS` | see below | Premium plans (name, limit, days, price) |
| `REF_BONUS` | `40` | Bonus checks per successful referral |
| `CHUNK_SIZE`, `CHUNK_COOLDOWN`, `LONG_COOLDOWN_EVERY`, `LONG_COOLDOWN`, `UNL_COOLDOWN_EVERY`, `UNL_COOLDOWN` | `20, 10, 60, 20, 100, 20` | Bulk cooldown rules |
| `BACKUP_EVERY` | `1800` | Seconds between automatic backups |

`UPI_ID`, `UPI_NAME`, `DB_PATH`, `EMOJI_FILE`, `USE_CUSTOM_EMOJI` and `LOG_CHANNEL` can also be set through
environment variables of the same name, or simply edited directly in the file.

---

## 👤 How users use the bot

1. Send `/start` to see the main menu.
2. **Single Mode** – send a username (`john`) or an address (`john@hi2.in`).
3. **Bulk Mode** – send many addresses separated by spaces or commas.
4. Results show **❌ Taken**, **✅ Not taken / 🍀 Free**, or **❔ Unknown**.

Supported domains: `hi2.in` and `telegmail.com`. A name without `@` is checked on `hi2.in`.

**Main menu buttons**

| Button | What it does |
|---|---|
| Single Mode / Bulk Mode | Start checking |
| My Premium | Plan, expiry, daily limit |
| My Statistics | Total checks, today's usage, join date |
| Buy Premium | Plans and UPI payment |
| Redeem | Enter a token code |
| Free Checks | Redeem, Refer & Earn, Tasks |
| Updates | Your channel link |
| Admin Panel | Only visible to admins |

Notes:
- **Unknown** results (when the check could not be completed) are **not** counted against the limit.
- Messages that are no longer needed are cleaned up automatically to keep the chat tidy.
- `/cancel` stops any step in progress.

---

## ⏱ Bulk checking & cooldowns

Bulk requests are processed in **chunks of 20 mails**. After each chunk the bot shows a live timer, then continues on its own:

```
Cooldown ➛ 7s
██████░░░░
Next 20 mails start automatically
```

| User type | Cooldown rule |
|---|---|
| Free & premium (100 / 200) | **10 s** after every 20 mails, **20 s** after every 60 mails |
| Unlimited (and admins) | **20 s** after every 100 mails |

Examples for free / premium: 20 → 10 s · 40 → 10 s · 60 → **20 s** · 80 → 10 s · 100 → 10 s · 120 → **20 s** …

There is no cooldown after the final mail. Each chunk gets its own message, so very large batches never hit Telegram's message-length limit. A short summary is sent at the end.

---

## 💳 Plans & limits

| Plan | Checks / day | Validity | Price |
|---|---|---|---|
| Free | 30 | – | Free |
| Premium 100 | 100 | 7 days | ₹21 |
| Premium 200 | 200 | 7 days | ₹31 |
| Premium Unlimited | ∞ | 7 days | ₹49 |

Daily counters reset at **midnight IST**. Change plans or prices in the `PLANS` dictionary.

**Payment flow**

1. User opens **Buy Premium** and picks a plan.
2. The bot generates a **UPI QR** (and shows the UPI ID).
3. User pays, taps **I've Paid** and sends a screenshot.
4. The screenshot reaches the owner with **Approve / Reject** buttons.
5. On approval the plan activates instantly and the user is notified. Buying the same plan again extends it.

---

## 🎁 Free checks: Redeem · Referrals · Tasks

Everything earned here goes into a **bonus balance**. Bonus checks are used **after** the user's daily checks run out, and they never expire.

The **Free Checks** button appears on the main menu, on the Buy Premium screen, and on the "daily limit reached" screen.

### 🔑 Redeem tokens

- Admin creates a token, for example `/token 50 10 7` → *50 checks, usable by 10 users, valid for 7 days*.
- Custom code: `/token PROMO 50 10`.
- Users press **Redeem** and send the code. Each user can use a code once; expired or full codes are rejected.
- After 5 wrong codes a user is locked out for 10 minutes.

### 👥 Refer & Earn

- Every user has a personal link: `https://t.me/<your_bot>?start=ref_<user_id>` and a **Share** button.
- When a **brand-new** user starts the bot through the link, the referrer gets **+40 checks** and a notification.
- Existing users, repeat starts and self-referrals do not count.

### 📝 Tasks

- Admin adds a task: **title**, **description** (put the video or link here) and a **reward in checks**.
- Users open **Tasks**, pick one, complete it, and send a **screenshot** as proof.
- The proof goes to the owner with **Approve / Reject**. Approval adds the reward immediately.
- A task can be completed once per user. Rejected proofs can be submitted again.

---

## 🛠 Admin panel & commands

Open the panel with `/admin` or the **Admin Panel** button (admins only).

### Panel buttons

| Button | Purpose |
|---|---|
| Statistics | Users, active users, premium, banned, joined today, checks today, revenue, pending payments |
| Users / Premium Users | Latest users and active premium members |
| Broadcast | Send any message or media to all users, with confirmation |
| Export Users | CSV of all users |
| Ban / Unban, User Info, Message One User | User management |
| **Check Report** | Checks done, Taken / Free / Unknown for *last hour, today, all time* and the **latest 10 free mails from the last hour** |
| **Backup Now / Restore Backup** | Manual backup and restore |
| **Create Token / Tokens** | Make and manage redeem codes |
| **Tasks** | Add and remove tasks, see pending proofs |

### Commands

| Command | What it does |
|---|---|
| `/admin` · `/stats` · `/users` | Panel, quick statistics, CSV export |
| `/userinfo @user` | Full details of a user |
| `/premium @user days [p100\|p200\|unl]` | Grant premium |
| `/removepremium @user` | Remove premium |
| `/setlimit @user number\|default` | Custom daily limit |
| `/givechecks @user number` | Add bonus checks |
| `/ban @user` · `/unban @user` | Block or unblock |
| `/msg @user text` | Send a private message |
| `/token [CODE] checks max_users [days]` | Create a redeem token |
| `/tokens` · `/deltoken CODE` | List or delete tokens |
| `/tasks` | Manage tasks |
| `/backup` · `/restore` | Back up or restore the database |
| `/cancel` | Cancel the current step |

A user must have started the bot once before they can be found by `@username`.

---

## 💾 Backups & restore

**Automatic backups**

- Every **30 minutes** (first one about a minute after start) the bot copies the database and posts it to your log channel as `erebus_backup_YYYYMMDD_HHMM.sqlite3`.
- Also triggered after every approved payment and by **Backup Now** / `/backup` (a copy is also sent to your chat).
- Requires `LOG_CHANNEL` to be set and the bot to be an admin of that channel.

**Restore**

1. Open **Admin Panel → Restore Backup** (or send `/restore`).
2. Send a backup file to the bot **as a document**.
3. The bot checks that it's a valid, uncorrupted Erebus database, saves a safety copy of the current data as `erebus_checker.sqlite3.before_restore`, then loads the backup.
4. A wrong or corrupted file is rejected and your current data stays untouched.

Backups include users, premium plans, payments, limits, tokens, tasks, referrals and check history. Older backups are upgraded automatically when restored.

> 💡 Hosting on a platform with temporary storage? Keep the log channel set up. If the server resets, just restore the latest backup from the channel.

---

## 📂 Project files

```
FakeMailCheckerBotv2.py      the whole bot (engine + UI + accounts layer)
README.md                    this file
erebus_checker.sqlite3       database (created automatically)
erebus_checker.sqlite3.before_restore   safety copy created during a restore
emoji_ids.json               optional animated-emoji overrides
```

The mail-checking engine (`solve_recaptcha_hi2` and `check_hi2_email`) and the `run_bot()` loop are kept as they were; the UI, limits, payments and admin tools wrap around them.

---

## 🩺 Troubleshooting

| Problem | Fix |
|---|---|
| Buttons are slow or sometimes do nothing | Make sure **only one** copy of the bot is running. The console shows `ANOTHER copy of this bot is running` when it detects a clash |
| Animated emojis or colored buttons don't appear | Set `USE_CUSTOM_EMOJI=0`. The bot also falls back to plain emojis automatically |
| No backups or logs arrive | Set `LOG_CHANNEL` to your channel ID (starts with `-100`) and add the bot as channel admin |
| Payment QR missing | Install the QR library: `pip install "qrcode[pil]"`. Users still see the UPI ID without it |
| Many "Unknown" results | The site's captcha step failed; try again later or reduce speed. Unknown results are not charged |
| "User not found" for `@username` | The user must have started the bot at least once. Use their numeric ID instead |
| Restore says "not an Erebus backup" | Send a file created by this bot (`erebus_backup_*.sqlite3`) as a document |
| Slow responses on a phone or distant server | The bot makes several network calls per tap; a faster connection to Telegram helps |

---

## 🔒 Security notes

- **Never share your bot token.** If it has ever been posted publicly, revoke it in @BotFather (`/revoke`) and put the new one in `BOT_TOKEN`.
- Only IDs in `OWNER_ID` / `ADMIN_IDS` can use admin features. Admin buttons and commands are re-checked on every press.
- Keep your log channel private, since backups contain user data.
- Referral rewards can be farmed with extra Telegram accounts. If that becomes a problem, lower `REF_BONUS` or ask for a per-user referral cap.

---

<div align="center">

Made with 💜 by **Haze** · [@Noxmirage](https://t.me/Noxmirage) · [Channel](https://t.me/linksfromerebus)

</div>
