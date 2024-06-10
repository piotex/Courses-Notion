# aliases-like-shortcuts

### temp aliases
```
alias l="ls -lahrt"
alias d="df -h | awk '{print \$6} | cut -c1-4"
```
```
alias       -> print
```
```
unalias my_alias_name
```

### user aliases
```
vi /home/user/.bashrc
alias l="ls -lahrt"
```

### global aliases
```
vi /etc/bashrc
alias l="ls -lahrt"
```