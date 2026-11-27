FROM python:3.12.9

#installation de uv !!!
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# set work folder
WORKDIR /app

# install venv and all python package needed with uv
COPY pyproject.toml uv.lock README.md ./
ENV UV_NO_DEV=1 \
    UV_FROZEN=1
RUN uv sync

# copy other script python using in this project
COPY src src
COPY api api
# copy model using for this project
COPY models models


# run api
CMD ["uv", "run", "uvicorn", "api.fast:app", "--host", "0.0.0.0", "--port", "8080"]
