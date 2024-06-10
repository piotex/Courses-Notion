# input-output-redirects

|   |   |   |
|---|---|---|
| stdin | Standard input | decryption number as 0 |
| stdout | Standard output | decryption number as 1 |
| stderr | Standard error | decryption number as 2 |

### stdin
```
grep "Apr 10" < lahrt.txt
```

### stdout
```
ls -la > la_la.txt
cat la_la.txt
```

### stderr
```
telnet localhost 2> error.txt
```
