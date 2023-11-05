import os
import re

# Directory path where your TypeScript files are located
directory_path = "./src/entities/"

# Regular expression pattern to match "Entity;" and replace it with "Relation<Entity>;"
pattern_entity = r'(\w+): (\w+)Entity;'

# Replacement pattern to change "Entity;" to "Relation<Entity>;"
replacement_entity = r'\1: Relation<\2Entity>;'

# Regular expression pattern to match "Entity[]" and replace it with "Relation<Entity>[]"
pattern_array = r'(\w+): (\w+)Entity\[\];'

# Replacement pattern to change "Entity[]" to "Relation<Entity>[]"
replacement_array = r'\1: Relation<\2Entity>[];'

# Iterate through files in the directory
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith(".entity.ts"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                content = file.read()
            content = re.sub(pattern_entity, replacement_entity, content)
            content = re.sub(pattern_array, replacement_array, content)
            with open(file_path, 'w') as file:
                file.write(content)
