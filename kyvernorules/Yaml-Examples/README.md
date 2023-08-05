#### Get UUID of `Deployment`, `Statefulset`, `Daemonset` and `ReplicaSet` UUIDs for `secret` `ownerreference` key

```bash
$ kubectl get deployment deployment-1 -o jsonpath='{.metadata.uid}' -n check-kyverno
$ kubectl get daemonset daemonset-1 -o jsonpath='{.metadata.uid}'  -n check-kyverno
$ kubectl get statefulset statefulset-1 -o jsonpath='{.metadata.uid}' -n check-kyverno
$ kubectl get replicaset -n check-kyverno -l app=drepset-wout-annot -o jsonpath='{range .items[*]}{.metadata.uid}{"\n"}{end}'
$ kubectl patch statefulset sset-wout-annot -n check-kyverno -p "{\"spec\":{\"template\":{\"metadata\":{\"annotations\":{\"date\":\"`date +'%s'`\"}}}}}"
$ kubectl rollout restart deployment dment-wout-annot -n check-kyverno
$ kubectl rollout restart deployment drepset-wout-annot -n check-kyverno
$ kubectl rollout restart daemonset dset-without-annot -n check-kyverno
```

#### As user try to apply pod

```bash
$ kubectl --as=system:serviceaccount:default:test-user apply -f pod.yaml
```

#### Fetch the list of Pods in a Namespace and then pipes the output to kyverno jp which counts the number of Pods

```bash
$ kubectl get --raw /api/v1/namespaces/kyverno/pods | kyverno jp query "items | length(@)"
```

#### Get namespaces with annotation key `opso.info/max-replicas`

```bash
$ kubectl get namespaces -o json | jq -r '.items[] | select(.metadata.annotations["opso.info/max-replicas"]!=null) | .metadata.name'
$ kubectl get --raw /api/v1/namespaces/devops-dev?fieldSelector=metadata.annotations='opso.info/max-replicas' | jq
```

#### Get namespaces with annotation `opso.info/allowed-public-hosts`

```bash
$ kubectl get ns -o json | jq -r '.items[] | select(.metadata.annotations."opso.info/allowed-public-hosts"!=null) | .metadata.name'
```

#### Create NS and annotate it 

```bash
$ kubectl create namespace test
$ kubectl annotate ns test opso.info/allowed-public-hosts='test.com'

```
