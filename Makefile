.PHONY: install   # 타겟이 실행될 때 타겟명을 파일로 간주하고 찾게됨 // 파일이 아님을 명시하여 생산성 증대 + 동일한 파일명 있어도 여기서 찾도록
install:
	poetry install

# hook에 변경사항이 있을 때 pre-commit 도구를 통해 기존 hook 전체 삭제 및 재다운로드
.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

# pre-commit 툴을 사용하여 코드 스타일 수동 확인
.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m core.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python -m core.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

.PHONY: update
update: install migrate install-pre-commit ;
