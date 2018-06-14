sudo kill $(ps aux | grep '[p]ython /vagrant/dns_files/dnschef.py' | awk '{print $2}')
python /vagrant/dns_files/dnschef.py --fakeip $2 --fakedomains $1 --interface $(hostname -I) -q &
