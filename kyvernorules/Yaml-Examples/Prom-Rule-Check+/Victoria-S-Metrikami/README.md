# Install VictoriMetrics Itself

```bash
$ helm repo add vm https://victoriametrics.github.io/helm-charts/
$ helm repo update
$ helm search repo vm/
$ helm show values vm/victoria-metrics-cluster > vm-values.yaml
$ helm install victoria-metrics vm/victoria-metrics-cluster -f vm-values.yaml -n vicmet --debug --dry-run
$ helm install victoria-metrics vm/victoria-metrics-cluster -f vm-values.yaml -n vicmet --create-namespace
```

```bash
$ kubectl taint nodes db1 db=pgsql:NoSchedule-
$ kubectl taint nodes db2 db=pgsql:NoSchedule-
$ kubectl get nodes -o json | jq -r '.items[] | select(.spec.taints) | .metadata.name'
```

# Install VictoriaMetrics Operator

```bash
$ helm repo add vm https://victoriametrics.github.io/helm-charts/
$ helm repo update
$ helm search repo vm/victoria-metrics-operator -l
$ helm show values vm/victoria-metrics-operator > vm-operator-values.yaml
$ helm install vmoperator vm/victoria-metrics-operator -f vm-operator-values.yaml -n vicmet --debug --dry-run
$ helm install vmoperator vm/victoria-metrics-operator -f vm-operator-values.yaml -n vicmet
```