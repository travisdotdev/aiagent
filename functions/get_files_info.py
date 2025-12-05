import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, directory))
        if not abs_target.startswith(abs_working):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'
        else:
            entries = os.listdir(abs_target)
            detailed_entries = []
            for name in entries:
                full_path = os.path.join(abs_target, name)
                is_directory = os.path.isdir(full_path)
                size = os.path.getsize(full_path)
                detailed_entries.append(
                    f"- {name}: file_size={size} bytes, is_dir={is_directory}"
                )
            return "\n".join(detailed_entries)
    except Exception as e:
        return f"Error: {str(e)}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along witht heir sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            )
        },
    ),
)
