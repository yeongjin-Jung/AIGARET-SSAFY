#!/bin/bash

service nginx start
uwsgi -i /etc/uwsgi/sites/aigaret.ini
