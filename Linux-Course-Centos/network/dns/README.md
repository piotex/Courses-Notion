# dns

### DNS - Domain Name System
```
Hostname -> IP              - A Record
IP -> Hostname              - PTR Record
Hostname -> Hostname        - CNAME Record
```
```
/etc/named.conf
/var/named
```
```
systemctl restart named
```

#### Setup DNS
```
sudo rpm -qa | grep bind
sudo yum install bind bind-utils -y

vi /etc/named.conf
    listen on port 53 ( 127.0.0.1; 192.168.56.59; );

    zone - change to:
    zone "lab.local" IN {
        type master;
        file "forward.lab";
        allow-update { none; };
    };
    (under it)

    zone "1.168.192.in-addr.arpa" IN {
        type master;
        file "reverse.lab";
        allow-update { none; };
    }

vi /var/named/forward.lab
vi /var/named/reverse.lab

```

### network dns check commands
```
dig masterdns.lab.local
nslookup masterdns.lab.local
nslookup clienta.lab.local
nslookup clientb.lab.local
nslookup 192.168.1.240
nslookup 192.168.1.241

```

