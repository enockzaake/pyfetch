import pytest
import os
from pyfetch.reader import read_request_file, FileTypeUnsupportedException

@pytest.fixture
def yaml_file(tmp_path):
    file_path = tmp_path / "test.yaml"
    with open(file_path, 'w') as f:
        f.write('key: value\n')
    return str(file_path)

@pytest.fixture
def json_file(tmp_path):
    file_path = tmp_path / "test.json"
    with open(file_path, 'w') as f:
        f.write('{"key": "value"}')
    return str(file_path)

def test_read_yaml_file(yaml_file):
    assert read_request_file(yaml_file) == {'key': 'value'}

def test_read_json_file(json_file):
    assert read_request_file(json_file) == {'key': 'value'}

def test_read_invalid_file(tmp_path):
    file_path = tmp_path / "test.txt"
    with open(file_path, 'w') as f:
        f.write('some content')
    with pytest.raises(FileTypeUnsupportedException):
        read_request_file(str(file_path))
