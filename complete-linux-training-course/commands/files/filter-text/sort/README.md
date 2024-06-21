# sort

### sort - sort in alphabetic order
```
cat lahrt.txt | sort 
    -r   - reverse order
    -k2  - sort by 2 word
cat lahrt.txt | sort -k2 | awk '{print $2}'
```
