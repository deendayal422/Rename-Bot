# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "16681004")

API_HASH = os.environ.get("API_HASH", "161b61f5a06dd299a3d88a3384b9f104")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6816910555:AAE4kLmSB_FTF3pGMy1SpAV9lZsU6yzY-A8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "@Deendayal_dhakad") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://dndldhkd:iZgn69Q8PIN28EER@cluster0.mgz6put.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6646028262').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
