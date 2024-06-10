# creating-partition

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