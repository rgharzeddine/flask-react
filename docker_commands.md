# docker commands

| Scope             | Purpose                          |               Command                             |
|-------------------|----------------------------------|---------------------------------------------------|
| machine           | list machines                    | docker-machine ls                                 |
| machine           | create machine                   | docker-machine create -d virtualbox dev           |
| machine           | delete machine                   | docker-machine rm dev                             |
| machine           | start machine                    | docker-machine start dev                          |
| machine           | configure shell                  | eval $(docker-machine env dev)                    |
| image             | list images                      | docker images                                     |
| image             | delete image                     | docker rmi python                                 |
| image             | build image                      | docker build -t alpine:1.3                        |
| container         | list all containers              | docker ps -a                                      |
| container         | list active containers           | docker ps                                         |
| container         | delete container                 | docker rmi dazzling_darwin                        |
| container         | run container                    | docker run --rm -p 5001:5000                      |
|                   |                                  |                                                   |

