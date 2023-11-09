#!/bin/bash 

uvicorn src.main:app --host 0.0.0.0 --port $GEO_ROUTER_PORT --reload --log-level debug
# gunicorn src.main:app -k uvicorn.workers.UvicornWorker --reload --bind 0.0.0.0:$GEO_ROUTER_PORT