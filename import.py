import os
import re

# # Directory path where your TypeScript files are located
# directory_path = "./src/entities/"

# # Regular expression pattern to match existing 'typeorm' imports
# pattern_existing_imports = r'import {\s*([^}]+)\s*} from \'typeorm\';'

# # Iterate through files in the directory
# for root, dirs, files in os.walk(directory_path):
#     for file in files:
#         if file.endswith(".ts"):
#             file_path = os.path.join(root, file)
#             with open(file_path, 'r') as file:
#                 content = file.read()
#             match = re.search(pattern_existing_imports, content)
#             if match:
#                 existing_imports = match.group(1)
#                 new_imports = f'{existing_imports}, Relation'
#                 updated_import = f'import {{ {new_imports} }} from \'typeorm\';'
#                 content = re.sub(pattern_existing_imports, updated_import, content)
#                 with open(file_path, 'w') as file:
#                     file.write(content)

# Directory path where your TypeScript files are located


# Directory path where your TypeScript files are located
directory_path = "./src/entities/"

# Regular expression pattern to match the import statement from 'typeorm'
pattern_import_statement = r'import\s*{\s*(.*?)\s*}\s*from\s*\'typeorm\';'

# Iterate through files in the directory
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith(".ts"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                content = file.read()

            # Find the 'typeorm' import statement
            match = re.search(pattern_import_statement, content)
            if match:
                imported_objects = match.group(1)
                corrected_import = re.sub(r'\*\s*,', '*', imported_objects)
                corrected_import = re.sub(r',\s*\*', ', *', corrected_import)
                updated_import_statement = f'import {{ {corrected_import}, Relation }} from \'typeorm\';'
                content = content.replace(match.group(0), updated_import_statement)

                with open(file_path, 'w') as file:
                    file.write(content)
