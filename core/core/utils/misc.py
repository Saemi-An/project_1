import yaml


# value를 파이썬 문법으로 변경해주는 함수
def yaml_coerce(value):
    # yaml.load로 파이썬 객체를 반환하도록 함
    # "{'apples': 1, 'banana': 2}"와 같은 str dict를 파이썬 딕셔너리 타입으로 변환
    # 도커파일 등에서 설정들을 문자열로 해야하기 때문에 이와같은 경우에 유용함
    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
