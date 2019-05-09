FROM python:2.7-slim
COPY . /src
RUN pip install -r /src/requirements.txt
CMD ["python", "/src/api.py"]
