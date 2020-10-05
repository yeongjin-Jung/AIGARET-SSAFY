#!/bin/bash

# chmod 744 run.sh
cd /home/aigaret/back-end/
pip install -r requirements.txt
cd
service nginx start
uwsgi -i /etc/uwsgi/sites/aigaret.ini
/bin/bash
