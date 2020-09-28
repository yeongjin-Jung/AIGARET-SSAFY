FROM barkingcode/aigaret-server:base
MAINTAINER barkingcode@gmail.com

COPY front-end/dist /var/www/aigaret/
COPY back-end /home/aigaret/
COPY run.sh run.sh

ENTRYPOINT ["./run.sh"]
# service nginx start
# uwsgi -i /etc/uwsgi/sites/aigaret.ini