# add-disk

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