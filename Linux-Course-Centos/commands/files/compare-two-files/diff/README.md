# diff

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