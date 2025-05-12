import os.path
from pathlib import Path

from split_settings.tools import include, optional

# BASE_DIR 설정
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# 환경변수 prefix 정의
# Namespacing(프로그램에서 사용되는 이름의 논리적 그룹인 식별자의 컨텍스트) (?)
ENVVAR_SETTINGS_PREFIX = 'CORE_SETTINGS_'

# 팀원들이 (템플렛을 사용해)각자의 로컬머신에서 settings.dev.py가 아닌 커스텀 세팅파일을 만들 경우(?)
LOCAL_SETTINGS_PATH = os.getenv(f'{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH')

if not LOCAL_SETTINGS_PATH:  # 커스텀 세팅파일 없으면
    LOCAL_SETTINGS_PATH = 'local/settings.dev.py'  # 디폴트 세팅파일 사용

# 팀원의 커스텀 세팅파일 path가 상대경로일 경우 절대경로로 변경
if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

# 다수의 설정파일을 종합 (순서 중요)
include('base.py', 'custom.py', optional(LOCAL_SETTINGS_PATH), 'envvars.py', 'docker.py')
