# base_dict를 nested value로 업데이트 해주는 재귀 함수

# ============================================================
# **************************** 예시 ***************************
# ============================================================

# original dict - base.py의 DATABASE 설정
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'pro_django',
#         'USER': 'pro_django',
#         'PASSWORD': 'pro_django',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

# updated_with - docker-compse.yml에서 변경사항
# {'default':{'HOST':'db'}}

# 위 두개의 인자를 받아 key가 일치하면 updated_with의 value로 바꿔준 뒤
# 업데이트된 original dict를 반환
# 재귀호출을 통해 nested_dict를 순회하며 값을 바꿔줌

# ============================================================
# ************************************************************
# ============================================================


def deep_update(base_dict, updated_with):

    # 새로 들어온 값 순회
    for key, value in updated_with.items():

        # 만일 value가 dict 타입 이라면
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)  # base_dict에서 같은 key를 갖는 애를 찾아 그 value를 변수에 담음

            # 만일 원본 value 또한 dict 타입 이라면 재귀함수 호출
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            # 그렇지 않으면 값 업데이트
            else:
                base_dict[key] = value

        # 만일 value가 dict 타입이 아니라면 새로운 value로 업데이트
        else:
            base_dict[key] = value

    return base_dict
