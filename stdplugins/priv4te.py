# stdplugins/priv4te.py
from telethon import events
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="hi alok"))
async def handler(event):
    await event.reply("hey")
