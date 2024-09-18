#!/bin/bash

helm delete wog-charts --namespace wog
kubectl delete namespace wog

helm delete ingress-nginx --namespace ingress-nginx
kubectl delete namespace ingress-nginx