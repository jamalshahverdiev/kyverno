kubectl get deployment deployment-1 -o jsonpath='{.metadata.uid}' -n check-kyverno
kubectl get deployment deployment-1 -o jsonpath='{.metadata.uid}' -n check-kyverno
kubectl get deployment deployment-2 -o jsonpath='{.metadata.uid}' -n check-kyverno

kubectl get daemonset daemonset-1 -o jsonpath='{.metadata.uid}'  -n check-kyverno
kubectl get daemonset daemonset-2 -o jsonpath='{.metadata.uid}'  -n check-kyverno

kubectl get statefulset statefulset-1 -o jsonpath='{.metadata.uid}' -n check-kyverno
kubectl get replicaset -n check-kyverno -l app=drepset-wout-annot -o jsonpath='{range .items[*]}{.metadata.uid}{"\n"}{end}'

kubectl patch statefulset sset-wout-annot -n check-kyverno -p "{\"spec\":{\"template\":{\"metadata\":{\"annotations\":{\"date\":\"`date +'%s'`\"}}}}}"
kubectl rollout restart deployment dment-wout-annot -n check-kyverno
kubectl rollout restart deployment drepset-wout-annot -n check-kyverno
kubectl rollout restart daemonset dset-without-annot -n check-kyverno
