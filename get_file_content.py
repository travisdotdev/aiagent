import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))
        full_path = os.path.join(abs_target, file_path)
        if not abs_target.startswith(abs_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isdir(full_path):
            return f'Error file not found or is not a regular file: "{full_path}"'
        else:
            with open(full_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)

    except Exception as e:
        return f"Error: {str(e)}"
