FROM python:3.11-slim AS admin-builder

WORKDIR /opt
COPY requirements.txt .

RUN apt-get update && apt-get install -y build-essential python3-dev cmake gcc musl-dev \
     && pip install --upgrade pip \
     && pip3 install wheel && pip3 wheel -r requirements.txt --wheel-dir=/opt/wheels


FROM python:3.11-slim

COPY --from=admin-builder /opt /opt

RUN apt-get update && apt-get install -y build-essential python3-dev cmake gcc musl-dev libc-dev gdal-bin libgdal-dev python3-gdal binutils libproj-dev

WORKDIR /opt/admin
EXPOSE ${ADMIN_APP_PORT}
ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]

COPY . .
RUN  mkdir -p /var/www/static/ && pip install --no-index --find-links=/opt/wheels -r requirements.txt