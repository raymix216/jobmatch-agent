FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src/ ./src/
RUN pip install --no-cache-dir .

EXPOSE 8000

# M0: health check only; API server lands in M2 with the router.
CMD ["python", "-m", "jobmatch", "health"]
