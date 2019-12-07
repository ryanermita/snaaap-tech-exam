FROM python:3.7-alpine3.9

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/app.py"]
 