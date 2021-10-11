import config
import psutil
import telebot
import subprocess

# create instance of the TeleBot
bot = telebot.TeleBot(token=config.token, parse_mode="html")

# get server name
server = subprocess.getoutput("hostname")

# get disk usage
disk_usage = psutil.disk_usage('/')
disk_usage_total = ("%d GiB" % (disk_usage.total // (2 ** 30)))
disk_usage_used = ("%d GiB" % (disk_usage.used // (2 ** 30)))
disk_usage_free = ("%d GiB" % (disk_usage.free // (2 ** 30)))

# get virtual memory
virtual_memory = psutil.virtual_memory()
virtual_memory_total = ("%d GiB" % (virtual_memory.total // (2 ** 30)))
virtual_memory_used = ("%d GiB" % (virtual_memory.used // (2 ** 30)))
virtual_memory_free = ("%d GiB" % (virtual_memory.free // (2 ** 30)))

# get backups from directories with the current edit date
backup_dir = 'find ' + config.backup_dir + ' -type f -mtime -1'
backups_list = subprocess.getoutput(backup_dir)

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
                 "<b>Список бэкапов за сегодня: </b>" + "\n" + \
                 backups_list

# send a message to telegram
bot.send_message(config.chat_id, output_message)
