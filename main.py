# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram import Client

bot_token = "6072750107:AAGCAaTGcXjiiex8CwxmzfvHxSbbAZo8lW8"
api_id = 26286754
api_hash = "7a637e05958e14496e6ab1910a9eb9e7"

plugins = dict(
    root="plugins"
)

Bot = Client(
    "Movie-Info-Bot-V2",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins
)

Bot.run()
