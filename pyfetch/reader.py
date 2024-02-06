import json
import yaml

class FileTypeUnsupportedException(Exception):
    def __init__(self,file_path) -> None:
        super().__init__(f"Unsupported file type {file_path}")


def read_request_file(file_path:str) -> dict:
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path,"r") as yaml_file:
            data = yaml.safe_load(yaml_file)
            return data
    elif file_path.endswith(".json"):
        with open(file_path,"r") as json_file:
            data = yaml.safe_load(json_file)
            return data
    else:
        raise FileTypeUnsupportedException(file_path)

