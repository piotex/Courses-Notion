# k8s-scaling

```
          Trafic
            |
           svc
            |
         Amazon EKS
    (Auto Scaling group)
            |
            -------------------
            |                 |
deploy ->   Amazon EC2     Amazon EC2
hpa    ->   -----------------
            |       |       |
           pod     pod     pod

hpa - horizontal pod autoscaler
    - if cpu in pod is over threshold, 
      it will create new pod
    
Auto Scaling group 
    - if cpu in EC2 is over threshold,
      it will create new node
```

```
m5.large:
vCPU: 2
Memory (GiB): 8
```
```
1 vCPU = 1000m (milicore)
500m = Half of 1 vCPU
0.5  = Half of 1 vCPU
1    = 1 vCPU
```
```
256Mi = 256 MiB
```
```
cpu: 500m
memory: 256Mi
```

https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/

Example deployment:
```
eksctl create cluster

kubectl get all
kubectl get deployment metrics-server -n kube-system

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.7.1/components.yaml
kubectl get deployment metrics-server -n kube-system

kubectl apply -f cluster-autoscaler-deployment-1.yaml
kubectl get all
```
Generate load:
```
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
  Ctrl + C
  exit
```

Delete cluster:
```
eksctl get cluster
eksctl delete cluster --name=adorable-mushroom-1582352352
```

EKS Cluster Autoscaler Demo:
```
- Cluster Autoscaler has two components:
  - Open Source Cluster Autoscaler
  - EKS Implementation (AutoScalerGroup, IAM, etc.)
- Deploy App
- Node scale
```

Demo:
```
eksctl create cluster --name my-cluster --version 1.15 --managed --asg-access 
kubectl apply -f https://raw.githubusercontent.com/kubernetes/autoscaler/master/cluster-autoscaler/cloudprovider/aws/examples/cluster-autoscaler-autodiscover.yaml
kubectl -n kube-system annotate deployment.apps/cluster-autoscaler cluster-autoscaler.kubernetes.io/safe-to-exict="false"
kubectl -n kube-system edit deployment.apps/cluster-autoscaler
    APP-NAME -> my-cluster
    add bellow:
      - --balance-similar-node-groups
      - --skip-nodes-with-system-pods=false
  [ESC] + w + q + [ENTER]
kubectl -n kube-system set image deployment.apps/cluster-autoscaler cluster-autoscaler=k8s.gcr.io/cluster-autoscaler:v1.15.6
kubectl -n kube-system logs -f deployment.apps/cluster-autoscaler
```

Horizontal scaling
```
- ok
- more pods / nodes
```

Vertical scaling
```
- not ok - shut down node and create new one with higher version 
- more resources
```