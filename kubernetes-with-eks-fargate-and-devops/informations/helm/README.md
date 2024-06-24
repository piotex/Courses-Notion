# helm

```
- it's like manage multiple manifest files with one file

- Helm is package manager for Kubernetes
- Helm packages are called Charts
- Helm Charts help define, install and update complex Kubernetes application
- Helm Charts can be versioned, shared and published
- Helm Charts can accept input parameter
  - kubectl need template engine to do this
- Popular packages already available
```
```
Helm Hub - for templates
```

Charts Files
```
metadata            |   Chart.yaml
default config      |   values.yaml
manifest templates  |   templates/'
                            service.yaml
                            deployment.yaml
```

Helm nginx demo
```
(helm installation)
helm version

helm search repo nginx  -> search local repo
helm search repo nginx  -> search remote repo

helm repo add bitnami https://charts....

helm pull bitnami/nginx --untar=true

kubectl get all

helm install helm-nginx bitnami/nginx


kubectl get all
kubectl get service
kubectl get service
kubectl describe service
kubectl get svc


```




