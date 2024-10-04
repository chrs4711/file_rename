#!/usr/bin/env python3

import os
import re
import sys

## YYYY-MM-DDD
date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')
directory = "~/Downloads"

def new_filename(filename, date):
    new_name = filename.replace(date, '')
    return f"{date}-{new_name}"

def get_user_choice():
    while True:
        user_input = input('Proceed? (y = yes, s = skip, c = cancel): ').lower()
        if user_input in ['y', 's', 'c']:
            return user_input
        else:
            print("Invalid input.")

def do_rename(directory, filename, new_filename):
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_filename)
    os.rename(old_path, new_path)
    print(f"✅ new file: '{new_path}'")

def main():

    expanded_directory = os.path.expanduser(directory)
    
    for filename in os.listdir(expanded_directory):
        
        match = date_pattern.search(filename)
        if not match:
            continue
        
        date = match.group(1)
        
        if filename.startswith(date):
            continue

        new_name = new_filename(filename, date)

        print(f"Found:     '{filename}'")
        print(f"Rename to: '{new_name}'?")
        
        choice = get_user_choice()

        if choice == 'y':
            do_rename(expanded_directory, filename, new_name)
        elif choice == 's':
            print("🤷")
            continue
        elif choice == 'c':
            print("😵")
            sys.exit()
    
    
if __name__ == "__main__":
    main();
