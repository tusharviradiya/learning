# docker

KVM virtualization support
modprobe kvm
modprobe kvm_intel
for check kvm enable or not : lsmod | grep kvm 
To check ownership of /dev/kvm, run : ls -al /dev/kvm
Add your user to the kvm group in order to access the kvm device : sudo usermod -aG kvm $USER

Install Docker Desktop on Ubuntu

sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
sudo apt install gnome-terminal
sudo apt-get update
sudo apt-get install ./docker-desktop-<arch>.deb
To determine your architecture : dpkg --print-architecture
Install required dependencies: sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
Add Docker's GPG key : curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker.gpg
Set up the Docker repository: sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

install docker package
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin