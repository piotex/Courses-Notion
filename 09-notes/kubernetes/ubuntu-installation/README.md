# ubuntu-instalation

### HomeBrew installation on Ubuntu 20.04 Linux
```
sudo apt update
sudo apt-get install build-essential
reboot
```
### Install Git on Ubuntu 20.04
```
sudo apt install git -y
```
### Run Homebrew installation script
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### Add Homebrew to your PATH
```
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```
### Check Brew is working fine
```
brew doctor
brew install gcc
```
### Installation
```
brew install kind
```
### Create a Kubernetes cluster with Kind
```
kind create cluster
```
### Install kubectl
```
snap install kubectl --classic
```
### 
```
kubectl get nodes
kind create cluster --name abc
kind create cluster --name multi-node --config=multi-node.yaml
```







### Uninstall it from Linux
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```