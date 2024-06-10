# system-monitoring

```
top
df
dmesg
iostat 1
netstat
free
cat /proc/cpuinfo
cat /proc/meminfo
```
### manage running processes
```
top -d 1
```
### manage disk space
```
df -h
df -ha
```
```
sudo du /home -h --max-depth 1
```
```
free
cat /proc/cpuinfo
cat /proc/meminfo
```
### system messages
```
dmesg                                       -> msg of system 
sudo cat /var/log/messages | tail -n 
```
```
iostat l
netstat -rnv
netstat | more
```
### Log monitoring
```
cat /var/log/boot.log           -> info about how startup of system goes
cat /var/log/chronyd
cat /var/log/cron               -> info about each scheduled task/job
cat /var/log/maillog
cat /var/log/secure             -> info abaut all log in and out of all users
cat /var/log/messages           -> info about all software / hardware 
cat /var/log/httpd
```






