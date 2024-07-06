# eks-logging

EKS Control Plane Logging
```
- K8 api
- audit
- authenticator
- controllerManager
- scheduler
```

EKS Worker Nodes Logging
```
- System logs from kubelet, kube-proxy or dockerd
- Application logs from application container

- Containerized application writes to
    - stdout and stderr
- System logs to
    - systemd
- Container redirect logs to /var/log/containers/*.log files    !!!

```

```
node            node            node
|   |           |   |           |   |
pod pod         pod pod         pod pod
-------         -------         -------
    |               |               |
    -----Logging Architecture -------    
                (Abstract)
                    |
                   LOGS

```

```
So the solution is to run pod with LOGGING AGENT like:
- fluentd
- fluentbit etc.
and send logs to ELK, Elasticsearch, CloudWatch, etc.

EFK:
- Amazon Elasticsearch
- fluentd
- kibana
```

```
- fluentbit is beter that fluentd
- fluentd will be deprecated from AWS
```

Logging with fluentbit:
```
- run as single pod on each eks node

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-prerequisites.html
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs-FluentBit.html
- pod IAM Role (IRSA)
```

Logging with promeetheus
```
https://docs.aws.amazon.com/eks/latest/userguide/prometheus.html
```