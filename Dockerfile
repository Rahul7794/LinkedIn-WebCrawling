FROM python:3.6.0-slim

COPY . /app

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

WORKDIR app
RUN pip install --user -r /app/requirements.txt
ENTRYPOINT ["python","/app/main.py"]