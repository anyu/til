# Docker

## Overview

Docker uses a client-server architecture.

Docker client (`docker` CLI, docker compose) talks to Docker daemon (`dockerd`) via Docker's REST API.

## Components

### Docker daemon (dockerd)

- Listens for API requests and manages Docker objects (images, containers, networks, volumes)

### Docker client (docker)

- Client sends commands to `dockerd` via Docker API

### Docker registries

- Stores Docker images; Docker looks for images in Docker Hub by default
