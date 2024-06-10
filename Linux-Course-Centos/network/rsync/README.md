# rsync

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
