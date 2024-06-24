# eks-managed-nodegroups

```
- Feature available only for EKS

EKS Managed Nodegroups:
- Create and Manage EC2 Workers for you
- Amazon releases AMIs with bug fox, security patches for EKS Worker Nodes
   - Or bring your own custom AMI
- Automated deployment of updated AMIs with security patches 
   - No app downtime
   - No overhead of user managed orchestration
   - Auto scaling group is used behind the scenes
```

Demo
```
eksctl create cluster --name demoeks --version 1.14 --nodegroup-name demoeks-nodes --node-type t3.micro --nodes 4 --managed

kubectl get all

kubectl apply -f nginx-deployment.yaml

kubectl get all

eksctl nedegroup --name=managed-ng-1 --cluster=managed-cluster

kubectl get pods
kubectl get nodes 
```