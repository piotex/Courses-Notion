# ssh

### HOST
```
useradd jenkins_agent
passwd jenkins_agent

usermod -aG test_group jenkins_agent

sudo visudo
    jenkins_agent ALL=(ALL) NOPASSWD:ALL

sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
```

### MASTER
```
ssh-keygen -t rsa -b 2048 -C "jenkins_agent@192.168.56.57"
    /home/peter/.ssh/id_rsa-jenkins_agent@192.168.56.57
ssh-copy-id -i /home/peter/.ssh/id_rsa-jenkins_agent@192.168.56.57 jenkins_agent@192.168.56.57
```