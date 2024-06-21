# link-soft-hard

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