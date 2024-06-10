# system-updates

```
yum - when download package from internet
rpm - when have localy a package
```
```
yum install ntp -y
yum install httpd -y

```
```
rpm -qa | grep httpd            -> find if package is installed

rpm -ihv /tmp/package.rpm       -> install downloaded package
rpm -e package-name-from-qa     -> remove package / uninstall

```

### system upgrade / Patch management
```
ver:    7.3
        | |
    Major Minor
```
```
Major cant be updated
Minor can be updated with:

yum update -y
update  - preserve/save older versions 
upgrade - delete older versions

```

### create local repo - dvd / iso
```
createrepo 

/etc/yum.repos.d
```

### rolback updates
```
yum history
yum history undo <id- last id>
```
