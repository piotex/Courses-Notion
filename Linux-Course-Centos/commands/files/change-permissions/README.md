# change-permissions

### Permissions

| - | rwx | rwx | rwx |
|---|-----|-----|-----|
| file/type | users | groups | others |

<br> 

**sticky** bit - last bit (for example in -rwxrwxrwt it is 't' and in this case it prevent from deleting this directory)

```
chmod +t /my/dir
```

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
