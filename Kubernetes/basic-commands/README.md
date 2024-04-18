# basic-commands
```
kind create cluster --name multi-node --config=multi-node.yaml

kubectl get pods --all-namespaces

kubectl logs nazwa_poda -n nazwa_namespace
```



```
kubectl create deploy web-deployment-v1 --image=nginx --port=80
kubectl get deployment -o wide
kubectl get pods -o wide
kubectl logs web-deployment-v1-86f768cfb6-5gt4k


```

### basic deployment
https://medium.com/@dahmearjohnson/a-simple-kubernetes-deployment-eabc0a5a91dc