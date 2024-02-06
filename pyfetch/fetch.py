import json

import requests
from requests import Response
from requests.api import request
import sys

from pyfetch.reader import read_request_file

class Fetcher:
    def __init__(self) -> None:
        pass

    def fetch(file_path:str = 'data.yaml'):
        data:dict = read_request_file(file_path)
        res:Response = request(**data)
        print(res)

