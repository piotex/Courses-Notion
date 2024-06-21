# useful-commands

### Install oc
```
sudo usermod -aG docker $USER
wget https://github.com/openshift/origin/releases/download/v3.9.0/openshift-origin-client-tools-v3.9.0-191fece-linux-64bit.tar.gz
tar -zvxf openshift-origin-client-tools-v3.9.0-191fece-linux-64bit.tar.gz
cd openshift-origin-client-tools-v3.9.0-191fece-linux-64bit
sudo cp oc /usr/local/bin/
oc version
```

### ocp login
```
OpenShift page > Question mark > Command Line Tools > Copy login command

oc login --token=sha256-tocken --server=https://oc-server.com:6443

oc project my-project
```

### docker login to imagestream
```
sudo docker login -u `oc whoami` -p `oc whoami -t` oc-server.com/my-project
```

### docker push image to imagestream
```
docker image tag c0d82e1ec9e8 oc-server.com/my-project/jenkins2460:latest

sudo docker push oc-server.com/my-project/jenkins2460:latest
```