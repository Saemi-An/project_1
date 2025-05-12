import os

# from core.general.utils.misc import yaml_coerce   # 테스트용 절대경로 import
from .misc import yaml_coerce

# 환경변수를 순회하며 특정 접두사로 시작하는 항목들만 추려서 딕셔너리 형태로 가공하여 반환하는 함수

# ============================================================
# **************************** 예시 ***************************
# ============================================================

# 환경변수 목록
# test = {
#     "TS_IN_DOCKER": "1",
#     "TS_DEBUG": "true",
#     "OTHER_VAR": "ignored"
# }

# prefix = 'TS_'

# 모든 환경변수 목록을 순회하며
# 특정 prefix로 시작하는 환경변수들만 모아
# prefix를 뗀 부분을 키: 문자열 환경변수를 파이썬 문법에 맞게 변경한 값
# 을 갖는 딕셔너리 반환

# {'IN_DOCKER': 1, 'DEBUG': True}

# ============================================================
# ************************************************************
# ============================================================


def get_settings_from_environment(prefix):

    prefix_len = len(prefix)

    # tmp = {}
    # for key, value in test.items():   # 모든 환경변수 목록 탐색
    #     if key.startswith(prefix):   # prefix 필터링
    #         tmp[key[prefix_len:]] = yaml_coerce(value)   # prefix 떼고 뒷부분을 키로, 값은 yaml_coerce(value)로 하여 딕셔너리에 추가

    # return tmp

    return {key[prefix_len]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
