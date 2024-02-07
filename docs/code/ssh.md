# SSH

## Setup ssh
1. generate ssh key pair on password
```bash title=""
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

2. copy the public key
```bash title=""
cat ~/.ssh/id_rsa.pub
```

3. add it
      - to the service you want to connect to (ex github)
      - to the host `ssh-copy-id -i ~/.ssh/id_rsa.pub gamnes@raspberrypi`
      - by editing  `~/.ssh/authorized_keys`

##  Vscode

0. Setup the ssh connection with the raspberry as described above.
1. Download ssh extension
2. update the config
   ```ssh title="~/.ssh/config"
   Host raspberrypi
      HostName raspberrypi.local
      User pi
   ```

## Flashcards