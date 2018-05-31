update nameserver:
  file.managed:
    - name: /etc/resolv.conf
    - source: salt://set_nameserver/files/resolv.conf