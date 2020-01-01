kubectl delete -f dsp_gke.yaml
docker build -f Dockerfile -t eu.gcr.io/experimental-258714/polls . && \
docker push eu.gcr.io/experimental-258714/polls && \
kubectl create -f dsp_gke.yaml
