# stdplugins/priv4te.py
from telethon import events
from uniborg.util import admin_cmd
from time import sleep

@borg.on(admin_cmd(pattern="uwu"))
async def handler(event):
    for i in range(3):
        await event.edit("(｀･ω･´)")
        sleep(0.5)
        await event.edit("( ｀･ω)")
        sleep(0.5)
        await event.edit("( 　｀･)")
        sleep(0.5)
        await event.edit("(　 　 　)")
        sleep(0.5)
        await event.edit("(･` 　)")
        sleep(0.5)
        await event.edit("(ω･` )")
        sleep(0.5)
        await event.edit("(´･ω･`)")
