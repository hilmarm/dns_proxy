sudo kill $(ps aux | grep '[p]ython /vagrant/dns_files/dnschef.py' | awk '{print $2}')
python /vagrant/dns_files/dnschef.py --file /vagrant/dns_files/dns_record_update.ini --interface $(hostname -I) -q &
