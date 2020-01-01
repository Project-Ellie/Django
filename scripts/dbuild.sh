#!/bin/bash

docker build --build-arg pipenv_dev=1 -t eu.gcr.io/cep-gke/mydjango .