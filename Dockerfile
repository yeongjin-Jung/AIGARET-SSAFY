FROM barkingcode/aigaret-server:base
MAINTAINER barkingcode@gmail.com

COPY front-end/dist /var/www/aigaret/dist
COPY back-end /home/aigaret/back-end
COPY run.sh run.sh

ENTRYPOINT ["./run.sh"]
# service nginx start
# uwsgi -i /etc/uwsgi/sites/aigaret.ini