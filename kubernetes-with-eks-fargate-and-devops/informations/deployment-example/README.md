# deployment-example

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    environment: test
  name: test
spec:
  replicas: 3
  selector:
    matchLabels:
      environment: test
  template:
    metadata:
      labels:
        environment: test
    spec:
      containers:
      - image: nginx:1.16
        name: nginx
```

```
- resources are managed by labels
```

Deployment with rolling update
```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    environment: test
  name: testdeploy
spec:
  replicas: 3
  selector:
    matchLabels:
      environment: test
  minReadySeconds: 10
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
    type: RollingUpdate
  template:
    metadata:
      labels:
        environment: test
    spec:
      containers:
      - image: nginx:1.16
        name: nginx
```