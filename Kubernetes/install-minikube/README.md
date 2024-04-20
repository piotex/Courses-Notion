# install-minikube

```
sudo yum -y update
sudo yum -y install epel-release
sudo yum -y install libvirt qemu-kvm virt-install virt-top libguestfs-tools bridge-utils

sudo systemctl start libvirtd
sudo systemctl enable libvirtd
sudo systemctl status libvirtd

sudo usermod -a -G libvirt $(whoami)
sudo vi /etc/libvirt/libvirtd.conf
    unix_sock_group = "libvirt"
    unix_sock_rw_perms = "0770"

sudo systemctl restart libvirtd.service
wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo chmod +x minikube-linux-amd64 && sudo mv minikube-linux-amd64 /usr/bin/minikube

minikube version

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client

sudo chmod +x kubectl && sudo mv kubectl /usr/bin/
kubectl version --client -o json
minikube start









minikube stop
minikube restart

kubectl create deployment nginx --image=nginx
kubectl get pods

kubectl create service nodeport nginx --tcp=80:80
kubectl get svc

kubectl get cluster-info


http://192.168.49.2:31922/

```