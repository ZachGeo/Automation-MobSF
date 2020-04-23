#!/bin/bash

# Calculate the md5 hash value of each sample and create a txt file whcich contains the md5 and the path of each sample.
find ~/Automation-MobSF/APKs -type f -exec md5sum {} + | sort -k 2 > ~/Automation-MobSF/scans_comparison/samples.txt

# Create a txt file which contains all the samples (md5 hash value) which have been already scanned by MobSF.
ls ~/Mobile-Security-Framework-MobSF/uploads/ > ~/Automation-MobSF/scans_comparison/scanned_samples.txt

# Number of samples that I want to scan.
num_samples=`find ~/Desktop/automation/APKs/ -type f | wc -l`

# If there are no samples into the APKs file, then print message.
if [ '$num_samples -eq 0' ]; then 
    echo "$(tput setaf 1)MESSAGE:$(tput setaf 8) [There are no files to be scanned]"
else
    echo "$(tput setaf 2)MESSAGE:$(tput setaf 7) There are $(tput setaf 4) $num_samples samples $(tput setaf 7) to be scanned."
fi

# Authorization API Key.
api_key=$(head -n 1 ~/Automation-MobSF/authorization_api_key.txt)

# Loop over the number of samples. 
for ((num=1; num<= "$num_samples"; num++));
do
  # From the txt file, I store the values of md5 and path of the sample.
  sample_md5=`sed -n -e "$num"p ~/Automation-MobSF/scans_comparison/samples.txt | awk '{print $1}'`
  sample_path=`sed -n -e "$num"p ~/Automation-MobSF/scans_comparison/samples.txt | awk '{print $2}'`

  # Check if the sample has already been scanned.
  # If "YES", remove file from those which I want to be scanned. If "NO", continue with scanning.  
  if grep -q "${sample_md5}" ~/Automation-MobSF/scans_comparison/scanned_samples.txt;
  then
   rm "$sample_path"

  else

   echo "$(tput setaf 6)START SCANNING OF SAMPLE $num OUT OF $num_samples..."

   test_sample="${sample_path}"
   name_sample="${sample_path:35}"
   type_sample="${sample_path: -3}"

   if [ "$type_sample" == "ppx" ]; then type_sample="appx"; fi

   # Upload sample.
   echo "UPLOAD SAMPLE:$(tput setaf 6) STEP 1 OUT OF 4"
   curl -F "file=@$test_sample" http://localhost:8000/api/v1/upload -H "Authorization:$authorization_api_key"

   # Scan sample. Static Analysis
   sleep 1m
   echo "STATIC SCAN:$(tput setaf 6) STEP 2 OUT OF 4"
   curl -X POST --url http://localhost:8000/api/v1/scan --data "scan_type=$type_sample&file_name=$name_sample&hash=$sample_md5" -H "Authorization:$authorization_api_key"

   # Run scrit to check the Security Static Score of the sample.
   #sleep 2m
   #python3 ~/Desktop/automation/run/static_score.py "$sample_md5"

   # Run script to start Dynamic Analysis
   sleep 2m
   echo "DYNAMIC SCAN:$(tput setaf 6) STEP 3 OUT OF 4"
   package_sample=$(python3 ~/Automation-MobSF/run/dynamic_scan.py "$name_sample" 2>&1)

   # Run script to download Static and Dynamic Report.
   sleep 10m
   echo "CREATE REPORTS:$(tput setaf 6) STEP 4 OUT OF 4"
   python3 ~/Automation-MobSF/run/reports.py "$sample_md5" "$package_sample" "$authorization_api_key"
  fi
done