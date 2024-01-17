#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <config_file>"
    exit 1
fi

# Read paths and versions from the config file
while read -r line; do
    # Skip empty lines and lines starting with #
    if [[ -n "$line" && ! "$line" =~ ^\s*# ]]; then
        # Extract path and version from each line
        path=$(echo "$line" | awk '{print $1}')
        version=$(echo "$line" | awk '{print $2}')

        # Check if path and version are not empty
        if [ -n "$path" ] && [ -n "$version" ]; then
            # Check if the path exists
            if [ -d "$path" ]; then
                # Delete JRE path if version is not provided
                if [ -z "$version" ]; then
                    rm -rf "$path"
                    echo "Deleted JRE path: $path"
                fi
            else
                echo "Error: Path not found: $path"
            fi

            # Uninstall JRE using rpm if version is provided
            if [ -n "$version" ]; then
                rpm -e "jre$version"
                echo "Uninstalled JRE version $version using rpm from: $path"
            fi
        else
            echo "Error: Invalid line in config file: $line"
        fi
    fi
done < "$1"
