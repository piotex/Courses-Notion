# firewall

```
iptables    - older
firewalld   - newer
```

### firewalld
```
systemctl stop iptables
systemctl disable iptables
systemctl mask iptables
```
```
systemctl status firewalld.service

firewall-cmd --list-all
firewall-cmd --reload

firewall-cmd --get-services
firewall-cmd --get-zones
firewall-cmd --get-active-zones
firewall-cmd --zone=public --list-all

cat /usr/lib/firewalld/services/ssh.xml
cat /usr/lib/firewalld/services/kube-apiserver.xml

sudo firewall-cmd --zone=public --add-service=http --permanent
sudo firewall-cmd --zone=public --remove-service=http --permanent

sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
sudo firewall-cmd --zone=public --remove-port=8080/tcp --permanent

sudo firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.0.25" reject'     -> block traffic from this ip address

```


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