#!/bin/bash

# Deploy the application
echo "Deploying the application..."

# Create namespace
kubectl apply -f k8s/namespaces/wog-namespace.yaml

# Install NGINX Ingress Controller (if not already installed)
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml



# Apply ConfigMap and Secrets
kubectl apply -f k8s/configmaps/env-configmap.yaml
kubectl apply -f k8s/secrets/secrets.yaml

# Create PersistentVolumeClaim
kubectl apply -f k8s/volumes/postgres-data-persistentvolumeclaim.yaml

# Deploy PostgreSQL StatefulSet and Service
kubectl apply -f k8s/statefulsets/postgres-statefulset.yaml
kubectl apply -f k8s/services/postgres-service.yaml

# Deploy Web application Deployment and Service
kubectl apply -f k8s/deployments/web-deployment.yaml
kubectl apply -f k8s/services/web-service.yaml

# Deploy Ingress
kubectl apply -f k8s/ingress/web-ingress.yaml

# Verify deployment
echo "Verifying deployment..."
kubectl get all -n wog
kubectl get ingress -n wog
