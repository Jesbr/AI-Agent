import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    # Compute the absolute target path
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    # Step 2: Check if the file_path is outside the working_directory
    if not target_path.startswith(abs_working_dir + os.sep):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # Step 3: Check if the file_path is not a file
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
        
    try:
        # Read file content
        with open(target_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Truncate if content is longer than 10,000 characters
        if len(content) > MAX_CHARS:
            truncated_notice = f'[...File "{file_path}" truncated at 10000 characters]'
            return content[:MAX_CHARS] + truncated_notice

        return content
        
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

#AI utility  
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)