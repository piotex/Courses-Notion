# sendmail

```
# sendmail

```
/etc/mail/sendmail.mc
/etc/mail/sendmail.cf

rpm -qa | grep sendmail
sudo yum install sendmail sendmail-cf -y

systemctl restart sendmail

mail -s "subject line" email@mydomain.com
    mail body
    [Ctrl] D
```
