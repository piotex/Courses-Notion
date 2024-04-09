# file-system-structure


  <br/>

  <br/>

  <br/>

  <br/>

  <br/>

/opt  <br/>

/proc  <br/>
/lib → usr/lib  <br/>
strace -e open pwd <br/>

/tmp  <br/>






| Command | Description | 
|----------|----------|                                   
| afs | |
| bin -> usr/bin | Everyday user commands e.g. pwd |
| boot | Contains file that is used by the boot loader (grub.cfg)  |
| data |                                                 |
| dev | System devices (e.g. disk, cdrom, flashdrive, keyboard etc.)  |
| etc | Configuration files                 |
| home | Directory for user  |
| lib -> usr/lib |   C programming library files needed by commands and apps  |
| lib64 -> usr/lib64 | |
| media | For cdrom mounts. |
| mnt | To mount external filesystem. (e.g. NFS) |
| opt | Optional add-on applications (Not part of OS apps)  |
| proc | Running processes (Only exist in Memory)  |
| root | root user home directory. It is not same as /  |
| run | System daemons that start very early (e.g. systemd and udev) to store temporary runtime files like PID files  |
| sbin -> usr/sbin |  System/filesystem commands |
| srv | |
| sys | |
| tmp | Directory for temporary files |
| usr | |
| var | System logs  |
