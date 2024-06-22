# create-eks-cluster

manually
```
kubectl create cluster --name eksctl-test --nodegroup-name ng-default --node-type t3.micro --nodes 2

kubectl get all
```

// after setting up cluster, there should be directory with config file for kubectl -> .kube/config

with yaml script
```
eksctl create nodegroup --config-file=eksctl-create-ng.yaml
eksctl create nodegroup --config-file=eksctl-create-cluster.yaml
eksctl get nodegroup --cluster=eksctl-test
```

Delete cluster
```
eksctl get cluster
eksctl delete cluster --name=eksctl-test
```