

## Local 
Clone code to your local folder

test code:
`python api.py "batman" <api_key>`

## Docker
* Install Docker 
refer : https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

* Check if Docker is running : docker run hello-world

`docker build -t omdbapi .`

`docker run omdbapi "batman" <api_key>`

### Todo
- [x] Dockerize
- [ ] Add UnitTest Cases
