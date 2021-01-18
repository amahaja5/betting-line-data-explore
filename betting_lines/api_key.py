import pathlib 

def get_api_key(use_file=True, file_path=pathlib.Path("~/.api_keys/sports_odds")):
    if use_file:
        if not isinstance(file_path, pathlib.Path):
            file_path = pathlib.Path(file_path)
        
        file_path = file_path.expanduser()
        with file_path.open('r') as fp:
            return fp.readline().strip()
    else:
        return "INSERT_API_KEY_HERE"
