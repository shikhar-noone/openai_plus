start:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

build:
	docker build -t openai_plus_image .

remove-app:
	docker exec openai_container rm -rf openai_plus

copy-app:
	docker cp ./openai_plus openai_container:.app/

deploy:
	python manage.py makemigrations
	python manage.py migrate
	docker exec openai_container rm -rf openai_plus
	docker cp ./openai_plus openai_container:.app/
	docker restart openai_container


deploy-conf:
	docker rm -f openai_container
	docker build -t openai_plus_image .
	docker run --env-file .env \
		--name openai_container \
		-v $(shell pwd):/app \
		-p 8030:8020 \
		openai_plus_image

remove-container-image:
	docker rm -f openai_container
	docker rmi openai_plus_image

shell_plus:
	docker exec openai_container python manage.py shell_plus --ipython

reload-nginx:
	docker exec -it openai_container service nginx reload

migrate:
	docker run --rm openai_plus_image python manage.py migrate

makemigrations:
	docker run --rm openai_plus_image python manage.py makemigrations

getvolume:
	docker inspect -f '{{ .Mounts }}' openai_container