# -*- coding: utf-8 -*-
# vim: ft=sls

dnschef python:
  file.managed:
    - name: /home/vagrant/dnschef.py
    - source: salt://dnschef/files/dnschef.py

dnschef config:
  file.managed:
    - name: /home/vagrant/dns_record.ini
    - source: salt://dnschef/files/dns_record.ini

dnschef config update:
  file.managed:
    - name: /home/vagrant/dns_record_update.ini
    - source: salt://dnschef/files/dns_record_update.ini

dnschef shell script old:
  file.managed:
    - name: /home/vagrant/dns_set_old.sh
    - source: salt://dnschef/files/dns_set_old.sh
    - mode: 744

dnschef shell script updated:
  file.managed:
    - name: /home/vagrant/dns_set_updated.sh
    - source: salt://dnschef/files/dns_set_updated.sh
    - mode: 744

dnschef log_file:
  file.managed:
    - name: /home/vagrant/dns_log
    - source: salt://dnschef/files/dns_log
    - mode: 664
