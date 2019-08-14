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

## Some usefule Vim commands

  A - append at the end of the line.
	w - move forward by a word
	2w - move forward by two words
	e - move the cursor to the end of the word
	0 - move to the start of the line
	dw - place the cursor on the beginning of the word to delete the whole word
	d$ - delete to the end of the line
	$ - move to the end of the line
	dd - delete the whole line
	x - delete a character
	u - undo last change
	U - return line to saved state
	(Control - R) - to redo
	p - after you type dd the line is deleted and added to the register. To Put the line back press p
	r - replace the character under the cursor with the next character typed
	ce - deletes the rest of the current word and places the cursor in insert mode
	c$ - deletes the rest of the line and places the cursor in insert mode
	G - move to the end of the file
	gg - move to the beginning of the file
	/ - to search for a word
	% - to jump to matchiing parenthesis
	f [character to match to] - find next character
	ct [character to match to] - replace up to the end of the line
	. to repeat the last action in command mode
	Y - to copy the whole line
	H - go high on the screen
	M - go middle on the screen
	L - go low on the screen
	
Many Vim commands have two parts, operator and a motion. In the examples above d is the operator and w and $ are the motions.
