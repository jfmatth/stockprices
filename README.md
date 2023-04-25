# Postgres

I'm using the zalando postgres operator for all postgres stuff, it's amazing!

## Creating the database in K8s
The .yaml file was built from the UI fo Zalando interface, another amazing item.    

1. The namespace was removed, so we can put this anywhere in the K8s environment
2. There is a LoadBalancer specified, so we can connect outside of our pods
3. There is only one replica for now
4. There is a database called stockprices and a user develop in the home cluster

```bash
kubectl create -f postgres-cluster.yaml
```

## Database details from YAML
- Database = stockprices
- User = develop
- Password = obtained from the kubernetes secret created by Zalando  

## Connecting via PSQL
To connect to the cluster, you should follow the Zalando docs (https://postgres-operator.readthedocs.io/en/latest/user/#connect-to-postgresql)

- Get the password
```bash
export PGPASSWORD=$(kubectl get secret develop.home.credentials.postgresql.acid.zalan.do -o 'jsonpath={.data.password}' | base64 -d)
```

- Setup SSL (required)
```bash
export PGSSLMODE=require
```
- You have to find the port the LB service has been given
```bash
kubectl get svc
...
home          LoadBalancer   10.43.70.224   192.168.100.70,192.168.100.71,192.168.100.72   5432:32538/TCP
```

The LB has assigned 30400/TCP to the external port, which then routes traffic to the 5432 ports of the pods, now just connect to the cluster with the following

```bash
psql stockprices -U develop -h 192.168.100.70 -p 32538
```

## Setup DATABASE_URL

```bash
export DATABASE_URL=postgres://develop:$PGPASSWORD@192.168.100.70:32538/stockprices
```

