FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir pdm

COPY pyproject.toml ./

COPY src/aiasan ./src/aiasan
COPY src/hanazono/__init__.py ./src/hanazono/__init__.py

RUN pdm install --without aiassistant
ENV PATH="/app/.venv/bin:$PATH"

COPY src ./src
COPY mkdocs.yml ./
