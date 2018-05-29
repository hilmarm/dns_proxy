# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.synced_folder "./", "/vagrant"
  config.vm.synced_folder "saltstack/salt", "/srv/salt/"
  config.vm.synced_folder "saltstack/pillar", "/srv/pillar/"
  config.vm.synced_folder "saltstack/etc", "/etc/salt/"
  config.vm.network "private_network", ip: "192.168.50.4", virtualbox__intnet: true

  config.vm.provision :salt do |salt|
    salt.minion_config = "saltstack/etc/minion"
    salt.run_highstate = true
    salt.log_level = 'info'
    salt.verbose = true
    salt.colorize = true
  end

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 1
    # v.cpu_mode = "host-passthrough"
  end

  config.vm.define :dns do |dns|
    dns.vm.hostname = "dns-proxy"
    dns.vm.network "private_network",:auto_config => true, :libvirt__dhcp_enabled => true, ip: "192.168.200.100"
  end
  config.vm.define :client do |cl|
    cl.vm.hostname = "client"
    cl.vm.network "private_network",:auto_config => true, :libvirt__dhcp_enabled => true, ip: "192.168.200.101"
  end

end
