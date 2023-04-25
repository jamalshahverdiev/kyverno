# Kyverno must be installed 

## Apply all the following commands to create new ClusterRole, ClusterRolebinding, ClusterPolicy, Secret and Deployment objects inside of the `check-kyverno` namespace

### Give an access to the Kyverno `ServiceAccount` after which our deployment will be restarted when some key of the secret with name `webapp-secret` will be changed

```bash
$ kubectl create ns check-kyverno
$ kubectl apply -f cr-crb.yaml
```

#### Apply `ClusterPolicy` and `Deployment`, which after that rule will be matched to the secret with name `webapp-secret` inside of the `check-kyverno` namespace for all keys in case of UPDATE (it means when key will be updated, deleted or new added) event will be happened. Mutation happens only for `Deployment` with name `webapp` inside of `check-kyverno` namespace. 

```bash
$ kubectl apply -f autorestart-deployment-policy.yaml
$ kubectl apply -f secret.yaml
$ kubectl apply -f deployment.yaml
```

#### So what does it means. In case of when some key of secret `webapp-secret` will be added,updated or deleted our `ClusterPolicy` with name `restart-deployment-on-secret-change` going to add label key `deployment-version` with value `request.object.metadata.resourceVersion` from our object and due that deployment starting to think something changed and I must be restarted. Like as the following. 

```bash
$ kubectl get deployment -n check-kyverno webapp -o json | jq -r '.spec.template.metadata.annotations'
{
  "deployment-version": "691392"
}
```

#### You can see the simulation as following

![Simulation](https://github.com/jamalshahverdiev/kyverno/blob/main/Restart-Deployment-On-Secret-Changes/tmux-session-optimized.gif)