import yaml


# 도커 설정파일에서 str_dict로 환경변수가 설정되면 이를 인자로 받아 파이썬 문법으로 변환하여 반환해주는 함수
# '{"default":{"HOST":"db"}}' --> {'default': {'HOST': 'db'}} <class 'dict'>
def yaml_coerce(value):
    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
