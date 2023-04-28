# Restrict usage docker images with latest tag

## This cluster policy blocks usage any of images with `latest` tag but, it is not applied to the namespaces in the `exclude` section of `ClusterPolicy` `kind`

### Apply `ClusterPolicy` and `Deployment` (with wrong image) manifests

```bash
$ kubectl apply -f cpol-image-deny-latest-tag.yaml
$ kubectl apply -f deployment.yaml
```

#### Applied `Deployment` uses `docker.io/nginx:1.24.0` image but to test it we can use the following commands to change image in deployment

```bash
$ kubectl -n check-kyverno patch deployment webapp --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value": "docker.io/nginx:latest"}]'
```

#### At the same time you can you to check it in the `kube-system` namespace which is already excluded

```bash
$ kubectl run application --image=docker.io/nginx:latest --namespace=kube-system
$ kubectl run application --image=docker.io/nginx:latest --namespace=check-kyverno
$ kubectl run application --image=docker.io/nginx:1.24.0 --namespace=check-kyverno
```

#### The simulation as following

![Simulation](https://github.com/jamalshahverdiev/kyverno/blob/main/Image-Registry-Policies/Deny-Latest-Image-Tag/tmux-session-optimized.gif)