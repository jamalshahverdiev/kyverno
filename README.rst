*************************************************************************************************
In this repository I will store Policy and ClusterPolicy rules of Kyverno for different scenarios
*************************************************************************************************

* `Restart deployment pods when secret keys chaned,added or deleted  <https://github.com/jamalshahverdiev/python-general-codes/tree/master/HaProxyRestAPI>`_

Before starting to test something we must install Kyverno to our Kubernetes cluster with Helm.

.. code-block:: bash

   $ helm repo add kyverno https://kyverno.github.io/kyverno/
   $ helm repo update
   $ helm install kyverno kyverno/kyverno -n kyverno --create-namespace --version 2.6.5 --set replicaCount=1

To uninstall we can use the following command

.. code-block:: bash

   $ helm uninstall kyverno -n kyverno
