# timedatectl 

### timedatectl - beter date command
```
timedatectl
timedatectl list-timezones
    q
timedatectl set-timezone "America/New_York"
timedatectl set-time YYYY-MM-DD
timedatectl set-time '2024-11-21 16:04:40'

systemctl status ntpd
systemctl status chronyd 
timedatectl set-ntp true
```

```
date
```
```
sudo date -s $(curl -s "http://worldtimeapi.org/api/timezone/Europe/Warsaw" | grep -oE '"datetime":"[^"]+"' | cut -d'"' -f4)
```

### set actual date
```
sudo date -s $(curl -s "http://worldtimeapi.org/api/timezone/Europe/Warsaw" | grep -oE '"datetime":"[^"]+"' | cut -d'"' -f4)
```