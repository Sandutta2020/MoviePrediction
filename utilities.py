from pathlib import Path
from typing import Union

import yaml
from yaml import Loader


def read_yaml(file: Union[str, Path], key: str = None) -> dict:
    with open(file, "r") as fp:
        params = yaml.load(fp, Loader)
    return params[key] if key else params
def get_movie_list(Genre):
    final_list =[]
    with open("config.yaml", "r") as fp:
        params = yaml.load(fp, Loader)
        for item in Genre:
            for movies in params[item][0:6]:
                final_list.append([item,movies])
    return final_list


