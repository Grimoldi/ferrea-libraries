# Ferrea-Libraries

Repo for Ferrea project. Dedicated to the libraries microservice.

This microservice is responsible for handling the libraries inside the circuit.

## Run as a docker container

``` bash
docker build --tag grimoldi/ferrea-libraries:latest .

docker run --name ferrea-lib -d -p 8000:80 --env DB_USR=<user> --env DB_PWD=<user s password> --env DB_URL=<db url> --env FERREA_APP=libraries ferrea-libraries
```

## Run on Kubernetes

Apply the manifests you can find under k8s folder.

``` bash
kubectl apply -f k8s/
```

Please note that the Secret Manifest should be compiled with the actual password, url and so on.

## Web service structure

The web service has three distinct layers:

- web api layer: the routing of the api (./src/routers folder).
- business logic layer: the logic under the hood (./src/operations folder).
- data layer: how to access to the data (./src/models folder).

### Openapi Schema

You can find the OpenApi exposed under the */docs/libraries* endpoint.

The OpenApi definitions are stored under the ./src/definitions folder.
