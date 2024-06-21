# file-system-repair

```
df -h | awk '{print $1}'
df -hT | awk '{print $1, "   ", $2}' | column -t

umount /data
# fsck /dev/sdb1
xfs_repair /dev/sdb1
echo $?
    0 - no error
    1 - filesystem errors corrected
    2 - system should be rebooted
    ...
mount /dev/sdb1 /data

df -h
```