# atq

```
atq                         -> show list of all planed jobs/tasks

echo "echo \"rm -rf /tmp/archive.tar.gz\" " > /tmp/at_script.sh
chmod 777 /tmp/at_script.sh
at 02:48 PM -f /tmp/at_script.sh

echo "hello peter" >> /home/peter/message.txt
echo 'wall < /home/peter/message.txt' | at now + 1 minute
```
```
crontab -e          -> edit crontab
crontab -l          -> list all crontab entries
crontab -r          -> remove crontab
crond               -> crontab daemon
systemctl status crond


min | hour | day | mounth | day of the week
* * * * *

crontab -e
21 46 * 10 * echo "hello peter" > /tmp/msg_hello_from_crontab.txt
crontab -r
crontab -l
```
