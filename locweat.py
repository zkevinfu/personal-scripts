import requests
import json
import yaml

CONFIG_FILE = 'config.yaml'

def get_loc():
    loc_url = 'http://freegeoip.app/json'
    r = requests.get(loc_url)
    j = json.loads(r.text)
    return (j['latitude'], j['longitude'])

def get_weat():
    with open(CONFIG_FILE, 'r') as config_file:
        config = yaml.load(config_file)

    ds_url_base = 'https://api.darksky.net/forecast'
    ds_api_key = config['locweat']['apikey']
    exclude = '?exclude=flags,alerts'
    lat_lon = get_loc()
    latitude, longitude = lat_lon[0], lat_lon[1]
    ds_request = '%s/%s/%s,%s%s'%(ds_url_base, ds_api_key,latitude,longitude,exclude)
    ds_r = requests.get(ds_request)
    ds_j = json.loads(ds_r.text)
    return ds_j

def main():
    j_weat = get_weat()
    print (j_weat['daily']['summary'], j_weat['hourly']['summary'], j_weat['minutely']['summary'])

if __name__ == '__main__':
    main()
