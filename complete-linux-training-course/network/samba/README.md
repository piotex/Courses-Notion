# samba



# SAMBA - like NFS but can be mounted by other operating systems

```
###### Install on host Linux ##########################
take snapshot
sudo yum install samba samba-client samba-common

firewall-cmd --permanent --zone=public --add-service=samba
firewall-cmd -reload

systemctl stop firewalld, iptables
systemctl disable firewalld, iptables

mkdir -p /samba/shared_dir
chmod a+rwx /samba/shared_dir
chown -R nobody:nobody /samba

# chcon -t samba_share_t /samba/shared_dir
# sestatus
# vi /etc/selinux/config
    Change: SELINUX=enforcing
    To:     SELINUX=disable
# reboot


vi /etc/samba/smb.conf
    // delete all under # you modified it.
    insert:

    [global]
        workgroup = WORKGROUP
        netbios = centos
        security = user
        map to guest = bad user
        dns proxy = no

    [Anonymous] 
        path = /samba/shared_dir
        browsable = yes
        writable = yes
        guest ok = yes
        guest only = yes
        read only = no

testparam
    [Enter]

systemctl enable smb, nmb
systemctl start smb, nmb
systemctl status smb, nmb

###### Mount on Client Windows ##########################
search > 
    \\192.168.56.59

###### Mount on Client Linux ##########################
yum install cifs-utils samba-client
mkdir /mnt/samba_sahred
mount -t cifs //192.168.56.59/Anonymous /mnt/samba_sahred
    [Enter]

df -h
cd /mnt/samba_sahred && ls -la
```


### secured samba:
```
Create a group smbgrp & user larry to access the samba server with proper
authentication
# useradd larry
# groupadd smbgrp
# usermod -a -G smbgrp larry
# smbpasswd -a larry
New SMB password: YOUR SAMBA PASS
Retype new SMB password: REPEAT YOUR SAMBA PASS
Added user larry
• Create a new share, set the permission on the share:
# mkdir /samba/securepretzels
# chown -R larry:smbgrp /samba/securepretzels
# chmod -R 0770 /samba/securepretzels
# chcon -t samba_share_t /samba/securepretzels
• Edit the configuration file /etc/samba/smb.conf (Create a backup copy first)
# vi /etc/samba/smb.conf
Add the following lines
[Secure]
path = /samba/securepretzels
valid users = @smbgrp
guest ok = no
writable = yes
browsable = yes
• Restart the services
# systemctl restart smb
# systemctl restart nmb





