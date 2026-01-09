FROM python:3.10-slim
WORKDIR /student
COPY . .
RUN pip install --no-cache-dir pytest
# Run tests at build time (CI)
RUN pytest -v
ENTRYPOINT [ "python", "student.py" ]