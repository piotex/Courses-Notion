# ec2-scaling

```
Trafic
|
Application Load Balancer
|
Auto Scaling Policy
(Scalle if CPU > 50%)
(based on CloudWatch Metrics)
|
Auto Scaling Group
-------------------
| Amazon | Amazon |
| EC2    | EC2    |
-------------------

```


