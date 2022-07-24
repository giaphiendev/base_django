# INSTALLATION

* Copy `.env.example` to `.env` and edit it to your needs.
* `$ cp .env.example .env`

# WITHOUT DOCKER

# WITH DOCKER

* `$ docker-compose -f docker/docker-compose.yml up -d --build`
* Open browser and go to `localhost:8000/api/doc/` to see swagger

## Migrate for the first time

* `docker-compose -f docker/docker-compose.yml exec backend python manage.py migrate`

### Get container's log

* `$ docker logs [container_name] -f`

### Seed data (Role)

* `$ docker-compose -f docker/docker-compose.yml exec backend python manage.py loaddata seed/0001_Role.json`

### Git
- `$ ssh-keygen`
- `$ eval 'ssh-agent -s'`
- `$ ssh-add ~/.ssh/id_rsa`
- `$ cat ~/.ssh/id_rsa.pub`

### acc git 
- `giaphiendev`
- `hien0388423***`