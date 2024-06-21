# docker-instalation

### Install docker
https://docs.docker.com/engine/install/centos/
```
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

sudo yum install docker docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

sudo systemctl start docker

sudo docker run hello-world

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world

docekr ps -a
docker rm c567560547e5
```

