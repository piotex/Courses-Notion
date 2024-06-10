# openLDAP

### openLDAP installation
```
sudo yum install *openldap* -y
```
```
systemctl start slapd
systemctl enable slapd
```
```
ls -al  /etc/openldap/slapd.d
vi /etc/nsswitch.conf
    
```