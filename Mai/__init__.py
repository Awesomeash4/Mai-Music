from Mai.core.bot import MaiBot
from Mai.core.dir import dirr
from Mai.core.git import git
from Mai.core.userbot import Userbot
from Mai.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()
git()
dbb()
heroku()
sudo()

# Clients
app = Mai()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
