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

add / remove
sudo firewall-cmd --zone=public --add-service=http --permanent
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
sudo firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.0.25" reject'     -> block traffic from this ip address
sudo firewall-cmd --add-icmp-block-inversion"                                                   -> block incomming ping traffic
host -t a www.facebook.com                                  -> find ip address
sudo firewall-cmd --direct --add-rule ipv4 filter OUTPUT 0 -d 31.13.71.36 -j DROP               -> block facebook page

```