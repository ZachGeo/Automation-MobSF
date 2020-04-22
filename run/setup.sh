#!/bin/bash

echo '[INSTALL] Installing Requirements'
pip install --no-cache-dir -r requirements.txt

echo 'Create Necessary Directories'
mkdir APKs
mkdir reports
mkdir scans_comparison