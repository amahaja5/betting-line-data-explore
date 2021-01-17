import requests
import json
import logging

logger = logging.getLogger(__name__)


def get_sports(api_key, check_requests=False):
    sports_response = requests.get('https://api.the-odds-api.com/v3/sports', params={
        'api_key': api_key
    })
    if check_requests:
        print('Remaining requests', sports_response.headers['x-requests-remaining'])
        print('Used requests', sports_response.headers['x-requests-used'])

    sports_json = json.loads(sports_response.text)

    if not sports_json['success']:
        raise Exception(
            'There was a problem with the sports request:',
            sports_json['msg']
        )
    else:
        print()
        print(
            'Successfully got {} sports'.format(len(sports_json['data'])),
            'Here\'s the first sport:'
        )
        print(sports_json['data'][0])
        return sports_json
    
def get_set_of_sports(api_key):
    sports_json = get_sports(api_key)
    return [sport["key"] for sport in sports_json["data"]] + ["upcoming"]

def get_odds(api_key, sport, region, mkt=None, date_format=None, odds_format=None, check_requests=False):
    api_params = {"api_key" : api_key}
    sports_list = get_set_of_sports(api_key)
    if sport in sports_list:
        api_params["sport"] = sport
    else:
        raise ValueError(f"Invalid sport. Sport choices are {sport_choices}")
    region_choices = {"au", "uk", "eu", "us"}
    if region in region_choices:
        api_params["region"] = region
    else:
        raise ValueError(f"Invalid region. Region choices are {region_choices}")
    if mkt in {"h2h", "spreads", "totals"}:
        api_params["mkt"] = mkt
    if date_format in {"unix", "iso"}:
        api_params["dateFormat"] = date_format
    if odds_format in {"decimal", "american"}:
        api_params["oddsFormat"] = odds_format
    
    odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params=api_params)
    if check_requests:
        # Check your usage
        print()
        print('Remaining requests', odds_response.headers['x-requests-remaining'])
        print('Used requests', odds_response.headers['x-requests-used'])

    odds_json = json.loads(odds_response.text)
    if not odds_json['success']:
        Exception(
            'There was a problem with the odds request:',
            odds_json['msg']
        )
    else:
        # odds_json['data'] contains a list of live and 
        #   upcoming events and odds for different bookmakers.
        # Events are ordered by start time (live events are first)
        print()
        print(
            'Successfully got {} events'.format(len(odds_json['data'])),
            'Here\'s the first event:'
        )
        print(odds_json['data'][0])
        return odds_json
    
    