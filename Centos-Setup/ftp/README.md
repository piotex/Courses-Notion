# FTP - FIle Transfer Protocol
Default FTP Port = 21 <br>

```

Install and Configure FTP on the remote server
• # Become root
• # rpm –qa | grep ftp
• # ping www.google.com
• # yum install vsftpd
• # vi /etc/vsftpd/vsftpd.conf (make a copy first)
• Find the following lines and make the changes as shown below:
• ## Disable anonymous login ##
• anonymous_enable=NO
• ## Uncomment ##
• ascii_upload_enable=YES
• ascii_download_enable=YES
• ## Uncomment - Enter your Welcome message - This is optional ##
• ftpd_banner=Welcome to UNIXMEN FTP service.
• ## Add at the end of this file ##
• use_localtime=YES
• # systemctl start vsftpd
• # systemctl enable vsftpd
• # systemctl stop firewalld
• # systemctl disable firewalld
• # useradd iafzal (if the user does not exist). By: Imran Afzal
www.utclisolutions.com
FTP – File Transfer Protocol
• Install FTP client on the client server
• # Become root
• # yum install ftp
• # su – iafzal
• $ touch kruger
• Commands to transfer file to the FTP server:
• ftp 192.168.1.x
• Enter username and password
• bi
• hash
• put kruger
• bye.
By: Imran Afzal
www.utclisolutions.com
SCP – Sec

```