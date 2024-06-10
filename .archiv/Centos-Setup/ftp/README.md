# FTP - FIle Transfer Protocol
Default FTP Port = 21 <br>

### instalation on host
```
sudo su
rpm –qa | grep vsftpd   -> check if already installed
yum install vsftpd -y
cp /etc/vsftpd/vsftpd.conf /etc/vsftpd/vsftpd.conf.backup
vi /etc/vsftpd/vsftpd.conf 
        ## Disable anonymous login ##
    anonymous_enable=NO
        ## Uncomment ##
    ascii_upload_enable=YES
    ascii_download_enable=YES
        ## Uncomment - Enter your Welcome message - This is optional ##
    ftpd_banner=Welcome to UNIXMEN FTP service.
        ## Add at the end of this file ##
    use_localtime=YES


systemctl start vsftpd
systemctl enable vsftpd
# systemctl stop firewalld          # modify to allow incoming trafic from port 21 !
# systemctl disable firewalld       # modify to allow incoming trafic from port 21 !

### useradd iafzal (if the user does not exist). By: Imran Afzal

```
### installation on client
```
sudo yum install ftp -y
```
### transfer file to host
```
### su – iafzal
echo "imp data 123" > kruger

ftp 192.168.56.59
    [ Enter username and password ]
    bi
    hash
    put kruger
    bye
```

### SCP - Secure Copy Protocol ...
Default SCP Port = 22 <br>
transfer file from one host to another
```
scp [source] [destination]
scp file.txt peter@192.168.56.59:/home
```

### rsync - Remote Synchronization - faster SCP
Default Port = 22 <br>
transfer only changes - so it is way faster
```
rpm -qa | grep rsync
yum install rsync

tar cvf backup.tar /home/peter
rsync -zvh backup.tar /tmp      -> backup

rsync -azvh /home/peter /tmp    -> copy dir

rsync -avz backup.tar  peter@192.168.56.59:/tmp     -> copy to remote
```



