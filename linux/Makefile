# Run the database Docker container
start-db:
	docker build -t wavedb -f database/Dockerfile .
	docker run \
	 	-d \
		--name wavedb-container \
		-p 5432:5432 \
		-e POSTGRES_PASSWORD=password \
		wavedb

# Migration
run-migrations:
	docker build -f=db/migrations/Dockerfile ./db/migrations -t migrations && \
	docker run \
		--network "host" \
		-e POSTGRES_HOST=localhost \
		-e POSTGRES_DB=wavedb \
		-e POSTGRES_USERNAME=postgres \
		-e POSTGRES_PORT=5432 \
		-e POSTGRES_PASSWORD=password \
		migrations


# Stop and remove the database container
stop-db:
	docker stop wavedb-container
	docker rm wavedb-container

# Clean up the database image
clean-db:
	docker rmi wavedb-image

.PHONY: run-db stop-db clean-db
