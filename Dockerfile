FROM python:3.9-buster


RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p app
# RUN mkdir -p app/pip_cache
# COPY data/.pip_cache app/pip_cache/
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
COPY . /app

# RUN pip install -r requirements.txt --cache-dir app/data/pip_cache
RUN python manage.py collectstatic --no-input
RUN chown -R www-data:www-data /app

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["./start-server.sh"]