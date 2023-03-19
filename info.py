import os, re
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '15823382'))
API_HASH = environ.get('API_HASH', '016d5e115a06ddfb6121823d72ae4d8c')
BOT_TOKEN = environ.get('BOT_TOKEN', "5931548571:AAFn32G5T4VgMa9EaTzr8Gt_d-HkiLrMRzM")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

PICS = (environ.get('PICS', 'http://telegra.ph/file/2380653c98786f9306bbf.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/94750f782f45f592b823f.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/8ee413afc32e5b393e790.jpg")
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/07c14729659c7c2b99f5a.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI',
                           "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Channel Button Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Trickyakash5213')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Trickyakash5213')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/Trickyakash5213')
MSG_ALRT = environ.get('MSG_ALRT', 'Share and Support Us')

# Custom Chats
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', -1001797596826))
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', -1001814841940))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', 'https://t.me/+kRAEW_GJ4RY1ZThl')
HOW_DWLD_LINK = environ.get('HOW_DWLD_LINK', 'https://t.me/okhajaj/8')

# Log Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001524622686))
RQST_LOG_CHANNEL = int(environ.get('RQST_LOG_CHANNEL', -1001524622686))

# Bot Options
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION",
                                  "ɴᴀᴍᴇ: <code>{file_name}</code> \n\n [🏏 𝘼𝙡𝙡 𝙇𝙞𝙫𝙚 𝙎𝙥𝙤𝙧𝙩𝙨 𝙁𝙧𝙚𝙚 𝙃𝙚𝙧𝙚 ⚽️](https://urlsopen.net/kuDJ)\n [🏏 𝘼𝙡𝙡 𝙇𝙞𝙫𝙚 𝙎𝙥𝙤𝙧𝙩𝙨 𝙁𝙧𝙚𝙚 𝙃𝙚𝙧𝙚 ⚽️](https://urlsopen.net/kuDJ)</b>")
BATCH_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION",
                                 "ɴᴀᴍᴇ: <code>{file_name}</code> \n\n [🏏 𝘼𝙡𝙡 𝙇𝙞𝙫𝙚 𝙎𝙥𝙤𝙧𝙩𝙨 𝙁𝙧𝙚𝙚 𝙃𝙚𝙧𝙚 ⚽️](https://urlsopen.net/kuDJ)\n [🏏 𝘼𝙡𝙡 𝙇𝙞𝙫𝙚 𝙎𝙥𝙤𝙧𝙩𝙨 𝙁𝙧𝙚𝙚 𝙃𝙚𝙧𝙚 ⚽️](https://urlsopen.net/kuDJ)</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.TEMPLATE)
CYNITE_IMDB_TEMPLATE = environ.get("KD_IMDB_TEMPLATE", script.TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001814841940')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

# Auto Delete , Filter & Auto Filter
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
MAUTO_DELETE = is_enabled((environ.get('MAUTO_DELETE', "True")), True)

# Delete Time
DELETE_TIME = int(environ.get('DELETE_TIME', 120))
SPL_DELETE_TIME = int(environ.get('SPL_DELETE_TIME', 60))

# URL SHORTNER

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'shorturllink.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '95a8195c40d31e0c3b6baa68813fcecb1239f2e9')

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += (
    "IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += (
    "P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += (
    "SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (
    f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += (
    "Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += (
    "Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (
    f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

# Auto Delete For Bot Sending Files #

BLACKLIST_WORDS = (
    list(os.environ.get("BLACKLIST_WORDS").split(","))
    if os.environ.get("BLACKLIST_WORDS")
    else []
)

BLACKLIST_WORDS = ["[D&O]", "[MM]", "[]", "[FC]", "[CF]", "LinkZz", "[DFBC]", "@New_Movie", "@Infinite_Movies2", "MM", "@R A R B G", "[F&T]", "[KMH]", "[DnO]", "[F&T]", "MLM", "@TM_LMO", "@x265_E4E", "@HEVC_MoviesZ", "SSDMovies", "@MM_Linkz", "[CC]", "@Mallu_Movies", "@DK Drama", "@luxmv_Linkz", "@Akw_links", "CK_HEVC", "@Team_HDT", "[CP]", "www 1TamilMV men", "@TamilMob_LinkZz", "@GreyMatter_Bots", "@Forever_Bros", "@TamilMvmovies2Tunnel", "@TEAM_HD4K", "@MoviezzClub", "PFM", "[GorGom]", "4U", "www", "1TamilMV", "[FHM]", "@CC", "[CF]", "MLM", "themoviesboss", "@AM_linkzz", "[MF]", "[CVM]", "[PM]", "[MM]", "aFilmywap", "[MSM]", "FG", "@Mj_Linkz", "MCArchives", "[MASHOBUC]", "[MABLG]", "Bros", "[YDF]", "HEBC", "LINKS", "www_1TamilMV_men", "Linkz", "HEVC", "[MoviesNowTamil]", "7HitMovies", "linkzz", "[JP]", "[CD]", "HD4K", "[CD]", "@MM", "[DC]", "DC", "[AnimeRG]", "[CNT]", "Moviez", "TheMoviesBoss", "bros", "Movies", "1stOnNet", "[TIF]", "()", "[MF]", "[WC]", "ғαιвεяsgαтє", "TF", "E4E", "X265", "autos", "[HCN]", "KC", "[KC]", "[Movieshd121]", "[CNT]", "Download", "[MS]", "[WMJ]", "links", "[Movie_Bazar]", "S_1", "[MF]", "[MJ]", "Filmy4cab", "24X7", "[MJ]", "M_D_B", "[Nep_Blanc]", "HDT", "tv", "M_D_B_", "wdll", "[FN]", "[mwkOTT]", "LinkZ", "MABLG_", "[MW]", "[MH]", "[Movie_Bazar]", "Links", "media", "TamilHDRip", "[MwK]", "{KMH}", "[M5]", "[A2MOVIES]", "@Movierockerzs", "[Hotstar Tamil]", "[CG]", "ടാക്കീസ് മീഡിയ റിലീസ്", "[ടാക്കീസ് മീഡിയ റിലീസ്]", "[ടാക്കീസ് മീഡിയ റിലീസ്]", "D&O", "MM", "[]", "FC", "CF", "LinkZz", "DFBC", "New_Movie", "Infinite_Movies2", "MM", "R A R B G", "F&T", "KMH", "DnO", "F&T", "MLM", "TM_LMO", "x265_E4E", "HEVC_MoviesZ", "SSDMovies", "MM_Linkz", "CC", "Mallu_Movies", "DK Drama", "luxmv_Linkz", "Akw_links", "CK_HEVC", "Team_HDT", "CP", "www 1TamilMV men", "TamilMob_LinkZz", "GreyMatter_Bots", "Forever_Bros", "TamilMvmovies2Tunnel", "TEAM_HD4K", "MoviezzClub", "PFM", "GorGom", "4U", "www", "1TamilMV", "FHM", "CC", "CF", "MLM", "themoviesboss", "AM_linkzz", "MF", "CVM", "PM", "MM", "aFilmywap", "MSM", "FG", "Mj_Linkz", "MCArchives", "MASHOBUC", "MABLG", "Bros", "[YDF]", "HEBC", "LINKS", "www_1TamilMV_men", "Linkz", "HEVC", "[MoviesNowTamil]", "7HitMovies", "linkzz", "JP", "CD", "HD4K", "CD", "MM", "DC", "DC", "AnimeRG", "CNT", "Moviez", "TheMoviesBoss", "bros", "Movies", "1stOnNet", "TIF", "()", "MF", "WC", "ғαιвεяsgαтє", "TF", "E4E", "X265", "autos", "HCN", "KC", "[KC]", "Movieshd121", "CNT", "Download", "MS", "WMJ", "links", "Movie_Bazar", "S_1", "MF", "MJ", "Filmy4cab", "24X7", "MJ", "M_D_B", "Nep_Blanc", "HDT", "tv", "M_D_B_", "wdll", "FN", "mwkOTT", "LinkZ", "MABLG_", "MW", "MH", "Movie_Bazar", "Links", "media", "TamilHDRip", "MwK", "{KMH}", "M5", "A2MOVIES", "Movierockerzs", "Hotstar Tamil", "CG", "ടാക്കീസ് മീഡിയ റിലീസ്", "()", "[]", "{}", "(", ")", "[", "]", "[@]", "telegram", "{", "}", "{}", "മൂവി സീരീസ്", "മിസ്കിൻ മൂവി സീരീസ്", "മൂവി സീരീസ്", "മിസ്കിൻ", "PF", "[PF]"]
