# extend-lvm-disk

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