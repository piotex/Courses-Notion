# helm-nginx
https://docs.nginx.com/mesh/get-started/install/install-with-helm/



```
helm repo add nginx-stable https://helm.nginx.com/stable
helm repo update
git clone https://github.com/nginxinc/nginx-service-mesh
cd nginx-service-mesh/helm-chart
helm search repo nginx-stable -l
git checkout v2.0.0
helm install nsm nginx-stable/nginx-service-mesh --namespace nginx-mesh --create-namespace --wait
```
```
kubectl get pods --all-namespaces
kubectl get deployment -o wide --all-namespaces
kubectl get service -o wide --all-namespaces

helm history nsm -n nginx-mesh


```

