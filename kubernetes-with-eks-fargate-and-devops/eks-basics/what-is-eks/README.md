# what-is-eks

What is EKS
```
- AWS manage Kubernetes Control Plane 
   - High Availability - Multiple EC2 in Multiple AZs
- AWS Detects and Replaces Unhealthy Control Plane Instances
- AWS Scales Control Plane
- AWS Maintain etcd (Key Value Store for critical cluster info)
- Provides Automated Version Upgrade and Patching
- Integrated with AWS Ecosystem (IAM Roles etc.)
```

EKS Data Plane
```
AWS EC2 - Self Managed Node Groups
- You maintain worker EC2s
- You orchestrate version upgrade, security patching, AMI Rehydration, keeping pods up during upgrade
- Can use custom AMI

AWS EC2 - Managed Node Groups
- AWS manages worker EC2s
- AWS provides AMI with security patches version upgrade
- AWS manages pod disruption during upgrade
- Doesn't work with custom AMI

AWS Fargate
- No worker EC2 whatsoever!
- You define and deploy pods
- Container + Serverless!
```

AWS Services which goes with EKS:
```
- AWS Secret Manager
- Elastic LoadBalancer
- Amazon CloudWatch
- AWS CodePipeline
- IAM (AWS Identity and Access Management)
- Amazon API Gateway
```

EKS High Level Architecture
```
        |   Availability    |    Availability
        |      Zone 1       |      Zone 2
--------|---------------------------------------
AWS     |   Amazon EC2      |    Amazon EC2
Managed |  master + etcd    |   master + etcd
--------|---------------------------------------
Customer|   EC2 Instances   |   EC2 Instances
Account |       node        |       node
        |                   |
```
```
                                AWS deploys and
                                 manages master

DevOps ---------------> EKS --->     master         <----  Other DevOps
          Provision                EC2    EC2           - keep using k8s tools you know!
         EKS Cluster               EC2    EC2           - kubectl
                                                        - Prometheus, grafana, fluentd
                                Add worker nodes          cloudhealth, jenkins, gitlab, etc.
                                   to cluster        (all because EKS provides opensource Kubernetes)
```

Pricing of EKS
```
master - 72$/Month
+
EC2 node costs 
    for example:
    EC2 m5.large x3 = 210.24$/Month
    + EBS 30GB      = 9$/Month

total: 291.24$/mo
```

Ways To Spin Up EKS Cluster
```
- AWS Console
- CloudFormation
- AWS CLI
- eksctl CLI


    Local PC         AWS Cloud9       Amazon EC2
(using AWS Creds)    (Terminal)      (Comand line)
                                     (bastion host)
```

DevOps Tools
```
- Jenkins
- Gitlab
- Code Pipeline
- etc.
```

What is eksctl?
```
- CLI tool for creating cluster on EKS
- Easier than console?
- Abstracts lots of stuff - VPC, Subnet, Sec. Group, etc.
  Using CloudFormation
```

eksctl Commands
```
-----------------------------------------------------------------------
eksctl create cluster                   |      Create EKS cluster 
                                        |     with one nodegroup containing
                                        |       2 m5.large nodes
-----------------------------------------------------------------------
eksctl create cluster                   |      Create EKS cluster 
    --name <name>                       |     with K8 version 1.15 
    --version 1.15                      |     with 2 t3.micro nodes
    --node-type t3.micro                |
    --nodes 2                           |
-----------------------------------------------------------------------
eksctl create cluster                   |      Create EKS cluster 
    --name <name>                       |   with managed node group
    --version 1.15                      |
    --nodegroup-name <node-grp-name>    |
    --node-type t3.micro                |
    --nodes 2 --managed                 |
-----------------------------------------------------------------------
eksctl create cluster                   |      Create EKS cluster 
    --name <name>                       |   with Fargate Profile
    --fargate                           |   
-----------------------------------------------------------------------
```

Available eksctl features (Only on EKS)
```
- Create, get, list and delete clusters
- Create, drain and delete nodegroups
- Scale a nodegroup
- Update a cluster
- Use custom AMIs
- Configure VPC Networking
- Configure access to API endpoint
- Support for GPU nodegroups
- Spot instances and mixed instances
- IAM Management and Add-on Policies
- List cluster Cloudformation stacks
- Install coredns
- Write kubeconfig file for a cluster
```

```
kubectl works on all Kubernetest clusters

eksctl work only on EKS cluster
```

What is kubectl?
```
- CLI for running commands against a cluster on K8s resources
- Communicate via cluster API Server
- Works for any K8s cluster - EKS K8s on EC2, GKE (google), etc.
```

kubectl Command Syntax
```
kubectl     [command]           [type]                   [name]                   [flags]
                |                 |                         |                        |
              create       (any K8 resource type)      (optional)                (optional)
               get           pods / pod / po         name of the resource.     --filename / -f
             describe        namespaces / ns        if omitted, all resource     --output / -o
              delete       deployments / deploy      details displayed
              apply         replicasets / rs
              attach            etc.
             autoscale
               etc.
```
```
kubectl get pod pod1    - return info about single pod
kubectl get pod         - return info about all pods
kubectl get po          - same as previous command 
kubectl get po -o yaml  - return more info in yaml format
```

