#!/usr/bin/env bash

kyverno apply clusterpolicy.yaml --resource=cronjob.yaml --resource=job.yaml