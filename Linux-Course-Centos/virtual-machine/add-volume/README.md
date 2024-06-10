# virtual-machine-add-volume

### Add additional volume
1. Turn machine off
2. Settings -> Storage -> Add hard disk -> Create
3. Turn machine on
4. Show disk data
```
sudo su
df -h
fdisk -l
parted -l
lsblk
lsblk -o NAME,HCTL,SIZE,MOUNTPOINT,TYPE
```
5. Add volume
```
fdisk -uc /dev/sdb
    n
    p
    1
    [Enter]
    [Enter]
    w

mkfs.ext4 /dev/sdb1
cd /
mkdir /data
mount /dev/sdb1 /data
vi /etc/fstab
    /dev/sdb1 /data ext4 defaults 1 2
umount /data
mount -a
```
