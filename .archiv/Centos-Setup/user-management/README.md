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

### Monitor users
```
who             -> who is loggedin and since when
last            -> return info about every log in and reboot of system
w               -> who but more info
pinky           -> like w
id              -> return user info
```

### Talking to users
```
users           -> return list of active users on host
wall            -> used to print msg to user console
wall
    [Enter][Enter](write msg)[Enter][Enter] 
    [Ctrl] D

write           -> write direct msg to user
write
    [Enter][Enter](write msg)[Enter][Enter] 
    [Ctrl] D
```

Windows = Active Directory  <br>
RedHat  = IDM (Identity Manager)  <br>
WinBIND = Used in Linux to communicate with Windows (Samba)  <br>
Linux   = OpenLDAP (opn source) //module 7  <br>

### Linux Account Authentication = LDAP (LDAP is a protocol)
```

```


