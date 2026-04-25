import psutil
import requests
from datetime import datetime


def get_system_report():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

    return f"""🖥️ *System Health Report*
Date&Time: {date} 
CPU Usage: {cpu}%
RAM Usage: {ram}%
Disk Usage: {disk}%"""

def send_telegram_message(message):
    bot_token = '7995153048:AAHEqDV1CFm7kA2B_kKZYSmIqNx_yAmEkcM'
    chat_id = '941681233'
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    print(datetime.now())
    payload = {
        
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, data=payload)

report = get_system_report()
print(report)
send_telegram_message(report)
