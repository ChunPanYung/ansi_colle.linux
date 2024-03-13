import yaml


def get_version(file: str) -> str:
    with open(file) as stream:
        try:
            data: dict = yaml.safe_load(stream)
            return data["version"]
        except yaml.YAMLError as exc:
            print(exc)
            return "Error"
