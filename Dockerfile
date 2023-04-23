FROM python:3.10-slim-buster
WORKDIR /src
COPY requirements.txt requirements.txt
RUN  apt-get update  && apt-get install -y p7zip-full
RUN pip3 install -r requirements.txt
COPY . .
CMD ["uvicorn", "src.main:app"]
