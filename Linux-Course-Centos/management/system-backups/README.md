# system-backups (dd Command)

```
5 Different Types of Backups:
-----------------------------
1. System backup (entire image using tools such as acronis, Veeam, Commvault, etc.)
2. Application backup (3rd party application backup solution)
3. Database backup (Oracle dataguard, SQL backup, etc.)
4. Filesystem backup (tar gzip directories, etc.)
5. Disk backup or disk cloning (dd command)
```
```
dd if=<source file name> of=<target file name> [Options]

Backup/Clone entire hard disk to another hard disk connected to the same system:
dd if=/dev/sda of=/dev/sdb

Backup/Clone disk partition:
dd if=/dev/sda1 of=/root/sda1.img

Restoring this image to other machine:
copy .img to host
dd if=/root/sda1.img of=/dev/sdb3
```# system-maintenance

```
shutdown
init 0-6
        0 - shutdown
        3 - bring in multiusermode ???
        6 - reboot
reboot
halt    - force terminate system
```
