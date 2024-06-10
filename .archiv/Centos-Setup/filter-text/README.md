# filter-text

### cut - cut part of lines from file or pipe
```
cut -c1 file.txt                # return first char of each line in file.txt
cut -c1,2,3,5,7 file.txt        # return chars from selected indexes
cut -c1-7 file.txt              # return chars from range
cut -b1-7 file.txt              # return butes from range
cut -d: -f 6 /etc/passwd        # return 6th string separated by :  // : can be other char
ls -al | cut -c2-4
```

### aws - utility for data extraction
```
awk '{print $1}' file                           # print first column/word in file
ls -al | awk '{print $3}'
ls -al | awk '{print $1, $3}'                   # print first and third column
ls -al | awk '{print $NF}'                      # print last column
ls -al | awk '{print NF}'                       # print how much items are in result
ls -al | awk '/my_origin/ {print}'              # print rows with my_origin in this row
awk -F: '{print $1}' /etc/passwd                # print first element, separated by :
echo "Hello Tom" | awk '{$2="Adam"; print $0}'  # override/print second word with Adam
ll | awk 'length($0) > 100'                     # print lines longer that 100 chars
ll | awk '{if($9 == "error.txt") print $0;}'    # print line with error.txt as file name

```

### grep - filter
```
grep keyword file
cat lahrt.txt | grep X
    -c  - search for key and count
    -i  - search for key and ignore case-sensitive
    -n  - display mached lines and their line number
    -v  - display everything but keyword
```

### egrep - search for 2 keywords or more
```
cat lahrt.txt | egrep -i " 8|my"
cat lahrt.txt | egrep -i " 8 | 9 | 6 "
```

### sort - sort in alphabetic order
```
cat lahrt.txt | sort 
    -r   - reverse order
    -k2  - sort by 2 word
cat lahrt.txt | sort -k2 | awk '{print $2}'
```

### uniq - filter out repeted or duplicate lines
```
cat lahrt.txt |  awk '{print $3}' | uniq
    -c  - count how many repetitions
    -d  - show only repeted lines
```

### wc - word count
```
cat lahrt.txt |  wc
    -l  - return only number of lines
    -c  - return only number of cahrs / bytes
    -w  - return only number of words
```
<br>

```
echo "ala ma kota" | wc
```
|lines|words|bytes|
|-|-|-|
|1|3|12|
