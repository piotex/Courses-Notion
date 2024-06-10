# telnet

### telnet
```
sudo yum install telnet -y
```

```
[root@localhost tmp]# telnet example.com 80
    Trying 93.184.216.34...
    Connected to example.com.
    Escape character is '^]'.

        GET / HTTP/1.1
        Host: example.com
        ^

    HTTP/1.1 400 Bad Request
    Content-Type: text/html
    Content-Length: 349
    Connection: close
    Date: Wed, 10 Apr 2024 23:28:44 GMT
    Server: ECSF (sed/58AA)

    <?xml version="1.0" encoding="iso-8859-1"?>
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
            <head>
                    <title>400 - Bad Request</title>
            </head>
            <body>
                    <h1>400 - Bad Request</h1>
            </body>
    </html>
    Connection closed by foreign host.

```