# Shell commands

---
### Build the docker file
```
docker build -t gcr.io/gke-cep/mydjango -f Dockerfile .
```


### DB Connection String
```
INSTANCE=django-master-instance
CONNECTION=`gcloud sql instances describe $INSTANCE | grep conn | awk '{print $2}'`
echo $CONNECTION
```
---
### Start sql proxy (dev only)
This assumes the instance is already available <br/>
Make sure cloud_sql_proxy is on $PATH or prefix with ./
```
# do this if you have postgres server running locally
sudo pkill -u postgres

cloud_sql_proxy -instances=$CONNECTION=tcp:5432 > sql_proxy.log 2>&1 &
```



---
### Access to the SQL instance
[Use Console](https://cloud.google.com/python/django/kubernetes-engine#creating_a_service_account)
to create a service account, if it doesn't exist yet.<br/>
The proxy requires a service account with Editor privileges<br/>
Create a private key, download it as json file and rename it to sql-editor.json. We'll need it later.

For local access, export credentials. Note that these environment variables are 
referred from within ```bookstore_project.settings.py```
```
export DATABASE_USER=<your-database-user>
export DATABASE_PASSWORD=<your-database-password>
```


From within ```pipenv shell```
```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
```

---
### Use a bucket for static content
Note that the bucket has to be public to be accessible via https. The http
URL is referred to from within setting.py:
```
    # settings.py:
    STATIC_URL = 'https://storage.googleapis.com/dsp-258714/static/'
```

```
gsutil mb gs://dsp-258714
gsutil iam ch allUsers:objectViewer gs://dsp-258714
gsutil -m rsync -R static/ gs://dsp-258714/static
```

---
### Start-up a cluster
```
gcloud container clusters create dev-cluster   \
    --scopes "cloud-platform"   --num-nodes 2 \
    --zone "europe-west6-a" \
    --network adtrac-brok-vpc --subnetwork subnet-adtrac-brok-eu-west6-private
```

Getting the credentials so that kubectl is on the right cluster
```
gcloud container clusters get-credentials dev-cluster --zone "europe-west6-a"

# check the active context (*) is gke_<project>_<zone>_dsp
kubectl config get-contexts
```

Now use kubectl to deploy the secrets used within the cluster. The json file is the one we downloaded after creating
the sql editor service account (remember?)<br/>
You can see those secrets afterwards in th k8s console
```
kubectl create secret generic cloudsql-oauth-credentials --from-file=.secrets/sql-editor.json
```

K8s will provide these in the environment of the pods.
```
kubectl create secret generic cloudsql --from-literal=username=$DATABASE_USER --from-literal=password=$DATABASE_PASSWORD
```

Tell docker to use gcloud as credential helper
```
gcloud auth configure-docker
```

Push docker image
```
docker push eu.gcr.io/experimental-258714/dsp
```

