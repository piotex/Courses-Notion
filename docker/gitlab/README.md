# docker-gitlab

```
sudo su docker && export GITLAB_HOME=/data/gitlab && exit

sudo docker run --detach   --hostname gitlab.example.com   --env GITLAB_OMNIBUS_CONFIG="external_url 'http://gitlab.example.com'"   --publish 7443:443 --publish 7080:80 --publish 7022:22   --name gitlab   --restart always   --volume $GITLAB_HOME/config:/etc/gitlab   --volume $GITLAB_HOME/logs:/var/log/gitlab   --volume $GITLAB_HOME/data:/var/opt/gitlab   --shm-size 256m   gitlab/gitlab-ee:15.10.3-ee.0

sudo docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```

# instal on centos
https://www.server-world.info/en/note?os=CentOS_Stream_9&p=gitlab