FROM python:3.11-slim
RUN apt-get update && apt-get install -y chromium 2>/dev/null || true
COPY . /app
WORKDIR /app
RUN pip install -e ".[all]" 2>/dev/null || pip install -e .
CMD ["python3", "-c", "from stealth_core.guardian import ProcessGuardian; print('stealth ready')"]
