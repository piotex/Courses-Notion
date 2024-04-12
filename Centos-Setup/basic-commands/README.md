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

### Soft and Hard Links
inode - Pointer or number of a file on the hard disk <br>
Soft link - Link will be removed if file is remved or renamed <br>
Hard link - Deleting, renaming or moving the original file will not affect the hard link
```
hard_link -->-- INODE
                  |-->-- my_file
                           |
soft link ------------>-----
```



```
ln -s original_file link_name    # Create soft link

ln original_file link_name       # Create hard link 
                                 # // like creating a copy of file
```

### Create group and user
```
sudo groupadd group_name                  # Create group
sudo useradd -m -G group_name username    # Create user
                                          # -m - create home dir
                                          # -G add to group
sudo passwd username                      # Set password for user
visudo                                    # Add user to sudo group

sudo chgrp [options] new_group file       # change group ownership of files
```
### Save text to file
```
echo "test text" >  my_file_1.txt   # Override file 
echo "test text" >> my_file_1.txt   # Append text to file
ls -lahrt > lahrt.txt
```
### Show file content
```
cat my_file_1.txt 
```

### sed - replace text with text in file
```
sed -i 's/kot/kooooot/g' f2.txt 
    -i  - insert changes to file (without - will print to console) 
    s   - substitute
    g   - global // more that one place


sed -i 's/kot//g' f2.txt    -> will remove 'kot' from file

sed -i '/kot/d' f2.txt      -> will remove whole line that contains 'kot'

sed -i '/^$/d' f2.txt       -> will remove empty lines from file

sed -i '1d' f2.txt          -> will remove first line from file
sed -i '1,2d' f2.txt        -> will remove first two lines from file

sed -i 's/\t/ /g' f2.txt   -> replace TAB with SPACE
```






