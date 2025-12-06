import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    try:
        print(f"FILE PATH: {file_path}")
        print(f"WORKING DIR: {working_directory}")
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))
        cmd = ["python", abs_target] + args
        print(f"Abs_working: {abs_working}")
        print(f"Abs_target: {abs_target}")
        print(f"CMD: {cmd}")
        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not os.path.exists(abs_target):
            return f'Error: File "{file_path}" not found.'
        elif not abs_target.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        process_object = subprocess.run(
            cmd,
            cwd=abs_working,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
            text=True,
        )
        code = process_object.returncode
        print(f"RETURN CODE: {code}")
        if code != 0:
            return f"Process exited with code {code}"
        elif process_object.stdout is None:
            return "No output produced"
        else:
            return f"STDOUT: {process_object.stdout}\nSTDERR: {process_object.stderr}\n"
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs an external command with subprocess with the stdout and stderr as return values",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Command-line arguments to pass to the PYthon file",
            ),
        },
    ),
)
