### Connecting to the server manually

On Windows, activate the telnet client: https://www.technipages.com/windows-10-enable-telnet

On Linux, install it with `sudo apt install telnet`

`telnet localhost 7777`

`connect wizard`

#### Making players wizards manually

(to allow them to create new objects and rooms)

replace p with the players object id, which you can find out with `@who`
```
@chparent #p to $wiz
@programmer #p
;#p.wizard=1
```
