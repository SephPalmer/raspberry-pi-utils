# raspberry-pi-utils
Utils for the Raspberry Pi

## Some useful commands for the Raspberry Pi

`ping raspberrypi.local` to get the IP of the Pi on your network

`ssh <username>@<IP>` to log in via SSH

`sudo reboot` you guessed it, it reboots the Pi

`sudo shutdown -h now` to do a clean shutdown

`sudo apt-get dist-upgrade` update the distro. Can take a LONG time.

`sudo apt-get update` update the package manager

`curl -sSL https://get.docker.com | sh` install the Docker client

`sudo apt-get install nginx` install the NGINX server

`cat /etc/os-release` find out which OS release you have

`sudo visudo` to give a user root permissions. Use with caution

## Some useful Docker commands

`docker run --rm -d --network host --name <name of container> <name of image>` Docker Run exposing container to network
