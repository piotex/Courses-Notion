# user-management

### User management
```
sudo groupadd technical_users
sudo usermod -aG technical_users peter

sudo useradd -m -G technical_users docker
sudo passwd docker
sudo mkdir /data
sudo chown docker:technical_users /data

visudo
    peter    ALL=(ALL)       ALL
```

# user-management

```
useradd peter
id peter
passwd peter
usermod -G my_group peter
userdel -r peter
```
```
groupadd my_group
cat /etc/groups
groupdel my_group
```
```
cat /etc/passwd
cat /etc/shadow
```
```
useradd -g my_group -s /bin/bash -c "Peter K" -m -d /home/peter peter
```
```
sudo su
visudo
    peter    ALL=(ALL)       ALL
cat /etc/sudoers
```