# network-basics

### terms to know
```
IP
Subnet mask
Gateway
Static vs. DHCP

Interface
Interface MAC
```

### Interface configuration files
```
/etc/nsswitch.conf
/etc/hosts                          // or hostname
/etc/sysconfig/network
/etc/sysconfig/network-scripts/ifcfg-nic
/etc/resolv.conf                    // dns server
```

### basic network commands
```
ping
ifconfig
ifup or ifdown
netstat -rnv
tcpdump -i enp0s3
```

### NIC = Network Interface Card 
example: enp0s3 <br>
lo = loopback device <br>
virb0 = Virtual Bridge 0 - is used for NAT (Network Address Translation) - to connect to outside network (sometimes)

```
ethtool enp0s3
```

### NIC Bonding Procedure - for redundancy (in case if one network addapred dies) and higher spead (1G + 1G = 2G)
```
modprobe bonding 
modinfo bonding 
Create /etc/sysconfig/network-scripts/ifcfg-bond0 
Edit /etc/sysconfig/network-scripts/ethernet1 
Edit /etc/sysconfig/network-scripts/ethernet2 
Restart network = systemctl restart network

nicl ---------> bond0 
nic2 -----^
```

### network configuration with tools
//Bond & Team - redundancy <br>
// 
``` 
nmcli                   -> clinmtui
nmtui                   -> console tool to manage network (interactive mode)
nm-connection-editor    -> works only on gui.... no console
```

### set static ip
```
nmcli device
ping 10.10.10.10                                            -> should not be pingable
nmcli connection modify enp0s3 ipv4.addresses 10.10.10.10
nmcli connection modify enp0s3 ipv4.gateway 10.10.10.1/24
nmcli connection modify enp0s3 ipv4.method manual
nmcli connection modify enp0s3 ipv4.dns 8.8.8.8
nmcli connection down enp0s3 
nmcli connection up enp0s3 
ip address show enp0s3
```

### add new static ip
```
nmcli device status
nmcli connection show -active
ping 10.10.10.11                                            -> should not be pingable
nmcli connection modify enp0s3 +ipv4.addresses 10.10.10.11/24
nmcli connection reload 
systemctl reboot
ip address show 
```

### Bridged
```
laptop--------internet
         |
host-----|
```

### Host-only
```
laptop----------internet

laptop---|
         |
host-----|
```

### telnet
```
sudo yum install telnet -y
```

### ssh
```
ps -ef | grep sshd
ps -aux | grep sshd

ssh peter@192.168.56.59

sudo vi /etc/ssh/sshd_config
    AllowUsers ...
```

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

### traceroute - trace network traffic
```
sudo yum install traceroute -y
traceroute destination_ip_url
netstat -rnv
```