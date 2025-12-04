import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        file_path = os.path.abspath(full_path)
        # print("HERE======================")
        # print(f"Abs_working {abs_working}")
        # print(f"Abs_target: {abs_target}")
        # print(f"Full Path: {full_path}")
        # print(f"File_path: {file_path}")
        # print("END==========================")
        if not abs_target.startswith(abs_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(file_path):
            return f'Error file not found or is not a regular file: "{file_path}"'
        else:
            # print("WE REACHED FILE PRINTING")
            with open(file_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if len(file_content_string) == MAX_CHARS:
                    return f'{file_content_string}\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                else:
                    return file_content_string

    except Exception as e:
        return f"Error: {str(e)}"
