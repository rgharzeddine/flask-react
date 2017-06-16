# Notes

## Docker

**Problem**

**docker-compose up -d** did not start
docker had problems mounting volume

**Solution**

1. add user to docker group
2. use native machine on linux and do not build a machine

------------------------------------------------------

**Problem**

**test_add_user()** test failed

**Solution**

* change posted data useruser to username

------------------------------------------------------

**Problem**

nginx container build path not found by docker

**Solution**

changed nginx build to build : ./flask-microservices-main/nginx

------------------------------------------------------
