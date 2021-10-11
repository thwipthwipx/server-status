# server-status

Allows you to find out free space, free RAM and check current backups

## Usage
1. upload the project to your server
2. go to the project folder
3. Install dependencies:
```
pip3 install -r requirements.txt
```
4. go to the /src folder
5. Make the `server-status.sh` file executable:
 ```
 chmod u+x server-status.sh
 ```
4. Rename `config.example.py` to `config.py`
5. Write in a file your variables in `config.py`
```
token = 'telegram bot api key'
chat_id = 'id channel in telegram'
backup_dir = 'path to the folder with backups'
```
The bot must be an administrator in your channel
6. Try to run and check it works
```
./server-status.sh
```
7. Set to send notifications on a schedule `crontab -e`. Example:
```
0 7 * * * /usr/local/bin/server-status/src/server-status.sh
```
