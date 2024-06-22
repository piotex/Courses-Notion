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