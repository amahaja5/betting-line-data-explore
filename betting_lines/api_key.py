import pathlib

API_KEY_DEFAULT_LOCATION = pathlib.Path("~/.api_keys/sports_odds")

def get_api_key(use_file=True, file_path=None):
    if use_file:
        file_path = (file_path or API_KEY_DEFAULT_LOCATION).expanduser()
        with file_path.open('r') as fp:
            return fp.readline().strip()
    else:
        return "INSERT_API_KEY_HERE"