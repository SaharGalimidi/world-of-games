#!/bin/bash

# install ingress using helm
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace


helm upgrade wog-charts wog-charts --install --namespace wog #--create-namespace #--values values.yaml