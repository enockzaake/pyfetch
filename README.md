<div align="center">
<pre>


──────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─████████──████████─██████████████─██████████████─██████████████─██████████████─██████──██████─
─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─
─██░░██████░░██─████░░██──██░░████─██░░██████████─██░░██████████─██████░░██████─██░░██████████─██░░██──██░░██─
─██░░██──██░░██───██░░░░██░░░░██───██░░██─────────██░░██─────────────██░░██─────██░░██─────────██░░██──██░░██─
─██░░██████░░██───████░░░░░░████───██░░██████████─██░░██████████─────██░░██─────██░░██─────────██░░██████░░██─
─██░░░░░░░░░░██─────████░░████─────██░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██─────██░░██─────────██░░░░░░░░░░██─
─██░░██████████───────██░░██───────██░░██████████─██░░██████████─────██░░██─────██░░██─────────██░░██████░░██─
─██░░██───────────────██░░██───────██░░██─────────██░░██─────────────██░░██─────██░░██─────────██░░██──██░░██─
─██░░██───────────────██░░██───────██░░██─────────██░░██████████─────██░░██─────██░░██████████─██░░██──██░░██─
─██░░██───────────────██░░██───────██░░██─────────██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░██──██░░██─
─██████───────────────██████───────██████─────────██████████████─────██████─────██████████████─██████──██████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────
......................................
Make request from yaml or json files.

</pre>
</div>

### PyFetch

PyFetch is a command-line tool designed to fetch data from a given source based on a provided request file in YAML, JSON, or YAML formats.

### Installation

To install PyFetch, you can use pip:

```
pip install pyfetch
```

### Usage

```
usage: pyfetch [-h] [-f REQUEST_FILE_PATH] [-o OUTPUT_FILE_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -f REQUEST_FILE_PATH, --request_file_path REQUEST_FILE_PATH
                        Request file path of type .yaml, .yml, or .json
  -o OUTPUT_FILE_PATH, --output_file_path OUTPUT_FILE_PATH
                        Output file path else prints to standard output.
```

### Example

To use PyFetch, provide the path to the request file using the `-f` or `--request_file_path` flag and optionally specify an output file path using the `-o` or `--output_file_path` flag.

```
pyfetch -f request.yaml -o output.txt
```

This command will fetch data based on the requests specified in `request.yaml` and write the response to `output.txt`. If no output file path is provided, the response will be printed to the standard output.

### Request File Format

The request file must be in YAML, JSON, or YAML format and should contain the necessary parameters for making HTTP requests. Here's an example of a YAML request file:

```yaml
method: GET
url: https://api.example.com/data
headers:
  Authorization: Bearer <token>
```

### Output

The output will contain the response metadata (headers, status code, and URL) followed by the response content.

### Supported Formats

PyFetch supports request files in YAML, JSON, and YAML formats. If an unsupported file type is provided, an exception will be raised.

### Note

Ensure that the necessary dependencies are installed before using PyFetch.
