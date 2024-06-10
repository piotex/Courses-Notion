# lvm

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