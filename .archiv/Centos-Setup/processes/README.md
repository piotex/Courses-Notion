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