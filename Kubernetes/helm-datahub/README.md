# helm-datahub
https://github.com/acryldata/datahub-helm


```
kubectl create secret generic mysql-secrets --from-literal=mysql-root-password=datahub --from-literal=mysql-password=datahub
kubectl create secret generic neo4j-secrets --from-literal=neo4j-password=datahub --from-literal=NEO4J_AUTH=neo4j/datahub

helm repo add datahub https://helm.datahubproject.io/

helm install prerequisites datahub/datahub-prerequisites

kubectl get pods

helm install datahub datahub/datahub

kubectl get pods

kubectl port-forward <datahub-frontend pod name> 9002:9002

sudo systemctl start firewalld
sudo firewall-cmd --zone=public --add-port=9002/tcp --permanent
sudo firewall-cmd --reload

```
```
kubectl get pods --all-namespaces
kubectl get deployment -o wide --all-namespaces
get service -o wide --all-namespaces

helm history nsm -n nginx-mesh


helm search repo datahub
helm show values datahub/datahub
```



```
helm repo add jenkins https://charts.jenkins.io
helm repo update

helm search repo jenkins
helm upgrade --install myjenkins jenkins/jenkins
kubectl exec --namespace default -it svc/myjenkins -c jenkins -- /bin/cat /run/secrets/chart-admin-password && echo
kubectl --namespace default port-forward svc/myjenkins 8080:8080
kubectl describe pod myjenkins
helm show values jenkins/jenkins
```



helm install jenkins jenkins/jenkins --version 2.200.3





```
helm version
helm repo add datahub https://helm.datahubproject.io
helm repo update
helm search repo datahub -l


```

```

kubectl apply -f https://k8s.io/examples/service/load-balancer-example.yaml
kubectl get deployments hello-world
kubectl expose deployment hello-world --type=LoadBalancer --name=my-service --port=9090
kubectl get services my-service
kubectl describe services my-service

kubectl get pods --output=wide
kubectl describe services my-service
kubectl describe services my-service | grep Load
kubectl describe deployments hello-world
kubectl get replicasets

kubectl delete services my-service
kubectl delete deployment hello-world

```