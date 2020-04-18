
#!/bin/bash

# Find into the APKs file, only the files (not dir) and calculate the md5 hash for each file and pipe it sorted by hash value to a new file.
find /home/zach/Desktop/APKs/ -type f -exec md5sum {} + | sort -k 2 > upload_dir.txt

# Insert text into the first line of the selected file.
sed -i '1i #MD5 FilePath' /home/zach/Desktop/automation/upload_dir.txt

# File which has the name of the dirs of the samples which are already sanned.
ls /home/zach/mobsf/Mobile-Security-Framework-MobSF/uploads/ > mobsf_uploaded.txt

# Loop over all the lines of the file, doing something.
while IFS= read -r line; do
 # Read the first 32 number of each line of the file and assign to a variable. 
 sample_md5="$(head -c 32)"
 # Read the path of the APK, which we want to scan.
 sample_path="$(cut -d ' ' -f 3-)"

 if grep -q "${sample_md5}" /home/zach/Desktop/automation/mobsf_uploaded.txt;
 then
  rm "$sample_path"
  curl -X POST --url http://localhost:8000/api/v1/delete_scan --data "hash=$sample_md5" -H "Authorization:7749e3e9e6db8c3fc2f890348d81f084cc3ad8a5abac4592f6ceea5659b12caf" ;
 else
  test_sample="${sample_path}"
  name_sample="${sample_path:24}"
  type_sample="${sample_path: -3}"

  if [ "$type_sample" == "ppx" ]; then type_sample="appx"; fi 

  curl -F "file=@$test_sample" http://localhost:8000/api/v1/upload -H "Authorization:7749e3e9e6db8c3fc2f890348d81f084cc3ad8a5abac4592f6ceea5659b12caf";
  sleep 1m
  curl -X POST --url http://localhost:8000/api/v1/scan --data "scan_type=$type_sample&file_name=$name_sample&hash=$sample_md5" -H "Authorization:7749e3e9e6db8c3fc2f890348d81f084cc3ad8a5abac4592f6ceea5659b12caf"
  sleep 3m
  curl -X POST --url http://localhost:8000/api/v1/download_pdf --output StaticReport --data "hash=$sample_md5" -H "Authorization:7749e3e9e6db8c3fc2f890348d81f084cc3ad8a5abac4592f6ceea5659b12caf"
  sleep 2m

  python3 /home/zach/enviroments/test.py "$name_sample"
  sleep 10m
 fi
done < /home/zach/Desktop/automation/upload_dir.txt
