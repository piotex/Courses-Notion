# cmp

### cmp - byte by byte
```
diff file1 file2
```
Compare till first different char
Functionality: <br>
    The cmp command compares two files byte by byte and reports the first byte and line where they differ, or it outputs nothing if the files are identical.<br>
Output: <br>
    If the files differ, cmp outputs a message indicating the byte and line where the first difference occurs.<br>

```
cat f1.txt
    ala
    kot
    pies
cat f2.txt
    ala
    pies
    hhh
    aaaa

cmp f1.txt f2.txt
    f1.txt f2.txt differ: byte 5, line 2
```