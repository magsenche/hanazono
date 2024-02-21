# Raspberry Pi

## Getting started
## Install OS
Use [raspberry pi imager](https://www.raspberrypi.com/software/) to update, install or format the OS
With advenced settings, you can set up ssh, wifi, passwords, etc.

### First boot
1. Shutdown raspberry pi
2. Put the sd card on
3. Aliment the raspberry pi

$\Rightarrow$ green led indicates its processing

### SSH

Check [how to setup ssh](ssh.md)

### Wifi
1. Edit the `/etc/wpa_supplicant/wpa_supplicant.conf` file.
```bash title=""
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
1. Add the following lines with your WiFi credentials
```makefile title="wpa_supplicant.conf"
network={
    ssid="networkd_name"
    psk="password"
}
```

### Install python 3.11

Follow this [answer](https://stackoverflow.com/a/76942080)
