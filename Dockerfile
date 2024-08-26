FROM python:3.12-slim

WORKDIR /flaskintro

COPY ./src /flaskintro/src
COPY ./tests /flaskintro/tests
COPY ./env /flaskintro/env
COPY ./requirements.txt /flaskintro
COPY ./pytest.ini /flaskintro

RUN pip install --no-cache-dir -r requirements.txt && \
    pytest -v

EXPOSE 5000

ENV FLASK_APP=src/app.py
ENV FLASK_ENV=production

# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["python3", "src/app.py"]
# CMD ["sleep", "infinity"]