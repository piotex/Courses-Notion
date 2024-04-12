# Centos-Setup

### Create new virtual machine in VirtualBox
1. Create new machine
2. Set name and ISO image + Skip Unatended...
3. RAM: 8192 + 4 Procesors
4. Hard drive: 40Gb

### Centos init confing
1. Keyboard: English
2. Time: Europe/Warsow
3. Software Selection: Server
4. Instalation Destination: Select created disk
5. Root Password
6. User Creation

### Static Ip Address
1. Turn machine off
2. Settings -> Network -> Adapter 2: Host-only
3. Turn machine on
4. ``` nmtui ``` <br/> 
Add -> Ethernet <br/>
Profile name: enp0s8 <br/>
Device: Network adapter e.g.: enp0s8 (08:00:27:99:3C:43)
Address: 192.168.56.59 <br/>
Gateway: 255.255.255.0 <br/>
Save <br/>

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

### CMD Setup
```
sudo yum check-update
sudo yum update -y
sudo reboot
```

### User management
```
sudo useradd -m -G technical_users docker
sudo passwd docker
chown docker:technical_users /data/

visudo
    peter    ALL=(ALL)       ALL


```