# 인자 2개 전달: original dict, new values(update original dict as nested way)
# base_dict를 nested value로 업데이트 해주는 함수
def deep_update(base_dict, updated_with):

    # 새로 들어온 값 순회
    for key, value in updated_with.items():

        # 만일 value가 dict 타입 이라면
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)  # base_dict에서 같은 key를 갖는 애를 찾아 변수에 담는다

            # 만일 원본 value 또한 dict 타입 이라면 재귀함수 호출
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            else:
                base_dict[key] = value

        # 만일 value가 dict 타입이 아니라면 새로운 value로 업데이트
        else:
            base_dict[key] = value

    return base_dict
