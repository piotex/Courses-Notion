# login-message-autorun-commands

```
Message that appear after login to machine

vi /etc/motd
```
```
Commands that runs after login

vi /etc/profile.d/motd.sh
    #!/bin/bash
    echo -e "
    ############################
    # Welcome to `hostname`
    # Time: `date`
    ############################
    "

//Optional?
vi /etc/ssh/sshd_config
    #PrintMotd yes -> PrintMotd no

systemctl restart sshd.service
```