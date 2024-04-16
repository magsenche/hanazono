FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir pdm

COPY pyproject.toml ./
RUN mkdir -p src/hanazono

RUN pdm install
ENV PATH="/app/.venv/bin:$PATH"

COPY src ./src
COPY mkdocs.yml ./
