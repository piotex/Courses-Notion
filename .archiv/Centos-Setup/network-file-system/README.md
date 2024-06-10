# network-file-system (NFS)

```
===== On Server Host ===================================
yum install nfs-utils libnfsidmap

systemctl enable rpcbind
systemctl enable nfs-server
systemctl start rpcbind, nfs-server, rpc-statd, nfs-idmapd

mkdir /shared_dir
chmod a+rwx /shared_dir

vi /etc/exports
    /shared_dir     192.168.56.57(rw,sync,no_root_squash)               //for only 1 host
    /shared_dir     *(rw,sync,no_root_squash)                           //for all hosts

exportfs -rv

===== On Client Host ===================================
yum install nfs-utils rpcbind
systemctl start rpcbind                     // enable and start rpcbind
systemctl enable rpcbind                    // enable and start rpcbind
ps -ef | egrep "firewall|iptable"           // make sure firewall stopped
showmount -e 192.168.56.59                  // NFS Server IP
mkdir /mnt/shared_dir
mount 192.168.56.59:/shared_dir /mnt/shared_dir
df -h
umount /mnt/shared_dir
```
