run:
	uvicorn workout_api.main:app --reload

create-migrations:
	set PYTHONPATH=%cd% && python -m alembic revision --autogenerate -m "$(d)"

run-migrations:
	set PYTHONPATH=%PYTHONPATH%;%cd% && alembic upgrade head