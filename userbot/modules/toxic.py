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
    await typew.edit("**HA? GAPEDULI JUGA SI NGENTOT JIAHAHAHA**")


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
