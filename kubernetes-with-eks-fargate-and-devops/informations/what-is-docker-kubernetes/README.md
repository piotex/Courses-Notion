# what-is-docker-kubernetes

Container
```
A container is an atomic, self contained package of software that includes everything it needs to run 
- code
- runtime (npm, pip, proxy, etc.)
- libraries
- packages
- etc.
```

Big Picture
```
        Dockerfile                              Deploy Into                                  |- Amazon EKS
Your  ---------------> Docker ---> Repository ----------------> Container --- K8s Cluster ---|- Google Kubernetes Engine
App                    Image        - Docker Hub                              (Kubernetes)   |- K8s on Ec2
                                    - ECR (Elastic                                           |- ... 
                                    Container Registry)

```

Virtual Machines vs Container
```
Virtual Machines:
- abstraction of physical hardware turning one server into many servers
- hypervisor allows to run multiple machines on one server
- prealocate resources like RAM
- have to have Guest Operating System

App1            App1
Bins/Libs       Bins/Libs
Guest OS        Guest OS
=== === Hypervisor === ===
=== === Host OS      === ===
=== === Server (Host) === ===
```

```
Containers:
- abstraction of application layer that packages code and dependencies together
- multiple containers can run on same machine and share resources like RAM
- take way less space

App1            App1            App1
Bins/Libs       Bins/Libs       Bins/Libs
=== === === === Docker    === === === ===
=== === === === Host OS    === === === ===
=== === === === Server (Host) === === === ===
```

Tasks Associated with containers
```
- Deployment of Containers
- Redundancy and availability of Containers
- Scaling up or down of Containers
- Load Balancing
- Health Monitoring
```

Container Orchestrators
```
- Docker Swarm
- Apache Mesos
- AWS ECS (Elastic Container Service)
- Kubernetes (AWS EKS)
- AWS Fargate
```

What is Kubernetes
```
Architecture:
- master 
- nodes (lot of nodes)

                MASTER
                  |
        ---------------------
        |         |         |
       node      node      node
        |
    ---------
    |        |
   pod      pod
    |
  ---------------
  |             |
container     container 


Master (Control Plane) 
- manages
- monitors
- plans
- schedules nodes

Components of Master (Code Plane)
- etcd - (database) Key Value Store for critical cluster info
- sched - (kube scheduller) Puts containers to proper nodes
- c-m (kube controler manager) Ensures proper state of cluster components 
                               (for example, bring node up so current state = desired state)
- api (kube api server) Exposes Kubernetes API (to communicate with master)
```
```
Manifest file - file  that informs kubernetes what is the desired state 
```

Nodes
```
- node must have installed 
   - Container Runtime Engine - for example Docker
   - kubelet - agent that is running in node and report to master about state of node and containers
             - master communicate with node using kubelet
   - kube-proxy - is used to enable network communication between nodes/containers 

```

Pods
```
- Pods are the smallest deployable units of computing that can be created and managed in Kubernetes,
- Smallest object you can creaet in Kubernetes
- Has unique IP address inside cluster and other pods can talk to this pod by this address

```

Service
```
- distribute network trafic to pods
- it automaticaly detect if pod is down or it was created new pod (based on label selector)
- like load-balancer
- types of service:
   - LoadBalancer
   - ClusterIP - is accessible only inside cluster
   - Nodeport - by combining node IP address and nodeport port numer we can access pod
```

Declarative vs Imperative
```
Declarative - create manifest file and run kubectl apply                         - good - Infra as Code
Imperative  - run manually all kubectl comands to get same result as Declarative - not good
```
