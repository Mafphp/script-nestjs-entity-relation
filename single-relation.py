import os
import re

# Directory path where your TypeScript files are located
directory_path = "./src/entities/"

# Regular expression pattern to match "Entity;" and replace it with "Relation<Entity>;"
pattern = r'(\w+): (\w+)Entity;'

# Replacement pattern to change "Entity;" to "Relation<Entity>;"
replacement = r'\1: Relation<\2Entity>;'

# Iterate through files in the directory
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith(".entity.ts"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                content = file.read()
            content = re.sub(pattern, replacement, content)
            with open(file_path, 'w') as file:
                file.write(content)