FROM --platform=linux/amd64 python:3.12

WORKDIR /app

RUN pip install --no-cache-dir pdm

COPY pyproject.toml ./

COPY src/aiasan ./src/aiasan
COPY src/hanazono/__init__.py ./src/hanazono/__init__.py

RUN pdm install --without aiassistant
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

COPY src ./src
COPY mkdocs.yml ./
COPY docs ./docs

CMD ["sh", "-c", "pdm run init && pdm run gunicorn hanazono_conf.wsgi --timeout 600"]
