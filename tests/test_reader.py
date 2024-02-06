import pytest
from pyfetch import reader

def test_read_request_file__yaml_supported():
    assert reader.read_request_file("example.yaml") == "example.yaml"

def test_read_request_file__yml_supported():
    assert reader.read_request_file("example.yml") == "example.yml"

def test_read_request_file__json_supported():
    assert reader.read_request_file("example.json") == "example.json"

def test_read_request_file_unsupported():
    with pytest.raises(reader.FileTypeUnsupportedException):
        reader.read_request_file("example.docx")


