# ls-properties

[root@localhost /]# ls -lahrt

| Type / Permitions  | # of Links | Owner | Group | Size | Month | Day | Time | Name         |
|-------------|-----|------|-----|-------|----|----|--------|--------------------|
| drwxr-xr-x. |   2 | root | root|     6 | Aug|   9|   2021 | srv                |
| lrwxrwxrwx. |   1 | root | root|     8 | Aug|   9|   2021 | sbin -> usr/sbin   |


### Permisions
d - directory <br/>
l - link <br/>
[nothing] - file <br/>
<br/>
<br/>
<br/>

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

