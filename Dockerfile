FROM python:3.12.9


WORKDIR /app

### copy files for uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

### install python packages via uv
COPY pyproject.toml ./pyproject.toml
COPY uv.lock ./uv.lock

ENV UV_NO_DEV=1 \
    UV_FROZEN=1

RUN uv sync


### copy files in repo
COPY src ./src
COPY README.md ./README.md
COPY api ./api
COPY models ./models



### run api
CMD ["uv", "run", "uvicorn", "api.fast:app", "--host", "0.0.0.0","--port","8080"]
