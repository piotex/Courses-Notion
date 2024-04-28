# linux-os-hardening

```
User Account
Remove un-wanted packages
Stop un-used Services
Check on Listening Ports
Secure SSH Configuration
Enable Firewall (iptables/firewalld)
Enable SELinux
Change Listening Service Port Numbers
Keep your OS up to date (security patching)
```
```
cat /etc/passwd     -> list all user accounts
chage -l peter      -> print when password expire 
vi /etc/login.def   -> config of password requirements
```
```
rpm -qa | wc -l 
systemctl -a
```
```
netstat -tunlp          -> view active ports !!!
```

