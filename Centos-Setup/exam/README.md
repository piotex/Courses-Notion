# exam

### Question 1:
Which of the following is Redhat owned Linux flavors?
```
Redhat, CentOS and Fedora
```

### Question 2:
What are the different ways to install Linux operating systems?
```
ISO image
CD/DVD ROM
Network boot
```

### Question 3:
What is the client used to connect to VMWare from Windows?
```
vSphare
```

### Question 4:
What is the port number used for SSH connection?
```
22
```

### Question 5:
What is the new command introduced in the newer version of Redhat/CentOS replacing ifconfig?
```
ip
```

### Question 6:
Which ones are Linux filesystem?
```
ext2, ext3, ext4, xfs
```

### Question 7:
Which directory has the logs and configuration files?
```
/var and /etc
```

### Question 8:
Which of the following command is using an absolute path?
```
cp /ala /mo
```

### Question 9:
What is the purpose of <dmesg> command?
```
kernel log messages
```

### Question 10:
Which command will rename abc to xyz?
```
mv abc xyz
```

### Question 11:
If you have 10 lines in a file, which of the following command will give you 9th line?
```
tail -2 file | head -1
cat file | tail -2 | head -1
```

### Question 12:
Which of the following option of ls command can be used to view file inode number?
```
-i
```

### Question 13:
Which of the following command is used to view the contents of a compressed text file?
```
zcat
```

### Question 14:
What is the command to change the group ownership of a file?
```
chgrp
```

### Question 15:
Which command is used to extract a column from a text file?
```
cut
```

### Question 16:
Which of the following command display the disk utilization of a directory?
```
du
```

### Question 17:
Which option of rm command is used to remove a directory including all its subdirectories? 
```
-r
```

### Question 18:
What is the command to determine the path of an executable file?
```
which
```

### Question 19:
What is the command to count the number of words in a file?
```
wc
```

### Question 20:
Which of the following commands displays one page of output at a time?
```
more
```

### Question 21:
Which of the following commands will display all the files in your current directory and its subdirectories including the hidden files?
```
ls -aR
```

### Question 22:
Which of the following commands can be used to change default permissions for files and directories at the time of creation?
```
umask
```

### Question 23:
Which command will tar files p1 p2 and p3 files into filename.tar?
```
tar cvf filename.tar p1 p2 p3
```

### Question 24:
If you’re configuring the GRUB boot loader, which of the following files would you edit in a boot loader?
```
/boot/grub2/grub.cfg
```

### Question 25:
Which key is used to undo in vi editor
```
u
```

### Question 26:
Which of the following commands will get us the list of home directories of users in /etc/passwd?
```
cut -d: f6 /etc/passwd
```

### Question 27:
Which command will allow you to change the priority of a program already running?
```
renice
```

### Question 28:
Which of the following commands cannot reboot the system?
```
telinit 0
```

### Question 29:
Which command substitutes every instance of a word Windows to Linux in a file named ops? 
```
sed 's/Windows/Linux/g' ops
```

### Question 30:
How to delete all empty lines from data.txt file and save?
```
sed -i '/^$/d' data.txt
```

### Question 31:
How to add a user iafzal to another group called linux?
```
usermod -aG linux iafzal
```

### Question 32:
Which parameter you will add in /etc/sudoers file to allow iafzal to run all the root level commands?
```
iafzal ALL=(ALL) ALL
```

### Question 33:
How to check current system run-level?
```
who -r
runlevel
```

### Question 34:
What will happen if you run this command “ln test paul”?
```
It will create a hard link from paul to test
```

### Question 35:
Which command will change your hostname to stella?
```
hostnamectl set-hostname stalla
```

### Question 36:
How to check which NTP server your client is synchronized with?
```
ntpq --> peers
chronyc --> sources
```

### Question 37:
Which command will set a regular users password to force changing it every 90 days?
```
change -M 90 user
```

### Question 38:
Which of these directories are you least likely to backup or restore?
```
/proc
```

### Question 39:
Which permission, when applied to a directory in the file system, will allow a user to enter the directory?
```
Execute
```

### Question 40:
A file employees.odt has permission of rw-r- -r- -. If james is the file's owner, what can he do with it?
```
He can open the file, make changes and save the file
```

### Question 41:
You just created a new script file named myapp.sh. However, when you try to run it from the command prompt, the bash shell generates an error that says -bash: ./myapp.sh: Permission denied. Which command will fix this problem?
```
chmod u+x myapp.sh 
```

### Question 42:
Which of the following is NOT a Unix/Linux Filesystem?
```
unixfs
```

### Question 43:
Which of the following command will search for james (ignoring case sensitive) from USA file and output to an existing file BRAZIL?
```
grep -i james USA > BRAZIL
```

### Question 44:
When you insert a CD/DVD into your server, which mount point it gets mounted?
```
/media
```

### Question 45:
Which command will list files/dir owned by group root assuming there are no files named root?
```
ls -l | awk '{print $4,$9}' | grep root
```

### Question 46:
If you want to find a file in your system which of the following command you would use?
```
find / -name "FILENAME"
```

### Question 47:
Which command is used to identify the file type?
```
file
```

### Question 48:
How to create an alias to cd into /home/john/scripts with alias name sc?
```
alias sc="cd /home/john/scripts"
```

### Question 49:
Describe the output of “wc filename”
```
Lines, words and byte size
```

### Question 50:
Which of the following command will match all files with names starting with p followed by any SINGLE CHARACTER of the characters abc but ending with st.txt?
```
ls p[abc]st.txt
```

### Question 51:
Which of the following is the correct command to create a soft link of /home/iafzal/devola in tmp directory?
```
ln -s /home/iafzal/devola /tmp
```

### Question 52:
If you want to assign read and write permissions to a file for owner and others to a file bacula then which of the following command would work. Existing permissions are –rwxrw-rw-? 
```
chmod ugo-rwx bacula and chmod uo+rw bacula
```

### Question 53:
Which of the following is NOT a command to read a file?
```
echo
```

### Question 54:
Which command would work if you want to get the total number of errors in a file?
```
grep -i error FILENAME | wc -l
cat FILENAME | grep -i error | wc –l
```

### Question 55:
Which of the following is the correct command to get first 3 characters of a last column in a file zoo?
```
cat zoo | awk '{print $NF}' cut -c1-3
```

### Question 56:
How to list all processes running in your Linux system?
```
ps -ef
```

### Question 57:
You have created a script chkhealth in /home/seinfeld directory. Now you want it to run every Sunday at 9:15am. Which would be the correct syntax in crontab?
```
15 9 * * 0 /home/seinfeld/chkhealth
```

### Question 58:
If you are trying to kill a process and it does die then which option you would use to force kill it?
```
kill -9 PID
```

### Question 59:
How to check memory status in Linux?
```
free
top
```

### Question 60:
Which parameter you will have to set in ntp.conf or chrony.conf file to synchronize your system time?
```
server IP
```

### Question 61:
Which port NTP runs on?
```
123
```

### Question 62:
Can you read /var/log/messages as a regular user?
```
No
```

### Question 63:
How to find system hardware information in Linux?
```
dmidecode
```

### Question 64:
You called Redhat and they asked you to provide system information. Which command you will run to gather system information?
```
uname -a
cat /etc/redhat-release
```

### Question 65:
What is the name of the command which generates an SOS report for Redhat?
```
sosreport
```

### Question 66:
Which file you will have to modify to assign static IP address?
```
/etc/sysconfig/network-scripts-ifcfg-NIC
```

### Question 67:
Which file you will modify if you want to update the DNS server information?
```
/etc/resolv.conf
```

### Question 68:
Which command you will run to check your network interface status?
```
ethtool
```

### Question 69:
How to update your Linux system by deleting obsolete packages?
```
yum upgrade
```

### Question 70:
What is the command to extend LVM?
```
lvextend
```

### Question 71:
Which command will create a user home director as smith with /tmp?
```
useradd -d /tmp/smith smith
```

### Question 72:
Which command can publish environment variables?
```
export
```

### Question 73:
What is the command to get SELinux status?
```
getenforce
sestatus
```

### Question 74:
Command to set selinux in permissive mode?
```
setenforce 0
```

### Question 75:
Which file holds the configuration of NFS shared directories?
```
/etc/exports
```

### Question 76:
Which command searches for a keyword in a file while opened in vi editor?
```
/ or ?
```

### Question 77:
Which of the following commands will restart the network?
```
systemctl restart network
```

### Question 78:
How to enable NIC bonding driver?
```
modprobe bonding
```

### Question 79:
If your system does not have Development Tools then which command can be run to install it?
```
yum groups install "Development Tools"
```

### Question 80:
Which command can be used to download a package from a URL?
```
wget
```

### Question 81:
Command to create local repo?
```
createrepo
```

### Question 82:
Which one of the following is SSH configuration file?
```
/etc/ssh/sshd_config
```

### Question 83:
Which directory has all DNS Zone files?
```
/var/named
```

### Question 84:
What is the name of the DNS package?
```
bind
```

### Question 85:
How to restart DNS service?
```
systemctl restart named
```

### Question 86:
Which one is the configuration file for sendmail?
```
/etc/mail/sendmail.mc
```

### Question 87:
Which one is the configuration file for httpd?
```
/etc/httpd/conf/httpd.conf
```

### Question 88:
Which http file holds the contents of your webpage by default?
```
/var/www/html/index.html
```

### Question 89:
When a system reboots it looks into which of the following file to mount filesystem?
```
/etc/fstab
```

### Question 90:
Which one of the following is NFS configuration file?
```
/etc/sysconfig/nfs
```

### Question 91:
There are total of 7 run-levels from 0-6, what is run-level 3?
```
Multi-user mode with networking
```

### Question 92:
Which of the following is the correct Linux boot process sequence?
```
BIOS -> MBR -> GRUB -> Kernel -> Init -> Run-level
```

### Question 93:
Which of the following is NOT a command to transfer files from one machine to another?
```
transfer
```

### Question 94:
How to list total number of disks and its partitions in Linux?
```
fdisk -l
```

### Question 95:
Which command is used to make swap space?
```
mkswap
```

### Question 96:
Which of the following is RAID1?
```
2 disks mirror to each other
```

### Question 97:
Which utility to use if your XFS filesystem is corrupted?
```
xfs_repair
```

### Question 98:
When NFS server is setup and filesystem is ready to be exported, which command will export the NFS shares?
```
exportfs
```

### Question 99:
What is the command to mount NFS share on the client server?
```
mount 192.168.56.59:/shared-dir /mnt/location
```

### Question 100:
What is the difference between SAN and NAS?
```
SAN is directly attached to a machine using fiber or SCSI 
NAS is attached through network
```

### Question 101:
A systems administrator needs to append output of ls –lha /opt command to the contents of a test.txt file. Which of the following commands will accomplish this?
```
```

### Question 101:
A systems administrator needs to append output of ls –lha /opt command to the contents of a test.txt file. Which of the following commands will accomplish this?
```
ls –lha /opt >> test.txt
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```

### 
```
```
