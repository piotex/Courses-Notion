# cut 

### cut part of lines from file or pipe
```
cut -c1 file.txt                # return first char of each line in file.txt
cut -c1,2,3,5,7 file.txt        # return chars from selected indexes
cut -c1-7 file.txt              # return chars from range
cut -b1-7 file.txt              # return butes from range
cut -d: -f 6 /etc/passwd        # return 6th string separated by :  // : can be other char
ls -al | cut -c2-4
```

