import os

from .misc import yaml_coerce

# 환경변수 중 'CORESETTINGS_IN_DOCKER = 1'이 있다면
# {'IN_DOCKER': 1}과 같은 형태로 바꿔줌


def get_settings_from_environment(prefix):

    prefix_len = len(prefix)
    return {key[prefix_len]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
