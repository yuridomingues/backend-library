default:
	uvicorn src.main:app --reload

db:
	sudo docker compose up -d