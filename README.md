docker build -t omdbapi .

docker run omdbapi python /src/api.py "batman" <api_key>
