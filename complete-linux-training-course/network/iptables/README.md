# iptables

### iptables
```
systemctl stop firewalld
systemctl disable firewalld
systemctl mask firewalld
```
```
rpm -qa | grep iptables
yum install iptables-services

systemctl start iptables
systemctl enable iptables

iptables -L             -> to check the iptables rules
iptables -F             -> to flush iptables 
```
