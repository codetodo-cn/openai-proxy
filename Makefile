
up:
	docker-compose up -d

down:
	docker-compose down

dev:
	docker exec -it openai-proxy /bin/bash

logs:
	docker logs -f openai-proxy

restart:
	make down && make up
