FROM python:3.12-alpine

WORKDIR /animal_store

RUN pip install uv --no-cache-dir

COPY pyproject.toml uv.lock .python-version ./

RUN uv sync --no-cache

COPY . .

CMD ["uv", "run", "python", "-m", "main"]
