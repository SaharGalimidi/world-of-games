#!/bin/bash

# Base directory to start from
BASE_DIR=$1

# Function to process files
process_files() {
    local DIR=$1
    for FILE in "$DIR"/*; do
        if [[ -d "$FILE" ]]; then
            # If it's a directory and not 'venv', recursively process files
            if [[ "$(basename "$FILE")" != "venv" && "$(basename "$FILE")" != "__pycache__" ]]; then
                process_files "$FILE"
            fi
        elif [[ -f "$FILE" ]]; then
            # Print relative path and file content
            RELATIVE_PATH="${FILE#$BASE_DIR/}"
            echo "$RELATIVE_PATH:"
            cat "$FILE"
            echo -e "\n\n\n"
        fi
    done
}

# Start processing from the base directory
process_files "$BASE_DIR"
