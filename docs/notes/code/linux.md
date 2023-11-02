# Linux

## Install & Update

`dpkg -i xxxx.deb`

### Where ?
- `/opt/app`  non-self, external, prepackaged binary/application bundle installation area
- `/usr/local/bin/app.exe`  self, inhouse, compiled and maintained software

Can make a symlinks, e.g `/usr/local/bin/app.exe` or `/usr/bin/app.exe` pointing to `/opt/app/bin/app.exe`

## Shortcuts
- create `/path/to/shortcut.sh` with code to run
- set custom shortcut to `bash -f /path/to/shortcut.sh`

example:

**Insert code in mattermost**
```bash
#!/bin/bash
xclip -in -selection c ~/.custom/mattermost/insert_code.txt
sleep 0.1
xdotool key ctrl+v
xdotool key BackSpace
xdotool key Up
```

## Flashcards