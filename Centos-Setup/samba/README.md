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

