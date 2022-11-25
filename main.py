from utils import download_data, load_yaml, translate

yaml = load_yaml("config.yaml")

if __name__ == '__main__':
    #example on how to download_data
    download_data(yaml["file-url"])

    #example on how to translate a string
    tar = translate("I want to eat", yaml["translation-api"], "en", "id")
    print(tar)
