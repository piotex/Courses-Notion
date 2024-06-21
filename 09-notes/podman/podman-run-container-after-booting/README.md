# podman-run-container-after-booting

```
podman generate systemd --new --files --name httpd

cp /root/container-httpd.service /etc/systemd/system

systemctl enable container-httpd.service
systemctl start container-httpd.service
systemctl status container-httpd.service
```

