# Restrict usage of registry servers

## This cluster policy blocks usage any of registry servers with exception `registry.gitlab.com` and `gcr.io` but it is not applied to the namespaces which starts with `kube*` and kyverno

### Apply `ClusterPolicy` and `Deployment` (with wrong image) manifests

```bash
$ kubectl apply -f cpol-restrict-image-registries.yaml
$ kubectl apply -f deployment.yaml
```

#### To test it we can use the following commands to change image in deployment

```bash
$ kubectl -n check-kyverno patch deployment webapp --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value": "nginx:latest"}]'
$ kubectl -n check-kyverno patch deployment webapp --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value": "registry.gitlab.com/gitlab-examples/nginx"}]'
$ kubectl -n check-kyverno patch deployment webapp --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value": "gcr.io/cloud-builders/nginx"}]'
```

#### The simulation as following

![Simulation](https://github.com/jamalshahverdiev/kyverno/blob/main/Image-Registry-Policies/Restrict-Image-Registry/tmux-session-optimized.gif)