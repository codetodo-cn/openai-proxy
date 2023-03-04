
up:
	docker-compose up

down:
	docker-compose down

dev:
	docker exec -it openai-proxy /bin/bash

logs:
	docker logs -f openai-proxy

restart:
	make down && make up
