
FROM python:3.9-slim

RUN apt-get update && apt-get install -y git

WORKDIR /srv

COPY requirements.txt . 

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

RUN pip install --no-cache-dir --upgrade -r requirements.txt || cat /tmp/pip-error.log

RUN pip install git+https://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@github.com/VladimirJz/safi-core-library.git@release-candidate#egg=safi

COPY ./src /srv

COPY .env  /srv


EXPOSE 3007

CMD ["fastapi", "run", "main.py", "--port", "3007"]
