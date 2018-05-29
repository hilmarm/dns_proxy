kill $(ps aux | grep '[p]ython dnschef.py' | awk '{print $2}'):
python dnschef.py --file dns_record.ini -q &
