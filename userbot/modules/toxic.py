from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^D(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**UDAH BACOT SO ASIK NAJISS**")


@register(outgoing=True, pattern='^E(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TERUS?LU PIKIR GUA PEDULI? TENTU SAJA TIDAK YAHAHAHA RUN BESTI RUN LU TYP GINI LU PIKIR GUA BACA
TYP LU? NAJIS BAT SIAL.PENGEN BANGAT DI NOTICE GUA YA? YAHAHA NGENTOT NGENTOT DI TELE MAH JAGO DI RL JADI AUTIS BUSET
UDAH MUKA KAGA CAKEP BAU JENGBOT SOKSOAN SEGALA JIAKHH KENA MENTAL SOSMED MALAH HIAT TELE UNIN TELE AUTIS BAT ANJ
KALO GA ADA NYALI DIEM AJA BOS KE TRIGGER SENDIRI NTAR WKEEKKEKE TAWAIN AJA BOCAH AUTIS KALO NYALI MASIH PATUNGAN
DIEM AJA BEGO.APA?LU MAU BILANG FEEDBACK? SETIA KAWAN? AELAH NGENTOT GA USAH SEMBUNYI DI BALIK KATA ITU JAMET JIAHAHAHA
RUN BESTI ADA NYALI PATUNGAN BERKEDOK SETIA KAWAN WKEKEKEKEKE**")


@register(outgoing=True, pattern='^F(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU SEMUA KAYA KONTOL HAHAHAHA!!**")


@register(outgoing=True, pattern='^I(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL LU JAMURAN PAKE AER KERAS BIAR GA JAMURAN!!**")


@register(outgoing=True, pattern='^Q(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAJELAS KAFIR!!**")


@register(outgoing=True, pattern='^R(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL KONTOL APA YANG KERIPUT?KONTOL KAU LAH ANJING!!**")


@register(outgoing=True, pattern='^T(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TETE DOANG GEDE GA OPEN VCS!!!**")


@register(outgoing=True, pattern='^U(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOK CAKEP LU!!GANTENGAN JUGA GUA YHAHAHAHA**")


@register(outgoing=True, pattern='^W(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOK CAKEP LU!!CANTIKAN JUGA GUA YHAHAHAHA**")


@register(outgoing=True, pattern='^Q(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LU BACOT GA BIKIN GUA TREMOR GOBLOK HAHAHAHA!!**")

CMD_HELP.update({
    "toxic":
    "D\
\nUsage: Bacotin Orang.\
\n\nE\
\nUsage: Buat Orang Yang Sok Keras.\
\n\nF\
\nUsage: Ngatain Orang Wkwkkw.\
\n\nI\
\nUsage: Kontol Orang Ngatain.\
\n\nQ\
\nUsage: Ngajak Ribut Orang.\
\n\nR\
\nUsage: Pantun Anjing.\
\n\nT\
\nUsage: Nyebutin Binatang.\
\n\nU\
\nUsage: Biar Dikata Ganteng.\
\n\nW\
\nUsage: Biar Dikata Cantik.\
\n\nQ\
\nUsage: Tremor Kan Lu."
})
