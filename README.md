# datawagon Трек 3

## Запуск проекта
``` 
# Копирование переменных окружения
cp .env.example .env 

# Скачать образ кликхауса
docker pull clickhouse/clickhouse-server:23.9.3-alpine

# Копирование файлов настроек для nginx
rm -rf ./nginx/static && cp -r ./nginx/static_defaults/ ./nginx/static

# Запуск проекта
make dev