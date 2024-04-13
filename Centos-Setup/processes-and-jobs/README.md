# processes-and-jobs

Application -> Service that runs on your computer like apache or chrome<br>
Script      -> List of instructions writen in a file which can can be executed <br>
Process     -> // represent an instance of running program <br>
Daemon      -> //proces that run continuously in a background<br>
Threads     -> // it's a sequence of instructions that can be executed independently by a CPU core<br>
Job         -> // run a service or process at a schedule time<br>
<br>

# Service commands
```
systemctl or service
ps
top
kill
crontab         -> schedule job
at              -> like crontab but run onece
```
```
systemctl --type service
systemctl enable apache       -> enable service to start automatically during system boot
systemctl status apache
systemctl list-units --all    -> display list of all units managed by systemd

systemctl start apache
systemctl stop apache
systemctl restart apache
```
```
ps aux
ps -ef
ps -u peter
```
```
top -d 1
top -d 1 -u peter             // press C to show absolute path of script
top -d 1 -u peter             // press K to select which process kill
top -d 1 -u peter             // press M and P to sort processes by Memory usage
```
```
kill -l                    -> list all signkill
kill -9 PID                -> force kill
kill -15 PID               -> kill gracefully
kill -1 PID                -> restart
```
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
# Move process to the background
```
sleep 100
    [Ctrl] Z
        bg
sleep 100 &

ps -ef | grep sleep


bg                       -> move process to background 
fg                       -> move process to front 

nohup sleep 75 &         -> detached from user parrent process // ignore closing terminal
jobs
more nohup.out
```

# silent process
```
nohup sleep 73 > /dev/null 2>&1 &
```

# working with process priority 
```
nice
```



