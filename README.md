# dataset-translator

## How to Setup
```bash
sudo apt install -y wget unzip
pip install -r requirements.txt
```

## How to Config
```yaml
file-url: https://pl-flash-data.s3.amazonaws.com/wmt_en_ro.zip
source-language: en
target-language: id
translation-api: https://translate.googleapis.com/translate_a/single?client=gtx&sl=
translate-file: data/train.csv
```

## Usefull Function
```python
def download_data(file_url:str, dest_path:str="data"):
    os.system(f"wget -P {dest_path} {file_url}")
    os.makedirs(dest_path, exist_ok=True)
    os.system(f"unzip {dest_path}/{file_url.split('/')[-1]} -d {dest_path}")
    os.remove(f"{dest_path}/{file_url.split('/')[-1]}")


def translate(text:str, translate_api:str, source_language:str, target_language:str)->str:
    url = translate_api+source_language+"&tl="+target_language+"&dt=t&q="+text
    x = requests.get(url)

    return x.json()[0][0][0]
```

## How to run
you need to do yourself for the dataloader and datasaver, because every data is different on translate_file
```python
def translate_file(file_path:str):
    raise NotImplementedError
```

if you not implement that you will get error NotImplementedError
```bash
python main.py
```