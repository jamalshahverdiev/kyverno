
```bash
$ kubectl apply --server-side -f manifests/setup --force-conflicts
$ kubectl wait --for condition=Established --all CustomResourceDefinition --namespace=monitoring
$ kubectl apply -f manifests/
```