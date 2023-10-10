FROM python:3.11

WORKDIR /app

COPY pyproject.toml ./
COPY src ./src

RUN pip install --no-cache-dir pdm
RUN pdm install
ENV PATH="/app/.venv/bin:$PATH"

COPY mkdocs.yml .