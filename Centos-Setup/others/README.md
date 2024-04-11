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
```

[root@localhost tmp]# telnet example.com 80
    Trying 93.184.216.34...
    Connected to example.com.
    Escape character is '^]'.

        GET / HTTP/1.1
        Host: example.com
        ^

    HTTP/1.1 400 Bad Request
    Content-Type: text/html
    Content-Length: 349
    Connection: close
    Date: Wed, 10 Apr 2024 23:28:44 GMT
    Server: ECSF (sed/58AA)

    <?xml version="1.0" encoding="iso-8859-1"?>
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
            <head>
                    <title>400 - Bad Request</title>
            </head>
            <body>
                    <h1>400 - Bad Request</h1>
            </body>
    </html>
    Connection closed by foreign host.

```

### see output and save to file - tee
```
ifconfig | tee ifconfig.txt
ifconfig | tee -a ifconfig.txt   # append

```

### calculate number of chars in text
```
wc -c ifconfig.txt
```
### calculate number of lines in text
```
wc -l ifconfig.txt
```
### pipes - combining commands
```
ls -al /etc | more
ls -la | tail -n 5
```
### copy files
```
cp source destination
cp -p source dest          # copy with permitions

scp /tmp/file.txt user@host:/tmp/directory
```
### display file 
```
cat
more
less

head
tail
```

### truncate - cut content of file 
```
cat f1.txt
        ala
        kot
        pies
        kot
truncate -s 10 f1.txt
cat f1.txt
        ala
        kot
        pi
```

# combining files
```
cat file1 file2 file3 > file4
```

# spliting file
```
split -l 300 file.txt childfile
        -l  - split file into 300 lines per file to childfileaa, childfileab
```