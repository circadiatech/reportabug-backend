# Report A Bug - backend

Local Setup

1. Install Docker
2. Install Docker Compose
3. Run `docker compose build`
4. Run `docker compose up -d`
5. Run `docker-compose exec web flask db migrate -m "X model migration."` when you create new model
6. Run `docker-compose exec web flask db upgrade` when you start project first time to create tables for the already created migrations
