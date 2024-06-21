# service-commands

### Service commands
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