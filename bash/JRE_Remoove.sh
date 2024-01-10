#!/bin/bash
# This script will remove JRE from a RHEL 7 server
# Check if JRE is installed with RPM
rpm -qa | grep -i jre
# If RPM reports a package similar to jre-<version>-fcs, then uninstall it
if [ $? -eq 0 ]; then
  rpm -e jre-<version>-fcs
fi
# Find out if JRE is installed in some folder
# Common locations are /usr/java/jre_<version> or /opt/jre_nb/jre_<version>/bin/java
# If you find the folder, delete it
if [ -d /usr/java/jre_<version> ]; then
  rm -rf /usr/java/jre_<version>
elif [ -d /opt/jre_nb/jre_<version> ]; then
  rm -rf /opt/jre_nb/jre_<version>
fi
# Remove any references to JRE in system-wide PATH and MANPATH settings
# Check /etc/environment, /etc/profile, and the files in /etc/profile.d directory if it exists
# Delete any system-wide JAVA_HOME environment variable settings
sed -i '/JAVA_HOME/d' /etc/environment
sed -i '/JAVA_HOME/d' /etc/profile
if [ -d /etc/profile.d ]; then
  for file in /etc/profile.d/*; do
    sed -i '/JAVA_HOME/d' "$file"
  done
fi
# Check that /usr/local/bin directory doesn't contain any now-broken symbolic links pointing to the tools within JRE
find /usr/local/bin -type l -exec test ! -e {} \; -delete
# Verify that JRE is removed by typing: which java
# If JRE is removed, the output should be: no java in (<paths>)
which java
