from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`TERUS ? LU PIKIR GUA PEDULI TENTU SAJA TIDAK YAHAHAHA RUN BESTI RUN LU TYP GINI LU PIKIR GUA BACA
TYP LU ? NAJIS BAT SIAL.PENGEN BANGAT DI NOTICE GUA YA? YAHAHA NGENTOT NGENTOT DI TELE MAH JAGO DI RL JADI AUTIS BUSET
UDAH MUKA KAGA CAKEP BAU JENGBUT SOKSOAN SEGALA JIAKHH KENA MENTAL SOSMED MALAH HIAT TELE UNIN TELE AUTIS BAT ANJ
KALO GA ADA NYALI DIEM AJA BOS KE TRIGGER SENDIRI NTAR WKEEKKEKE TAWAIN AJA BOCAH AUTIS KALO NYALI MASIH PATUNGAN
DIEM AJA BEGO.APA?LU MAU BILANG FEEDBACK? SETIA KAWAN? AELAH NGENTOT GA USAH SEMBUNYI DI BALIK KATA ITU JAMET JIAHAHAHA
RUN BESTI ADA NYALI PATUNGAN BERKEDOK SETIA KAWAN WKEKEKEKEKE`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")

# Create by myself @localheart


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


# Create by myself @localheart


@register(outgoing=True, pattern='^.idiot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("\n╭╮╱╱╭╮"
                     "\n┃╰╮╭╯┃"
                     "\n╰╮╰╯╭┻━┳╮╭╮"
                     "\n╱╰╮╭┫╭╮┃┃┃┃"
                     "\n╱╱┃┃┃╰╯┃╰╯┃"
                     "\n╱╱╰╯╰━━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮"
                     "\n┃╭━╮┃"
                     "\n┃┃╱┃┣━┳━━╮"
                     "\n┃╰━╯┃╭┫┃━┫"
                     "\n┃╭━╮┃┃┃┃━┫"
                     "\n╰╯╱╰┻╯╰━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╭╮╱╱╱╭╮"
                     "\n┃╭━━╯╱┃┃╱╱╭╯╰╮"
                     "\n┃╰━━┳━╯┣┳━┻╮╭╯"
                     "\n┃╭━━┫╭╮┣┫╭╮┃┃"
                     "\n┃╰━━┫╰╯┃┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻┻━━┻━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━╮╱╭╮"
                     "\n┃┃╰╮┃┃"
                     "\n┃╭╮╰╯┣━━╮"
                     "\n┃┃╰╮┃┃╭╮┃"
                     "\n┃┃╱┃┃┃╰╯┃"
                     "\n╰╯╱╰━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╱╱╱╱╭╮╱╭╮"
                     "\n╰╮╭╮┃╱╱╱╱╱┃┃╭╯╰╮"
                     "\n╱┃┃┃┣━━┳╮╭┫╰┻╮╭╯"
                     "\n╱┃┃┃┃╭╮┃┃┃┃╭╮┃┃"
                     "\n╭╯╰╯┃╰╯┃╰╯┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻━━┻━━┻━╯")


CMD_HELP.update({
    "animasi2":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sadboy`\
    \n↳ : Biasalah sadboy hikss\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.punten` dan `.pantau`\
    \n↳ : Coba aja hehehe.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.idiot`\
    \n↳ : u're ediot xixixi.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `kosong`\
    \n↳ : Tunggu update selanjutnya kawan."
})
