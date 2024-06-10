# recover-root-password

### recover-root-password
```
1. restart your computer
2. edit grub
        just before start - Press E
        line with: linux16 /vim... root=/dev... ro ...
        remove ro and type .... some text...? [in Centos 9 go to end of the line and after 'rhgb quiet' type 'rd.break' and press [Ctrl] X ]
3. change password
        chroot /sysroot
        touch /.autorelabel
4. reboot
```