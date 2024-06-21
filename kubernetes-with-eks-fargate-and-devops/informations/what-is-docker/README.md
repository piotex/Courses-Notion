# what-is-docker

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
