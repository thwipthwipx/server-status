import config
import psutil
from psutil._common import bytes2human
import telebot
import subprocess

# create instance of the TeleBot
bot = telebot.TeleBot(token=config.token, parse_mode="html")

# get server name
server = subprocess.getoutput("hostname")

# get disk usage
disk_usage = psutil.disk_usage('/')
disk_usage_total = bytes2human(disk_usage.total)
disk_usage_used = bytes2human(disk_usage.used)
disk_usage_free = bytes2human(disk_usage.free)

# get virtual memory
virtual_memory = psutil.virtual_memory()
virtual_memory_total = bytes2human(virtual_memory.total)
virtual_memory_used = bytes2human(virtual_memory.used)
virtual_memory_free = bytes2human(virtual_memory.free)

# get the count of backups
backup_dir = 'find ' + config.backup_dir + ' -type f -mmin ' + config.backup_hours + ' | wc -l'
backups_count = subprocess.getoutput(backup_dir)

# get the count of sites
sites_dir = 'find ' + config.sites_dir + ' -type ' + config.file_type + config.params + ' | wc -l'
sites_dir_count = subprocess.getoutput(sites_dir)

# generate a message in telegram
output_message = "<b>Сервер:</b> " + "\n" + \
                 server + "\n" + \
                 "\n" + \
                 "<b>Жесткий диск:</b>" + "\n" + \
                 "Всего: " + disk_usage_total + "\n" + \
                 "Использовано: " + disk_usage_used + "\n" + \
                 "Свободно: " + disk_usage_free + "\n" + \
                 "\n" + \
                 "<b>Оперативная память:</b>" + "\n" + \
                 "Всего: " + virtual_memory_total + "\n" + \
                 "Использовано: " + virtual_memory_used + "\n" + \
                 "Свободно: " + virtual_memory_free + "\n" + \
                 "\n" + \
                 "<b>Количество бэкапов: </b>" + "\n" + \
                 "Сделано " + backups_count + ' из ' + sites_dir_count + ' сайтов'

# send a message to telegram
bot.send_message(config.chat_id, output_message)
