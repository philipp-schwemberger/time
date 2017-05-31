### get time with GPS
___________

In order to set up the basics and install everything on the raspberry pi, follow this [tutorial](https://area-51.blog/2012/06/18/getting-gps-to-work-on-a-raspberry-pi/) first.  

I figured out that the command `$ sudo killall gpsd` wasn't enough for my system. I had to add `$ sudo service gpsd stop` right afterwards and therefore created this bash script:  
```
#!/bin/sh
sudo killall gpsd
sudo service gpsd stop
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
```
 which is launched, everytime the raspi boots.  
 
Another helpful command to check if you are getting infos from your GPS is `$ gpsmon /dev/ttyUSB0`. I experienced that I could get at least the utc-time with `$ cgps -s` or `$ gpsmon /dev/ttyUSB0` almost immediately, while for the 3D FIX (getting the latitude and longitude information) it took from 20min up to one hour. It works better when placed next to a window, but still took almost 20 minutes.
