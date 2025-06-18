# Coding: utf-8
# Copyright (C) 2024 github.com/donfushii

import os
import json
import asyncio
import discord
import logging

from server import keep_alive

from discord.ext import commands
from rgbprint import gradient_print
from discord.ui import View, Button
from discord import app_commands, ButtonStyle, AllowedMentions, PartialEmoji

# STOP SHARD & RATELIMIT LOGS
logging.getLogger("discord.gateway").disabled = True         # SHARDS
logging.getLogger("discord.client").disabled  = True         # STATIC TOKEN

logging.getLogger("discord.webhook").setLevel(logging.ERROR) # WEBHOOKS
logging.getLogger("discord").setLevel(logging.ERROR)         # FATAL ERRORS
logging.getLogger("websockets").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.ERROR)

# MAIN FUNCTION'S
class mainfuncs:

    def clear():
        os.system("cls") if os.name == "nt" else os.system("clear")

    def title(args=None):
        os.system('mode con: cols=120 lines=30')
        os.system("title  Imperium [Application Spammer]  -  Made by Fushii") if args == None else os.system(f"title Web utils {args}")

# BANNER COLOR
class ImperiumStyle():
    MAIN = f"\x1b[38;2;247;184;207m"

class ImperiumLight():
    MAIN = f"\x1b[38;2;252;131;175m"

class ImperiumBlack():
    MAIN = f"\x1b[38;2;245;102;154m"

def ascii_art_title(client_id):
    return f"""
  
                                                                   ,,                               
              `7MMF'                                               db                               
                MM                                                                                  
                MM  `7MMpMMMb.pMMMb. `7MMpdMAo.  .gP"Ya `7Mb,od8 `7MM `7MM  `7MM  `7MMpMMMb.pMMMb.  
                MM    MM    MM    MM   MM   `Wb ,M'   Yb  MM' ''   MM   MM    MM    MM    MM    MM  
                MM    MM    MM    MM   MM    M8 8M''''''  MM       MM   MM    MM    MM    MM    MM  
                MM    MM    MM    MM   MM   ,AP YM.    ,  MM       MM   MM    MM    MM    MM    MM  
              .JMML..JMML  JMML  JMML. MMbmmd'   `Mbmmd'.JMML.   .JMML. `Mbod'YML..JMML  JMML  JMML.
                                       MM                                                           
                                     .JMML.                                          Made By Fushii
\n
                         https://discord.com/oauth2/authorize?client_id={client_id}
\n
"""

def ascii_description(status_msg: str):
    return f"""

                                                 -> Information <-                              
                                 ╔═══                                          ═══╗ 

                                  {status_msg} 

                                 ╚═══                                          ═══╝ 
"""

# TOKEN TEMPLATE FOUNDER
filename = os.path.join("..", ".assets", "Data", "config.json")

def load_template(path):
    with open(path, 'r', encoding = 'utf-8') as file:
        return json.load(file)

def save_template(path, data):
    os.makedirs(os.path.dirname(path), exist_ok = True)

    with open(path, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def validate_inputs(user_id):
    if not user_id.isdigit():
        print(ImperiumBlack.MAIN + f"   [>] 'CLIENT_ID' must contain only numbers.")

if not os.path.exists(filename):
    print(ImperiumBlack.MAIN + f"   [>] Template file not found. Creating a new one: " + filename)

    empty_template = {
        "TOKEN": "",
        "CLIENT_ID": ""
    }

    save_template(filename, empty_template)

template_data = load_template(filename)

TOKEN = os.environ.get("TOKEN", template_data.get("TOKEN", ""))
CLIENT_ID = os.environ.get("CLIENT_ID", template_data.get("CLIENT_ID", ""))

if not TOKEN or not CLIENT_ID:
    print(ImperiumBlack.MAIN + f"   [>] The template file '{filename}' is missing TOKEN or CLIENT_ID.")
    exit(1)

# WHITELIST LOADER
whitelist_file = os.path.join("..", ".assets", "Data", "whitelist.json")

def load_whitelist(path):
    if not os.path.exists(path):
        save_whitelist(path, {"authorized_users": []})
    with open(path, 'r', encoding = 'utf-8') as file:
        return json.load(file)

def save_whitelist(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent = 4)

whitelist_data = load_whitelist(whitelist_file)

# BLACKLIST LOADER
blacklist_file = os.path.join("..", ".assets", "Data", "blacklist.json")

def load_blacklist(path):
    if not os.path.exists(path):
        save_blacklist(path, {"blacklisted_users": []})
    with open(path, 'r', encoding = 'utf-8') as file:
        return json.load(file)

def save_blacklist(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

blacklist_data = load_blacklist(blacklist_file)

# APPLICATION BOT PREFIX
intents = discord.Intents.all()
intents.messages = True
intents.message_content = True
intents.typing = False 
intents.presences = False

bot = commands.Bot(command_prefix = "!", intents = intents)

spam_tasks = {}

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()

        mainfuncs.clear()
        mainfuncs.title()
        gradient_print(ascii_art_title(CLIENT_ID), start_color = (0xFF6EA3), end_color = (0xF7B8CF))

        gradient_print(ascii_description(" > [02] : Successfully loaded. Ready for spam."), start_color = (0xFF6EA3), end_color = (0xF7B8CF))

    except Exception as e:
        print(ImperiumBlack.MAIN + f"   [>] Failed to sync commands: {e}")

mainfuncs.clear()

gradient_print(ascii_art_title(CLIENT_ID), start_color = (0xFF6EA3), end_color = (0xF7B8CF))
gradient_print(ascii_description("> [01] : Loading bot resources (SHARDS & TOKEN)."), start_color = (0xFF6EA3), end_color = (0xF7B8CF))

# EXTRA BUTTON SPAM
class AntiAngelouView(View):
    def __init__(self, user_id, spam_message, delay):
        super().__init__(timeout = None)
        self.user_id = user_id
        self.spam_message = spam_message
        self.delay = delay

        button = Button(
            label = "+5 Mensajes",
            style = ButtonStyle.gray,
            emoji = PartialEmoji(name = "Imperium", id = 1318478224690511963),
            custom_id = "extra_spam"
        )
        button.callback = self.extra_spam
        self.add_item(button)

    async def extra_spam(self, interaction):
        await interaction.response.defer(ephemeral = True)
        for _ in range(5):
            await interaction.followup.send(
                self.spam_message,
                allowed_mentions = AllowedMentions(everyone = True)
            )
            await asyncio.sleep(self.delay / 1000)

# RAID COMMAND
@bot.tree.command(
    name = "antiangelou",
    description = "Ataca un servidor remotamente. ‎ ‎•‎ ‎ https://discord.gg/angelou ‎ ‎|‎ ‎ https://discord.gg/sH5Mh2XfPC"
)

@app_commands.describe(
    delay = "Delay en milisegundos entre cada mensaje (por defecto 500ms evita ratelimit).",
    mensaje = "Envia un mensaje personalizado."
)

async def send(interaction: discord.Interaction, delay: int = 500, mensaje: str | None = None):
    forbidden_guilds = {"1358449508849025167", "1236760438566293557", "1229605011428868136"}

    whitelist_data = load_whitelist(whitelist_file)
    user_id = str(interaction.user.id)
    is_whitelisted = user_id in whitelist_data.get("authorized_users", [])

    blacklist_data = load_blacklist(blacklist_file)
    if user_id in blacklist_data.get("blacklisted_users", []):
        await interaction.response.send_message(
            "<:Imperium:1318478224690511963> **  ・  ** No tienes permiso para usar este bot ya que estás blacklisteado.\n[ Consulta en el servidor para intentar revocar tu usuario de la blacklist. [🦇](https://discord.gg/sH5Mh2XfPC) ]",
            ephemeral=True
        )
        return

    if interaction.guild and str(interaction.guild.id) in forbidden_guilds:
        await interaction.response.send_message(
            "<:Imperium:1318478224690511963> **  ・  ** No puedes usar este comando aquí, intenta en otro servidor nerdo. :nerd:",
            ephemeral=True
        )
        return

    default_message = (
        "\n"
        "                _ _\n"
        "**  •  **  *IMPERIUM  &  ANTI ANGELOU*     ♱     *ON TOP*\n"
        "**  •  **  Unete ya al imperio de los fideos, Le Front!\n"
        "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||| https://discord.gg/angelou https://discord.gg/sH5Mh2XfPC @everyone \n"
    )

    if mensaje and not is_whitelisted and len(mensaje) > 80:
        await interaction.response.send_message(
            "<:Imperium:1318478224690511963> **  ・  ** Estás usando la versión gratuita. Solo puedes usar hasta **80 caracteres**.\n[ Para eliminar este límite, consulte en nuestro servidor: [🦇](https://discord.gg/sH5Mh2XfPC) ]",
            ephemeral=True
        )
        return

    if is_whitelisted and mensaje and len(mensaje) > 1900:
        await interaction.response.send_message(
            "<:Imperium:1318478224690511963> **  ・  ** El mensaje personalizado no puede exceder **1900 caracteres.**",
            ephemeral=True
        )
        return

    spam_message = mensaje if mensaje else default_message
    channel_id = interaction.channel.id

    async def spam_loop():
        for _ in range(5):
            await interaction.followup.send(
                spam_message,
                allowed_mentions=discord.AllowedMentions(everyone=True)
            )
            await asyncio.sleep(delay / 1000)

    try:
        if isinstance(interaction.channel, discord.DMChannel) or (
            isinstance(interaction.channel, discord.TextChannel) and
            interaction.channel.permissions_for(interaction.guild.me).send_messages):

            await interaction.response.send_message(
                f"<:Imperium:1318478224690511963> **  ・  ** Bot iniciado exitosamente con un delay de {delay} ms.\n[ Solo se enviarán *5* mensajes por cada */antiangelou* ejecutado o cada botón gris presionado ].\n‎",
                view=AntiAngelouView(interaction.user.id, spam_message, delay),
                ephemeral=True
            )

            task = asyncio.create_task(spam_loop())
            if channel_id not in spam_tasks:
                spam_tasks[channel_id] = []
            spam_tasks[channel_id].append(task)

        else:
            await interaction.response.send_message(
                "<:Imperium:1318478224690511963> **  ・  ** No tengo permisos para poder enviar mensajes en este canal.",
                ephemeral=True
            )

    except Exception:
        pass

# RUN APPLICATION
keep_alive()
bot.run(TOKEN)
