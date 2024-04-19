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

### network configuration with tools
//Bond & Team - redundancy <br>
// 
``` 
nmcli                   -> clinmtui
nmtui                   -> console tool to manage network (interactive mode)
nm-connection-editor    -> works only on gui.... no console
```

### set static ip
```
nmcli device
ping 10.10.10.10                                            -> should not be pingable
nmcli connection modify enp0s3 ipv4.addresses 10.10.10.10
nmcli connection modify enp0s3 ipv4.gateway 10.10.10.1/24
nmcli connection modify enp0s3 ipv4.method manual
nmcli connection modify enp0s3 ipv4.dns 8.8.8.8
nmcli connection down enp0s3 
nmcli connection up enp0s3 
ip address show enp0s3
```

### add new static ip
```
nmcli device status
nmcli connection show -active
ping 10.10.10.11                                            -> should not be pingable
nmcli connection modify enp0s3 +ipv4.addresses 10.10.10.11/24
nmcli connection reload 
systemctl reboot
ip address show 
```

### Bridged
```
laptop--------internet
         |
host-----|
```

### Host-only
```
laptop----------internet

laptop---|
         |
host-----|
```

