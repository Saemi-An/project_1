from core.core.utils.collections_utils import deep_update
from core.core.utils.settings import get_settings_from_environment

# globals() is a dictionary of global variables
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
# 서버 실행시 core/project/settings/__init__.py에서 include()의 실행 순서 덕분에(split-setting 덕분에) 갠춘
