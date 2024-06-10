# set-static-ip

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

