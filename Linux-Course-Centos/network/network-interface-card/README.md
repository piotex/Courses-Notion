# network-interface-card

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

