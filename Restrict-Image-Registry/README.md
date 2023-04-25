# Restrict usage of registry servers

## This cluster policy blocks usage any of registry servers with exception `registry.gitlab.com` and `gcr.io` but it is not applied to the namespaces which starts with `kube*` and kyverno

### Apply `ClusterPolicy` and `Deployment` (with wrong image) manifests

```bash
$ kubectl apply -f cpol-restrict-image-registries.yaml
$ kubectl apply -f deployment.yaml
```

#### The simulation as following

![Simulation](https://github.com/jamalshahverdiev/kyverno/blob/main/Restrict-Image-Registry/tmux-session-optimized.gif)