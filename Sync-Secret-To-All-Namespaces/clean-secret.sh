#!/usr/bin/env bash

secret_name='imagepullsecretcred'
ns_names_where_secret=$(kubectl get secrets -A | grep $secret_name | awk '{ print $1 }')

for ns_name in $ns_names_where_secret; do
    kubectl delete secret $secret_name -n $ns_name
    #echo "Secret name: $secret_name || NS name: $ns_name"
done
