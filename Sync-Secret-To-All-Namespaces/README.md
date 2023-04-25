# Syncronize secret to all namespaces

## Just imagine we have secret where stored credentials to some docker registry endpoint and we must syncronize it to any other namespaces to be accessable inside our deployments to use it

### We syncronize `Secret` with name `imagepullsecretcred` to all another nemespaces but, excluded all namespaces which starts with `kube` and `kyverno` itself

**Note:** In case of delete key inside of the secret directly will not be syncronized. If we create new secret key or update some value of the existing key it will be syncronized. If we delete key at the same time add new key with some value it will be syncronized too

#### Create namespace with name `sourcesecret` and then create secret with name `imagepullsecretcred`

```bash
$ kubectl create ns sourcesecret
$ kubectl apply -f secret.yaml
```

#### Then apply `ClusterPolicy` YAML file which will do syncronize for us from secret `imagepullsecretcred` of `sourcesecret` namespace

```bash
$ kubectl apply -f cpol-to-sync-secret-another-namespaces.yaml
```

#### The simulation as following

![Simulation](https://github.com/jamalshahverdiev/kyverno/blob/main/Sync-Secret-To-All-Namespaces/tmux-session-optimized.gif)