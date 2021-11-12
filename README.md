# File-SHare-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
 </a>
  <br>
  <a href="https://github.com/Judson-web/STM-FILE-SHARE-BOT-V3/stargazers">
    <img src="https://img.shields.io/github/stars/Judson-web/STM-FILE-SHARE-BOT-V3?style=social">
  </a>
  <a href="https://github.com/Judson-web/STM-FILE-SHARE-BOT-V3/fork">
    <img src="https://img.shields.io/github/forks/Judson-web/STM-FILE-SHARE-BOT-V3?label=Fork&style=social">
  </a>  
</p>


Telegram Bot To Store Posts And Documents And it Can Access By Special Links.
I Guess This Will Be Usefull For Many People.....😇. 

### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- More than one Posts in One Link.
- Can be deployed on heroku directly.

### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 

##
### Installation
#### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Judson-web/STM-FILE-SHARE-BOT-V3)</br>

#### Deploy in your VPS
````bash
git clone https://github.com/Judson-web/STM-FILE-SHARE-BOT-V3
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users
```

### Variables

* `API_HASH` Your API Hash from [Click Me](https://my.telegram.org/auth)
* `API_ID` Your API ID from [Click Me](https://my.telegram.org/auth)
* `TG_BOT_TOKEN` Your bot token from [@BotFather](https://telegram.me/BotFather)
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/Judson-web/STM-FILE-SHARE-BOT-V3/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub


### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption


## Support   
Join Our [Telegram Group](https://t.me/storytym) For Support/Assistance.     

### Credits

- Thanks To [STM](https://t.me/STMbOTsUPPORTgROUP) 

##

   **Star this Repo if you Liked it ⭐⭐⭐**
