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




"""      [ CHANGE APP PRESENCE ] --

async def change_presence():

    activities = [
        discord.Streaming(name = ".gg/angelou ‎ .gg/sH5Mh2XfPC", url = "https://twitch.tv/angelouxddd"),
        discord.Streaming(name = "Comiendo FIDEOSSS 🍝", url = "https://twitch.tv/angelouxddd")
    ]

    index = 0
    await bot.wait_until_ready()
    while not bot.is_closed():
        await bot.change_presence(status = discord.Status.dnd, activity = activities[index])
        index = (index + 1) % len(activities)
        await asyncio.sleep(10)

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




# LANGUAGE LOADER
language_file = os.path.join("..", ".assets", "Data", "languages.json")
if not os.path.exists(language_file):
    save_template(language_file, {})

LANG_MESSAGES = {
    "es": {
        "support_language": "<:Imperium:1318478224690511963> **  ・  ** Idioma no soportado. Usa 'English' o 'Español'.",
        "unauthorized_guild": "<:Imperium:1318478224690511963> **  ・  ** No puedes usar este comando aquí, intenta en otro servidor nerdo. :nerd:",
        "free_limit": "<:Imperium:1318478224690511963> **  ・  ** Estás usando la versión gratuita. Solo puedes usar hasta **80 caracteres**.\n[ Para eliminar este límite, consulte en nuestro servidor: [🦇](https://discord.gg/sH5Mh2XfPC) ]",
        "long_msg": "<:Imperium:1318478224690511963> **  ・  ** El mensaje personalizado no puede exceder **1900 caracteres.**",
        "no_perm": "<:Imperium:1318478224690511963> **  ・  ** No tengo permisos para poder enviar mensajes en este canal.",
        "started": "<:Imperium:1318478224690511963> **  ・  ** Bot iniciado exitosamente con un delay de {delay} ms.\n[ Solo se enviaran *5* mensajes por cada */antiangelou* ejecutado o cada boton gris presionado ].\n‎",
        "language_changed": "<:Imperium:1318478224690511963> **  ・  ** Idioma actualizado a: **Español**.",
        "blacklisted": "<:Imperium:1318478224690511963> **  ・  ** No tienes permiso para usar este bot ya que estas blacklisteado.\n[ Consulta en el servidor para intentar revocar tu usuario de la blacklist. [🦇](https://discord.gg/sH5Mh2XfPC) ]"
    },
    "en": {
        "support_language": "<:Imperium:1318478224690511963> **  ・  ** Language not supported. Use 'English' o 'Spanish'.",
        "unauthorized_guild": "<:Imperium:1318478224690511963> **  ・  ** You can't use this command here, try in another server nerd. :nerd:",
        "free_limit": "<:Imperium:1318478224690511963> **  ・  ** You're using the free version. You can only send up to **80 characters**.\n[ Check our server to remove this limit: [🦇](https://discord.gg/sH5Mh2XfPC) ]",
        "long_msg": "<:Imperium:1318478224690511963> **  ・  ** Custom message cannot exceed **1900 characters.**",
        "no_perm": "<:Imperium:1318478224690511963> **  ・  ** I don't have permission to send messages in this channel.",
        "started": "<:Imperium:1318478224690511963> **  ・  ** Bot successfully started with {delay} ms delay.\n[ Only *5* messages will be sent per */antiangelou* command or each gray button press ].\n‎",
        "language_changed": "<:Imperium:1318478224690511963> **  ・  ** Language updated to: **English**.",
        "blacklisted": "<:Imperium:1318478224690511963> **  ・  ** You don't have permission to use this bot because you are blacklisted.\n[ Please check our server to request removal from the blacklist. [🦇](https://discord.gg/sH5Mh2XfPC) ]"
    }
}

def get_user_lang(user_id):
    langs = load_template(language_file)
    return langs.get(str(user_id), "es")

def set_user_lang(user_id, lang):
    langs = load_template(language_file)
    langs[str(user_id)] = lang
    save_template(language_file, langs)




"""      [ SAVE COMMAND LOGS ] --

command_log_file = os.path.join("..", ".assets", "Data", "logs.json")

def load_command_logs(path):
    if not os.path.exists(path):
        with open(path, 'w', encoding = 'utf-8') as f:
            json.dump([], f, indent = 4)
    with open(path, 'r', encoding = 'utf-8') as f:
        return json.load(f)

def save_command_logs(path, data):
    with open(path, 'w', encoding = 'utf-8') as f:
        json.dump(data, f, indent = 4)

def add_command_log(server_id, user_id, user_tag, command_name):
    logs = load_command_logs(command_log_file)

    server_entry = None
    for entry in logs:
        if server_id in entry:
            server_entry = entry
            break

    if server_entry is None:
        logs.append({server_id: [[user_id, user_tag, command_name]]})
    else:
        user_command_exists = False
        for uc in server_entry[server_id]:
            if uc[0] == user_id and uc[2] == command_name:
                user_command_exists = True
                break
        
        if not user_command_exists:
            server_entry[server_id].append([user_id, user_tag, command_name])

    save_command_logs(command_log_file, logs)

"""




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
    def __init__(self, user_id, spam_message, delay, lang):
        super().__init__(timeout = None)
        self.user_id = user_id
        self.spam_message = spam_message
        self.delay = delay
        self.lang = lang

        label = "+5 Mensajes" if lang == "es" else "+5 Messages"

        button = Button(
            label = label,
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
    forbidden_guilds = { "1358449508849025167", "1236760438566293557", "1229605011428868136" }

    whitelist_data = load_whitelist(whitelist_file)
    user_id = str(interaction.user.id)
    lang = get_user_lang(user_id)
    is_whitelisted = user_id in whitelist_data.get("authorized_users", [])

    blacklist_data = load_blacklist(blacklist_file)
    if user_id in blacklist_data.get("blacklisted_users", []):
        await interaction.response.send_message(LANG_MESSAGES[lang]["blacklisted"], ephemeral = True)
        return

    if interaction.guild and str(interaction.guild.id) in forbidden_guilds:
        await interaction.response.send_message(LANG_MESSAGES[lang]["unauthorized_guild"], ephemeral = True)
        return
    
    """      [ SAVE USER LOGS ] --

    server_id = str(interaction.guild.id) if interaction.guild else "DM"
    user_tag = f"{interaction.user.name}"

    add_command_log(server_id, user_id, user_tag, "/antiangelou")

    """
    
    default_message = (
        "\n"
        "                _ _\n"
        "**  •  **  *IMPERIUM  &  ANTI ANGELOU*     ♱     *ON TOP*\n"
        "**  •  **  Unete ya al imperio de los fideos, Le Front!\n"
        "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||| https://discord.gg/angelou https://discord.gg/sH5Mh2XfPC @everyone \n"
    )

    if mensaje and not is_whitelisted and len(mensaje) > 80:
        try:
            await interaction.response.send_message(LANG_MESSAGES[lang]["free_limit"], ephemeral=True)
        except discord.NotFound:
            try:
                await interaction.followup.send(LANG_MESSAGES[lang]["free_limit"], ephemeral=True)
            except:
                pass
        return
        
    if is_whitelisted and mensaje and len(mensaje) > 1900:
        try:
            await interaction.response.send_message(LANG_MESSAGES[lang]["long_msg"], ephemeral=True)
        except discord.NotFound:
            try:
                await interaction.followup.send(LANG_MESSAGES[lang]["long_msg"], ephemeral=True)
            except:
                pass
        return
        
    spam_message = mensaje if mensaje else default_message
    channel_id = interaction.channel.id

    async def spam_loop():
        for _ in range(5):
            await interaction.followup.send(spam_message, allowed_mentions = discord.AllowedMentions(everyone = True))
            await asyncio.sleep(delay / 1000)

    """      [ OLD SPAMMER ] --

    try:
        if isinstance(interaction.channel, discord.DMChannel) or (
            isinstance(interaction.channel, discord.TextChannel) and
            interaction.channel.permissions_for(interaction.guild.me).send_messages):

            await interaction.response.send_message(
                LANG_MESSAGES[lang]["started"].format(delay = delay), ephemeral=True
            )

            task = asyncio.create_task(spam_loop())
            if channel_id not in spam_tasks:
                spam_tasks[channel_id] = []
            spam_tasks[channel_id].append(task)

        else:
            await interaction.response.send_message(LANG_MESSAGES[lang]["no_perm"], ephemeral = True)

    """

    try:
        if isinstance(interaction.channel, discord.DMChannel) or (
            isinstance(interaction.channel, discord.TextChannel) and
            interaction.channel.permissions_for(interaction.guild.me).send_messages):

            await interaction.response.send_message(
                LANG_MESSAGES[lang]["started"].format(delay=delay),
                view=AntiAngelouView(interaction.user.id, spam_message, delay, lang),
                ephemeral=True
            )

            task = asyncio.create_task(spam_loop())
            if channel_id not in spam_tasks:
                spam_tasks[channel_id] = []
            spam_tasks[channel_id].append(task)

        else:
            await interaction.response.send_message(LANG_MESSAGES[lang]["no_perm"], ephemeral=True)

    except Exception:
        pass




# LANGUAGE COMMAND
@bot.tree.command(
    name = "language",
    description = "Cambia el idioma por defecto para los comandos."
)

@app_commands.describe(
    mensaje = "Escoge un idioma: English or Spanish. [Proximamente más]"
)

async def language_cmd(interaction: discord.Interaction, mensaje: str):
    user_id = str(interaction.user.id)

    black_lang = get_user_lang(interaction.user.id)

    blacklist_data = load_blacklist(blacklist_file)
    if user_id in blacklist_data.get("blacklisted_users", []):
        await interaction.response.send_message(LANG_MESSAGES[black_lang]["blacklisted"], ephemeral = True)
        return
    
    """      [ SAVE USER LOGS ] --

    user_tag = f"{interaction.user.name}"
    server_id = str(interaction.guild.id) if interaction.guild else "DM"

    add_command_log(server_id, user_id, user_tag, "/language")

    """

    lang = mensaje.lower()
    if lang in ["english", "en", "inglés", "ingles"]:
        lang = "en"
    elif lang in ["spanish", "es", "español", "espanol"]:
        lang = "es"
    else:
        user_lang = get_user_lang(interaction.user.id)
        await interaction.response.send_message(LANG_MESSAGES[user_lang]["support_language"].format(lang = mensaje), ephemeral = True)
        return

    set_user_lang(interaction.user.id, lang)
    await interaction.response.send_message(LANG_MESSAGES[lang]["language_changed"].format(lang = mensaje), ephemeral = True)




# RUN APPLICATION
keep_alive()
bot.run(TOKEN)
