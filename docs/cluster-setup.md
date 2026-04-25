# Local Cluster Setup

## Prerequisites

- Docker Desktop running
- Minikube installed (`brew install minikube`)
- kubectl installed (`brew install kubectl`)

## Start the cluster

```bash
minikube start --driver=docker --cpus=2 --memory=3000 --disk-size=20g
```

## Enable addons

```bash
minikube addons enable dashboard
minikube addons enable metrics-server
minikube addons enable ingress
```

## Create project namespace

```bash
kubectl create namespace cloudnative
```

## Verify cluster

```bash
minikube status
kubectl get nodes
kubectl get pods --all-namespaces
```

## Stop the cluster

```bash
minikube stop
```