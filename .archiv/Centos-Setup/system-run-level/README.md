# system-run-level

```
Main Run Levels:
0 - Shut down (or halt) the system
1 - Single-user mode; usually aliased as s or S
6 - Reboot the system

Other Run Levels:
2 - Multiuser mode without networking
3 - Multiuser mode with networking
5 - Multiuser mode withnetworking and GUI
```

### Check current run-level
```
sudo who -r
```

### Change run-level (it will reboot machine)
```
init 3
```
