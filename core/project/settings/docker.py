# Docker 환경에서 MIDDLEWARE 설정이 기대한 보안 구조를 따를 것을 assert로 강제(하는 안전장치)
# 조건이 충족되지 않을시 AssertionError 에러와 함께 즉시 실행 종료됨

# 서버 실행시 core/project/settings/__init__.py에서 include()의 실행 순서 덕분에(split-setting 덕분에) 갠춘
if IN_DOCKER:  # type: ignore # noqa: F821

    # MIDDLEWARE 리스트의 첫 번째 요소가 SecurityMiddleware임을 확실하게 함
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa: F821
        'django.middleware.security.SecurityMiddleware'
    ]
