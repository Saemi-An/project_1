if IN_DOCKER:  # type: ignore # noqa: F821

    print('도커모드에서 실행중..')
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa: F821
        'django.middleware.security.SecurityMiddleware'
    ]
