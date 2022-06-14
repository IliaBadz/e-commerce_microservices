# e-commerce_microservices

This repository implements microservices based e-commerce app. Currently, it is under development. Following services are provided for now: 
1. api_gateway: 
   1. takes all requests from client side and redirects them to the other services;
   2. is responsible for Authentication/Authorization of consumer;
   3. communicates with client side through `REST API`;
   4. uses [FastAPI](https://fastapi.tiangolo.com/) web framework for building APIs;
   5. implements [async gRPC client](https://grpc.github.io/grpc/python/grpc_asyncio.html)  to communicate with back-end services;
2. customers:
   1. saves customer credentials to the MongoDB database; 
   2. provides asynchronous `gRPC` service methods to implement CRUD operations on MongoDB database;
   3. uses [Beanie](https://roman-right.github.io/beanie/) an asynchronous Python object-document mapper (ODM) for MongoDB;


## How to run
**Note**: It is assumed that you have installed [Docker](https://www.docker.com/) and [MongoDB server](https://www.mongodb.com/) 
(server should listen to the standard MongoDB port, 27017).

1. Update api_gateway/.env file:
   1. Run in terminal `openssl rand -hex 32` and paste generated key to the `SECRET_KEY`.
2. Run following command from the root: `docker-compose up --build`.
3. Open your browser at http://localhost:8000/docs to see API documentation.