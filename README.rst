*************************************************************************************************
In this repository I will store Policy and ClusterPolicy rules of Kyverno for different scenarios
*************************************************************************************************

* `Restart deployment pods when secret keys chaned,added or deleted <https://github.com/jamalshahverdiev/kyverno/tree/main/Restart-Deployment-On-Secret-Changes>`_
* `Image registry ClusterPolicy rules <https://github.com/jamalshahverdiev/kyverno/tree/main/Image-Registry-Policies>`_
* `Synchronize secret imagepullsecrets to all namespaces <https://github.com/jamalshahverdiev/kyverno/tree/main/Sync-Secret-To-All-Namespaces>`_

Before starting to test something we must install Kyverno to our Kubernetes cluster with Helm.

.. code-block:: bash

   $ helm repo add kyverno https://kyverno.github.io/kyverno/
   $ helm repo update
   $ helm install kyverno kyverno/kyverno -n kyverno --create-namespace --version 2.6.5 --set replicaCount=1
   $ kubectl create ns check-kyverno

To uninstall we can use the following command

.. code-block:: bash

   $ helm uninstall kyverno -n kyverno
