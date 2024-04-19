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


```








```
helm version
helm repo add datahub https://helm.datahubproject.io
helm repo update
helm search repo datahub -l


```