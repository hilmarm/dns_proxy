sudo kill $(ps aux | grep '[p]ython /vagrant/dns_files/dnschef.py' | awk '{print $2}')