# network-basics

### terms to know
```
IP
Subnet mask
Gateway
Static vs. DHCP

Interface
Interface MAC
```

### Interface configuration files
```
/etc/nsswitch.conf
/etc/hosts                          // or hostname
/etc/sysconfig/network
/etc/sysconfig/network-scripts/ifcfg-nic
/etc/resolv.conf                    // dns server
```

### basic network commands
```
ping
ifconfig
ifup or ifdown
netstat -rnv
tcpdump -i enp0s3
```

### NIC = Network Interface Card 
example: enp0s3 <br>
lo = loopback device <br>
virb0 = Virtual Bridge 0 - is used for NAT (Network Address Translation) - to connect to outside network (sometimes)

```
ethtool enp0s3
```

### NIC Bonding Procedure - for redundancy (in case if one network addapred dies) and higher spead (1G + 1G = 2G)
```
modprobe bonding 
modinfo bonding 
Create /etc/sysconfig/network-scripts/ifcfg-bond0 
Edit /etc/sysconfig/network-scripts/ethernet1 
Edit /etc/sysconfig/network-scripts/ethernet2 
Restart network = systemctl restart network

nicl ---------> bond0 
nic2 -----^
```





