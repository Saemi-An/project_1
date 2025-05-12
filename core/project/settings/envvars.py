from core.general.utils.collections_utils import deep_update
from core.general.utils.settings import get_settings_from_environment

# export CORE_SETTINGS_IN_DOCKER = True
# 위와 같은 환경변수가 있을 때 이를 파이썬 문법으로 변환한 뒤 전역 변수에 업데이트한다.
# globals() is a dictionary of global variables

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821

# 서버 실행시 core/project/settings/__init__.py에서 include()의 실행 순서 덕분에(split-setting 덕분에) 갠춘
