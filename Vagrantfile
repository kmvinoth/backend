# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # Box Settings
  config.vm.box = "ubuntu/bionic64"

  # Provider Settings
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = 1
  end

  # Network Settings
  config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  # config.vm.network "private_network", ip: "192.168.33.10"
  
  # Folder Settings
  config.vm.synced_folder ".", "/home/vagrant/backend", type:"virtualbox"

  # install docker into the VM
  config.vm.provision :docker
  # install docker-compose into the VM
  config.vm.provision :docker_compose

end
