start:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

build:
	docker build -t openai_plus_image .

remove-app:
	docker exec openai_container rm -rf openai_plus

copy-app:
	docker cp ./openai_plus openai_container:./opt/app/

deploy:
	python manage.py makemigrations
	python manage.py migrate
	docker exec openai_container rm -rf openai_plus
	docker cp ./openai_plus openai_container:./opt/app/
	docker restart openai_container


deploy-conf:
	python manage.py makemigrations
	python manage.py migrate
	docker build -t openai_plus_image .
	docker run --name openai_container -it -p 8020:8020 \
		-e DJANGO_SUPERUSER_USERNAME=admin \
		-e DJANGO_SUPERUSER_PASSWORD=sekret1 \
		-e DJANGO_SUPERUSER_EMAIL=admin@example.com \
		openai_plus_image

remove-container-image:
	docker rm -f openai_container
	docker image rm openai_plus_image
