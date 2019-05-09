docker build -t omdbapi .
docker run omdbapi python /src/api.py "True Grit"
