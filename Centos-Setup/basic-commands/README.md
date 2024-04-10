# basic-commands
### View curent path directory / localization
```
pwd
```
### Change directory 
```
cd /home
cd ../
cd $HOME == cd
```
### Show what is in directory
```
ls 
ll 
ls -la
ls -lahrt
ls -lahrt /home/peter
```

### Get info about host 
```
whoami
hostname
```

### Changing Password
```
passwd userid
    Old pwd
    New pwd
    Retype new pwd
```

### Creating Files
```
touch test.txt
touch test1.txt test2.txt test3.txt 
```
### Copy files / directories
```
cp source.txt dest.txt
cp -R source_dir dest_dir
```
### Edit files
```
vi test.txt
    / - find in text
    w - write
    q - quite
    i - insert
```
### Find files
```
find / -name "*ala*" 
locate + updatedb   ... - find based on local database and cashe 
```
\* - zero or more chars  <br>
? - single char  <br>
[] - range of chars  <br>
\\ - as an escape character <br>
^ - the begining of line <br>
$ - the end of the line <br>

touch abcd{1..9}.txt - will create 9 files

### Creating Directories
```
mkdir folder
mkdir /home/folder
```












