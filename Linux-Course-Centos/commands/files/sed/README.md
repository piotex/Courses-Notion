# sed

### sed - replace text with text in file
```
sed -i 's/kot/kooooot/g' f2.txt 
    -i  - insert changes to file (without - will print to console) 
    s   - substitute
    g   - global // more that one place


sed -i 's/kot//g' f2.txt    -> will remove 'kot' from file

sed -i '/kot/d' f2.txt      -> will remove whole line that contains 'kot'

sed -i '/^$/d' f2.txt       -> will remove empty lines from file

sed -i '1d' f2.txt          -> will remove first line from file
sed -i '1,2d' f2.txt        -> will remove first two lines from file

sed -i 's/\t/ /g' f2.txt    -> replace TAB with SPACE

sed -n 12,18p f2.txt        -> Print lines [12, ... , 18] (included)
sed -n 12,18p f2.txt        -> Print lines without [12, ... , 18] (12, 18 also excluded)

sed  G f2.txt               -> Add blanck line between original lines

sed 's/aa/Aa/' f2           -> replace aa with Aa (once per line)
sed '8!s/aa/Aa/' f2         -> replace aa with Aa (once per line) except line number 8
```