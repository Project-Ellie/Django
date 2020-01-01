# Deploying gke-cep

```
docker run -d --rm -p 8000:8000 \
    -e DATABASE_HOST \
    -e DATABASE_USER \
    -e DATABASE_PASSWORD \
     eu.gcr.io/cep-gke/mydjango
```

```
docker build --build-arg pipenv_dev=1 -t eu.gcr.io/cep-gke/mydjango .
```