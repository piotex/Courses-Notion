# create-group

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