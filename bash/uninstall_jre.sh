#!/bin/bash

# Specify the file containing the JRE versions to uninstall
versions_file="versions.txt"

# Check if the versions file exists
if [ ! -f $versions_file ]; then
    echo "$versions_file does not exist."
    exit 1
fi

# Read each line in the versions file
while IFS= read -r jre_version
do
  for version in jre_version
  do
      # Check if the JRE version is installed
      if rpm -q $version
      then
          echo "Uninstalling $version"
          sudo yum remove $version -y
          echo "$version has been uninstalled."
      else
          echo "$version is not installed."
      fi
    done
done < "$versions_file"
