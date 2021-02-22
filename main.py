#Update python environment to 3.9.2
apt install libffi-dev libbz2-dev liblzma-dev libsqlite3-dev libncurses5-dev libgdbm-dev zlib1g-dev libreadline-dev libssl-dev tk-dev build-essential libncursesw5-dev libc6-dev openssl git
wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tar.xz
tar xf Python-3.9.2.tar.xz
cd Python-3.9.2
./configure --enable-optimizations
make -j -l 4
sudo make altinstall
#sudo nano ~/.bashrc
#Add command: alias python='python3.9'
#Add command: alias python3='python3.9'
#Save changes and exit
. ~/.bashrc


#Install packages needed for deepspeech
sudo apt install git python3-pip python3-scipy python3-numpy python3-pyaudio libatlas3-base
pip3 install deepspeech --upgrade
mkdir ~/dspeech
cd ~/dspeech
#Download scorer and tensorflow model for deepspeech
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.tflite
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/audio-0.9.3.tar.gz
tar xvf audio-0.9.3.tar.gz
source ~/.profile
