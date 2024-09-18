#!/bin/bash

# Cleanup the application
echo "Cleaning up the application..."

# Remove Ingress
kubectl delete -f k8s/ingress/web-ingress.yaml

kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Remove Web application Deployment and Service
kubectl delete -f k8s/deployments/web-deployment.yaml
kubectl delete -f k8s/services/web-service.yaml

# Remove PostgreSQL StatefulSet and Service
kubectl delete -f k8s/statefulsets/postgres-statefulset.yaml
kubectl delete -f k8s/services/postgres-service.yaml

# Remove PersistentVolumeClaim
kubectl delete -f k8s/volumes/postgres-data-persistentvolumeclaim.yaml

# Remove ConfigMap and Secrets
kubectl delete -f k8s/configmaps/env-configmap.yaml
kubectl delete -f k8s/secrets/secrets.yaml

# Remove namespace
kubectl delete -f k8s/namespaces/wog-namespace.yaml

echo "Cleanup complete."