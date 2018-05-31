kill $(ps aux | grep '[p]ython dnschef.py' | awk '{print $2}'):
  cmd.run

python dnschef.py --file dns_record.ini -q --interface {{ pillar['dns_interface'] }} --logfile dns_log:
  cmd.run:
    - cwd: "/home/vagrant/"
    - bg: True
