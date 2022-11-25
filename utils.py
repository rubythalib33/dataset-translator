import os
import requests
import yaml


def load_yaml(yaml_path:str) -> dict:
    with open(yaml_path, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
            return {}


def download_data(file_url:str, dest_path:str="data"):
    os.system(f"wget -P {dest_path} {file_url}")
    os.makedirs(dest_path, exist_ok=True)
    os.system(f"unzip {dest_path}/{file_url.split('/')[-1]} -d {dest_path}")
    os.remove(f"{dest_path}/{file_url.split('/')[-1]}")


def translate(text:str, translate_api:str, source_language:str, target_language:str)->str:
    url = translate_api+source_language+"&tl="+target_language+"&dt=t&q="+text
    x = requests.get(url)

    return x.json()[0][0][0]
    