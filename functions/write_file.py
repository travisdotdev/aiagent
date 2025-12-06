import os
from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))
        parent_dir = os.path.dirname(abs_target)
        # print("HERE======================")
        # print(f"Abs_working {abs_working}")
        # print(f"Abs_target: {abs_target}")
        # print(f"Full Path: {parent_dir}")
        # print("END==========================")
        if not abs_target.startswith(abs_working):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(parent_dir):
            # print(f"Path Created: {parent_dir}")
            os.makedirs(parent_dir)
        with open(abs_target, "w") as f:
            # print(f"WRITING TO FILE: {abs_target}")
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {str(e)}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file, creates the path if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be written to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that we will write to the file",
            ),
        },
    ),
)
