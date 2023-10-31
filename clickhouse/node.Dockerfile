FROM yandex/clickhouse-server:22.1

COPY ./server_config /etc/clickhouse-server
COPY ./server_config/metrika.xml /etc/metrika.xml
