# curl-proxy

curl -L -s https://dl.k8s.io/release/stable.txt --proxy proxy.url.com:80 
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt --proxy proxy.url.com:80 )/bin/linux/amd64/kubectl" --proxy proxy.url.com:80 