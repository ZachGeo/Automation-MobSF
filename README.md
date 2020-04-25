# Automation-MobSF
Automate Static &amp; Dynamic Analysis of the Mobile-Security-Framework

[![python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/)
[![platform](https://img.shields.io/badge/platform-linux-green.svg)](https://github.com/ZachGeo/Automation-MobSF)

## Requirements

- **Ubuntu based Linux**
  * Install git `sudo apt install git`
  * Install Python 3.6 - 3.7 `sudo apt install python`
  * Install JDK 8+ `sudo apt install openjdk-8-jdk`
  * Install the following dependencies `sudo apt install python3-venv python3-pip python3-dev build-essential libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev wkhtmltopdf
`
  * Android Emulator Options:  
    >*Recommended using Android 7.0 and above.*
    *  **Option 1**: Install Genymotion Android Emulator: [Genymotion Installation Guide](https://linuxhint.com/install_genymotion_android_emuator_ubuntu/)
     >*Supports x86 architecture Android 4.1 - 9.0, upto API 28*
    * **Option 2**: Download & Install Android Studio: [Android Studio Download Guide](https://linuxize.com/post/how-to-install-android-studio-on-ubuntu-18-04/)
     1. Add your Android SDK emulator directory to PATH: `export PATH="$PATH:/home/<user>/Android/Sdk/emulator`
     2. Set ADB_BINARY path in MobSF/settings.py, after the installation of MobSF: `ADB_BINARY = '/home/<user>/Android/Sdk/platform-tools/adb'`
     3. Create AVD Emulator with name mobsf: 
      >*Supports arm, arm64 and x86 architecture Android 5.0 - 9.0, upto API 28*
     4. To see your created emulator:
       * `cd ~/Android/Sdk/emulator`
       * `emulator -list-avds`
  * Install npm `sudo apt install npm`
  * Install pm2 `npm install pm2 -g`
  * Download [geckodriver](https://github.com/mozilla/geckodriver)
    ```
      wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
      tar -xvzf geckodriver*
      chmod +x geckodriver
      sudo mv geckodriver /usr/local/bin/.
    ```
  * Install curl `sudo apt install curl`    
  * Download [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)
    ```
      git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git 
      cd Mobile-Security-Framework-MobSF
      ./setup.sh
     ```    
   * Download [Automation-MobSF](https://github.com/ZachGeo/Automation-MobSF)
    ```
     git clone https://github.com/ZachGeo/Automation-MobSF
     cd Automation-MobSF/run/
     ./setup.sh
    ```
## Run
- `cd ~/Automation-MobSF/`
- `chmod +x emulator.sh`
- `pm2 start ./emulator.sh`
- `pm2 save`
- `cd ~/Mobile-Security-Framework-MobSF/`
- `chmod +x run.sh`
- `pm2 start ./run.sh`
- `pm2 save`
- `cd ~/Automation-MobSF/run/`
- `chmod +x auto_upload_scan.sh`
- `pm2 start ./auto_upload_scan.sh`
- `pm2 save`

## Tranfer samples to APKs directory, in order to start the static & dynamic analysis
- `python3 -m http.server 8080`
- `cd <path of the sample which you want to scan>`
- `~/Automation-MobSF/transfer.sh <name of the sample>`
##### Note: After every two minutes you have to re-start the HTTP SERVER with Port access 8080,  if you want to transfer a new sample.
