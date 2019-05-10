FROM python:alpine3.7
COPY . /omdbapi 
WORKDIR /omdbapi
RUN pip install -r /omdbapi/requirements.txt
ENTRYPOINT ["python","/omdbapi/api.py"]