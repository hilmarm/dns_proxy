kill $(ps aux | grep '[p]ython dnschef.py' | awk '{print $2}'):
  cmd.run

python dnschef.py --file dns_record_update.ini -q:
  cmd.run:
    - cwd: "/home/vagrant/"
    - bg: True
