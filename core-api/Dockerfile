FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

# store virtualenv outside mounted folder
ENV UV_PROJECT_ENVIRONMENT=/opt/venv

COPY pyproject.toml uv.lock* ./

RUN uv sync --no-dev

COPY . .

ENV PATH="/opt/venv/bin:$PATH"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]