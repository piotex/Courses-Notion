# ntp-and-chronyd

### NTP - network time protocol
```
/etc/ntp.conf
systemctl restart ntpd
ntpq
    peers
    quit
port: 123
```

### chronyd - beter NTP - time synchronization
```
ps -ef | grep chrony
rpm -qa | grep chrony
yum install chrony -y
/etc/chronyd.conf
/var/log/chrony
systemctl status chronyd

chronyc
```