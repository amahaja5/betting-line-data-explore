import pathlib
import appdirs

default_directory = pathlib.Path(appdirs.user_config_dir('betting_lines_api')) / 'api_key'

def get_api_key(file_path=default_directory):
    if not isinstance(file_path, pathlib.Path):
        file_path = pathlib.Path(file_path)
    if not file_path.is_file():
        raise RuntimeError(f'No file found at specified path {file_path}')
    file_path = file_path.expanduser()
    with file_path.open('r') as fp:
        return fp.readline().strip()
