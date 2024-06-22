# pod-limits-in-node

https://github.com/awslabs/amazon-eks-ami/blob/main/templates/shared/runtime/eni-max-pods.txt

```
Number of pods that can run on a node is limited by the EC2 instance type.
```
```
eksctl create cluster --name pod-test --version 1.15 --node-type t3.micro --nodes 2

kubectl get ns
kubectl get pods -n kube-system
```
```
kubectl apply -f nginx-deployment.yaml
kubectl get all
```

if we change replica to 10, not all pods will be running!
```
kubectl get pods
kubectl describe pod pod_name
```