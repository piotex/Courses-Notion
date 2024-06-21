# move-process-to-the-background

### Update
```
sudo yum check-update
sudo yum update -y          # don't remove old packages
sudo yum upgrade -y         # remove old packages
sudo reboot
```

# Move process to the background
```
sleep 100
    [Ctrl] Z
        bg
sleep 100 &

ps -ef | grep sleep


bg                       -> move process to background 
fg                       -> move process to front 

nohup sleep 75 &         -> detached from user parrent process // ignore closing terminal
jobs
more nohup.out
```