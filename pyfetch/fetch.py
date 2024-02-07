from typing import Optional
import json
import sys 

from requests import Response
from requests.api import request

from pyfetch.reader import read_request_file
from pyfetch.writer import write

class Fetcher:
    def __init__(self) -> None:
        sys.stdout.reconfigure(encoding='utf-8')

    def fetch(request_file_path:str ,output_file_path:Optional[str] = None):
        out = output_file_path or sys.stdout
        data:dict = read_request_file(request_file_path)
        response:Response = request(**data)

        response_metadata = json.dumps(dict(**response.headers,
                                            **{"status":response.status_code,"url":response.url}))
        write(response_metadata + '\n' + response.content.decode('utf-8'),
              out)