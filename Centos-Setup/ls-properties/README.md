# ls-properties
```
[root@localhost /]# ls -lahrt
```

| Type / Permitions  | # of Links | Owner | Group | Size | Month | Day | Time | Name         |
|-------------|-----|------|-----|-------|----|----|--------|--------------------|
| drwxr-xr-x. |   2 | root | root|     6 | Aug|   9|   2021 | srv                |
| lrwxrwxrwx. |   1 | root | root|     8 | Aug|   9|   2021 | sbin -> usr/sbin   |


### Permisions

|  |  |  
|-----|-----|
|  d  | directory |
|  l  | link | 
|  -  | file |


### Change permisions
```
chown user:group file_or_dir
chmod 777 file_or_dir 
```

|  |  |  |
|-----|-----|-----|
|  r  | read | 4  |
|  w  | write | 2  |
|  x  | execute | 1  |

7 = 4 + 2 + 1

### Time 
Month | Day | Time -> creation time


### Absolute vs Relative Path
Absolute Path:
```
cd /var/log/samba
```
Relative Path:
```
cd /var
cd log
cd samba
```

