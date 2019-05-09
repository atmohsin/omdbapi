FROM python:2.7-slim
COPY . /omdbapi 
WORKDIR /omdbapi
RUN pip install -r /omdbapi/requirements.txt
ENTRYPOINT ["python","/omdbapi/api.py"]