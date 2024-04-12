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
