import os


def get_files_info(working_directory, directory="."):
    # Compute the absolute target directory
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_dir = os.path.abspath(working_directory)

    # Step 2: Check boundary
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Step 3: Check if path is a directory
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    # Step 4: Build string listing of directory contents
    try:
        files_info = []
        for file_name in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file_name)
            file_size = 0
            is_dir = os.path.isdir(file_path)
            file_size = os.path.getsize(file_path)
            files_info.append(f'- {file_name}: file_size={file_size} bytes, is_dir={is_dir}')

        return "\n".join(files_info)

    except Exception as e:
        return f"Error listing files: {e}"
