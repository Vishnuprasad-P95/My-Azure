#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <config_file>"
    exit 1
fi

# Read versions and paths from the config file
while read -r line; do
    # Skip empty lines and lines starting with #
    if [[ -n "$line" && ! "$line" =~ ^\s*# ]]; then
        # Check if the line is a version or a path
        if [[ "$line" =~ ^[0-9.]+$ ]]; then
            # Uninstall JRE using rpm if it's a version
            rpm -e "jre$line"
            echo "Uninstalled JRE version $line using rpm"
        else
            # Verify that the path exists before attempting to delete
            if [ -d "$line" ]; then
                rm -rf "$line"
                echo "Deleted JRE path: $line"
            else
                echo "Error: Path not found: $line"
            fi
        fi
    fi
done < "$1"
