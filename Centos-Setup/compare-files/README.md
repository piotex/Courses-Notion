# compare-files

### diff - line by line
```
diff file1 file2
```
Compare line to line.
Functionality: <br>
    The diff command is used to compare the content of two files line by line and displays the differences between them. <br>
Output:  <br>
    The output of diff typically shows which lines are different between the two files. It uses a format that shows the differing lines along with symbols indicating additions, deletions, and changes. <br>
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

diff f1.txt f2.txt
    2d1
        < kot
    3a3,7
        > hhh
        > aaaa
        > bbbb
        > kot
        > kot
```

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

