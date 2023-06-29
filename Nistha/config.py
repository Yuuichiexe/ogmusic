import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "10821359"))
API_HASH = getenv("API_HASH", "2b1b1a5e842bff25ad1baa12657b3894")
BOT_USERNAME = getenv("BOT_USERNAME", "Esdeath_probot")
BOT_TOKEN = getenv("BOT_TOKEN", "6178626262:AAGYaJJ0-9seijKX0wT54BW_PaiER82rpN0")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "Mega_Bot_Updates")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Mega_Bots_Support")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Fuckingenos")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQBZsZXNVZZAqAxcLEWp2sqzVMrg9o9FXEChXut_iw6KGX5BWovKWY4qV3dZRxgI0wu-4efSQuZ-e_HiQahpbM3ME_59oxeHx3dfwqDTPLE5dzO2hHu_q1bQf0b5rfHqA5yF02fy3Qy8anRXkHpuoBwIumLxZSrsWS7S0jlIhNZw8mFJoga_QvqWdHlzhPfdsPIFrV_Ye3vbQHOytK3gs6yuNeu6MGwRysIPxcYZ5450-iUUg-1TUtINGeSzaZ6afGCEWAPuZzMhPda9NzQIbhkb4y9rdrG6NdsqXhMJK-UPEYcqVpjGbvi6ZFda40UaVnv4B83JYY-0tH-BqNpLTSaPAAAAAVG4GlQA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6204994197").split()))
aiohttpsession = aiohttp.ClientSession()
