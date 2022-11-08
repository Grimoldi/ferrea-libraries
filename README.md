# Ferrea-Libraries

Repo for Ferrea project. Dedicated to the libraries microservice.

This microservice is responsible for handling the libraries inside the circuit.

## Run as a docker container

``` bash
docker build --tag ferrea-libraries .

docker run --name ferrea-lib -d -p 8000:80 ferrea-libraries
```

## Run on Kubernetes

Apply the manifests you can find under k8s folder.

``` bash
kubectl apply -f k8s/
```

## Web service structure

The web service has three distinct layers:

- web api layer: the routing of the api (./src/routers folder).
- business logic layer: the logic under the hood (./src/operations folder).
- data layer: how to access to the data (./src/models folder).

### Openapi Schema

You can find the OpenApi exposed under the */docs/libraries* endpoint.

The OpenApi definitions are stored under the ./src/definitions folder.
