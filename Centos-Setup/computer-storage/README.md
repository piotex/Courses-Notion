# computer-storage

```
Local storage
- RAM, HDD, SSD, etc.

DAS (Direct Attached Storage)
- CD/DVD, USB flash drive

SAN (Storage Area Network)
- Storage attached through iSCSI or fiber cable

NAS (Network Attached Storage)
- Storage attached over network (TCP/IP)
- Samba, NFS, etc.
```

### disk-partition
```
df  -h

fdisk -l
```

### addind disk
```
- power off machine
- Settings > Storage > (Click on Controller: SATA) > (Click on Adds new storage attachement) > (Select: Add Hard Disk)
    Create new disk > VDI > Dynamically allocated > Name + Size > Create
    Click on OK
- power on machine 

sudo su
    df -h
    fdisk -l        // will return Disk name

fdisk /dev/sdb
    n
        p
        Enter
        Enter
        Enter
    w

mkfs.xfs /dev/sdb1
mkdir /data
mount /dev/sdb1 /data
vi /etc/fstab                                             //add text at the end of file
    /dev/sdb1   /data   xfs   defaults   0   0

init 6          // or reboot
```
### unmount disk
```
unmount /data
df -h
```

### creating partition !!!
==================== Graf ================================
```
File system                         datafs
                                      |
Logical Volume(s)                   datalv
                                      |
Volume Group                        datavg
                                      |
                           --------------------------
                           |          |             |           
Physical Volume         /dev/sda1   /dev/sdb1   /dev/sdc1
                            |           |           |
Partitions              /dev/sda1   /dev/sdb1   /dev/sdc1
                            |           |           |
Hard Disks              /dev/sda    /dev/sdb    /dev/sdc
```

================= Command: ================================
```
- power off machine
- Settings > Storage > (Click on Controller: SATA) > (Click on Adds new storage attachement) > (Select: Add Hard Disk)
    Create new disk > VDI > Dynamically allocated > Name + Size > Create
    Click on OK
- power on machine 

sudo su
    df -h
    fdisk -l        // will return Disk name

fdisk /dev/sdc
    n
        p
        Enter
        Enter
        Enter
    p
    t
        L
        8e
    p
    w

pvcreate /dev/sdc1
    pvdisplay   
vgcreate oracle_vg /dev/sdc1                  // oracle_xx is custon name, it can be changed
    vgdisplay oracle_vg 
lvcreate -n oracle_lv --size 1000M oracle_vg 

mkfs.xfs /dev/oracle_vg/oracle_lv
mkdir /oracle
mount /dev/oracle_vg/oracle_lv /oracle
vi /etc/fstab                                             //add text at the end of file
    /dev/oracle_vg/oracle_lv   /oracle   xfs   defaults   0   0

init 6          // or reboot
```

### LVM - Logical Volume Management
LVM allows disks to be combined together 
```
Physical       Volume       Logical
Volume         Groups       Volumes

                           |---> system
Disk 1  --->--- rootvg --->|---> home
                           |---> swap


Disk 2 --->|               |---> data 1
Disk 3 --->|--- datavg --->|---> data 2
Disk 4 --->|               |---> data 3
                           |---> data 4
```
```
select LVM disk during centos instalation ... add mandatory disk locations and / all
LVM is defaut for Cetnos xD
```

### Extend disk using LVM
```
Options:
- delete older files to free up disk space
- add new physical disk mount to /oracle2
- create a new virtual disk and mount to /oracle2
- extend /oracle through LVM
```
```
fdisk -l
fdisk /dev/sdd
    n
        p
        Enter
        Enter
        Enter
    p
    t
        L
        8e
    p
    w
reboot
sudo su
    pvdisplay 
    pvs
    vgdisplay
pvcreate /dev/sdd1
vgextend oracle_vg /dev/sdd1                  
lvextend -L+1024M /dev/mapper/oracle_vg-oracle_lv     // name from df -h command for /oracle 
xfs_growfs /dev/mapper/oracle_vg-oracle_lv
    df -h
```

### Usefull commands
```
df -h
du /home -h --max-depth 1
lsblk


```




