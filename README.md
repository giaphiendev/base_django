# INSTALLATION

* Create folder `.envs` contain 3 files `.env.django_app` - `.env.mysql` - `.env.node_app`

# WITHOUT DOCKER

# WITH DOCKER

* `$ docker-compose up -d --build`
* Open browser and go to `localhost:8000/api/doc/` to see swagger (django app)
* Open browser and go to `localhost:5005` to check app (node app)

## Migrate for the first time

* `docker-compose exec project_sem4_django python manage.py migrate`

## Import data.sql by hand (if run command above: dont run this)
* `$ docker exec -it project_sem4_mysql bash`
* `$ mysql -u root -p`
* Type `root` press enter to go ahead!

* `$ create databases techwiz;`
* `$ exit`
* `$ mysql -u root -p techwiz < ./data_sample/data.sql`
* Type `root` press enter to go ahead!




### Get container's log

* `$ docker logs [container_name] -f`

### Seed data (Role)

* `$ docker-compose exec project_sem4_django python manage.py loaddata seed/0001_Role.json`

## Process signup and login

- call `api/auth/get-pin` to generate pin and get token for validate pin
- after that, call `api/auth/sign-up`  to sign up or `api/auth/login` to login

### Git

- `$ ssh-keygen`
- `$ eval 'ssh-agent -s'`
- `$ ssh-add ~/.ssh/id_rsa`
- `$ cat ~/.ssh/id_rsa.pub`

### acc git

- `giaphiendev`
- `h***0388******`

### To push noti - follow [this tutorial](https://docs.expo.dev/push-notifications/sending-notifications/)
