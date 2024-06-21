# processes

```
nice
    -20 -> highetst priority
     19 -> lowest priority

top -> check process priority   [PR] [NI]
    PR -> actual process priority (that is used by Linux)   -> 0 to 139
    NI -> user priority                                     -> 100 to 139 

ps axo pid,comm,nice,cls --sort=nice
```
```
nice -n priority_number proces-name     -> set priority of process
nice -n -15 top

renice -n priority_number PID          -> change priority of process
nice -n -15 top
```

# processes-and-jobs

Application -> Service that runs on your computer like apache or chrome<br>
Script      -> List of instructions writen in a file which can can be executed <br>
Process     -> // represent an instance of running program <br>
Daemon      -> //proces that run continuously in a background<br>
Threads     -> // it's a sequence of instructions that can be executed independently by a CPU core<br>
Job         -> // run a service or process at a schedule time<br>
<br>


# silent process
```
nohup sleep 73 > /dev/null 2>&1 &
```

# working with process priority 
```
nice
```