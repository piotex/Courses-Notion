# Others

```
getfacl my_origin_file.txt
    # file: my_origin_file.txt
    # owner: root
    # group: root
    user::rwx
    group::rwx
    other::rwx
```
```
setfacl .... ?
```
```
man system_commant   # instruction / help
```
```
date
```
```
sudo date -s $(curl -s "http://worldtimeapi.org/api/timezone/Europe/Warsaw" | grep -oE '"datetime":"[^"]+"' | cut -d'"' -f4)
```
