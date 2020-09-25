FROM barkingcode/aigaret-server:base
MAINTAINER barkingcode@gmail.com

COPY front-end/dist /var/www/aigaret/
COPY back-end /home/aigaret/

