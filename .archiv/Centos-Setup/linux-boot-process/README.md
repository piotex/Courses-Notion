# linux-boot-process

```
Older version:
BIOS    -> Basic Input/Output System, executes MBR
MBR     -> Master Boot Record, executes GRUB
GRUB    -> Grand Unified Bootloader, executes Kernel
Kernel  -> Kernel, executes /sbin/init
Init    -> Init, executes runlevel programs
Runlevel-> Runlevel programs are executed from /etc/rc.d/rd*.d 
```
```
Newer version:
BIOS    -> Basic Input/Output System;       firmware interface
MBR     -> Master Boot Record;              Information saved in first sector of a hard disk that indicates where the GRUB2 is located so it can be loaded in computer RAM
GRUB2   -> Grand Unified Bootloader;        Loads Linux kernel /boot/grub2/grub.cfg
Kernel  -> Kernel;                          Core of Operating System, loads required drivers from initrd.img, starts the first OS process (systemd)
Systemd -> System Daemon (PID #1);          It then starts all the required processes, Reads /etc/systemd/system/default.target to bring the system to the run-level (0-6)
```
