# Solution
Unzip memdump.7z | Download Volatility3

Scan the memory dump for any existing files that has flag in the name
```
vol.py -f memdump.mem windows.filescan | grep flag
```
Output:
```
0xc18393cb5670.0\Users\ctf\Downloads\flag.txt   216
0xc18393ed7120  \Users\ctf\Documents\flag.txt   216
0xc18393edb900  \Users\ctf\AppData\Roaming\Microsoft\Windows\Recent\flag.lnk    216
```

Dump the file out with windows.dumpfiles (there are other ways)
```
vol.py -f memdump.mem windows.dumpfiles --virtaddr 0xc18393cb5670
```
Output: 
aV8xMHYzX20zTTByWV9kdk1weno=

From Base64:
i_10v3_m3M0rY_dvMpzz

# Final Flag
```
ISC2CTF{i_10v3_m3M0rY_dvMpzz}
```
