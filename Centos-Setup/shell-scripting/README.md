# shell-scripting

### History of shell
Gnome -> KDE -> sh -> bash -> csh and tcsh -> ksh

### Create a shell script
```
#!/bin/bash
# comment
echo "ala ma kota"
my_var=999
echo $my_var
echo "text: $my_var"
tmp=`hostname`
echo $tmp
```
statements: if, while, for, etc <br>
! remember to add x permissions to your script <br>
```
chmod a+x my_script.sh
```

### Input/Output in script
```
echo "Tell me sth"
read my_var
echo $my_var
```

### Run script
```
./my_script.sh
/home/something/my_script.sh
```

### if statement
```
#!/bin/bash
count=100
if [ $count -eq 100 ]
then
        echo "count is $count "
else
        echo " ... "
fi
```
```
if [ -e /home/peter/file.txt ] 
then
        echo "File exist"
fi
```
### loops - for
```
#!/bin/bash
for i in 1 2 3 4 5
do
        echo $i
done
```
```
for i in txt1 txt2 txt3

for i in {1..5}
```
```
#!/bin/bash
i=1
for day in Mon Tue Wed
do 
        echo " $day : $((i++)) "
done
```
```
#!/bin/bash
i=1
for username in `awk -F: '{print $1}' /etc/passwd`
do 
        echo " $username : $((i++)) "
done
```

### loops - while
```
#!/bin/bash
count=0
num=10
while [ $count -lt 10 ]
do 
        echo " $1 : $num "
        num=`expr $num - 1`
        count=`expr $count + 1`
        sleep 1
done
```
```
$1  is the firs parameter e.g. ./my_script param1 
```

### case scripts
```
#!/bin/bash
echo
echo Please chode one of the options below
echo
echo 'a = Display Date and Time'
echo 'b = List files and dirs'
echo 'c = List users logged in'
echo

read choice

case $choice in
a) date;;
b) ls -la;;
c) who;;
*) echo Invalid choice - Bye.
esac

```

### catch result of previous comand -> $?
```
#!/bin/bash
ping -c1 8.8.8.8
if [ $? -eq 0 ]
then 
        echo "connected"
fi
```

