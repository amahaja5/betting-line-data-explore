def get_api_key(use_file=True):
    if use_file:
        with open("API_KEY", 'r') as fp:
            return fp.readline().strip()
    else:
        return "INSERT_API_KEY_HERE"