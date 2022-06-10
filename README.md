# e-commerce_microservices

This repository implements microservices based e-commerce app. Currently, two services are provided: 
1. api_gateway - it takes all requests from client side and communicates to the other services. `api_gateway` is responsible for user authentication/authorization as well. 
It is built using FastAPI framework. Communication with client side is implemented in `REST API`. On the other hand, `gRPC` is used for communications with other back-end services.
2. customers - it provides `gRPC` service methods to implement CRUD operations on MongoDB database.


## How to run
Note: It is assumed that you have installed `Docker` and `MongoDB` server 
(server should listen to the standard MongoDB port, 27017).

1. Update api_gateway/.env file:
   1. Run in terminal `openssl rand -hex 32` and paste generated key to the `SECRET_KEY`.
2. Run following command from the root: `docker-compose up --build`.
3. Open your browser at http://localhost:8000/docs to see API documentation.