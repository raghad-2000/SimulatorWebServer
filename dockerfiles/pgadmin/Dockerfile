FROM dpage/pgadmin4

COPY server.json servers.json
RUN /venv/bin/python3 /pgadmin4/setup.py --load-servers servers.json

