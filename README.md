# kiwi

https://kiwitcms.readthedocs.io/en/latest/installing_docker.html

## deploy on docker compose
- docker compose up -d (or docker compose -f docker-compose-redmine.yml up -d)
- browser: https://localhost/
- docker exec -it kiwi_web /Kiwi/manage.py migrate
- docker exec -it kiwi_web /Kiwi/manage.py createsuperuser ==> username, email, password
- docker exec -it kiwi_web /Kiwi/manage.py refresh_permissions
- docker exec -it kiwi_web /Kiwi/manage.py set_domain <your_domain: e.g. public.tenant.kiwitcms.org>
- docker compose down

## deploy on k8s
- kubectl apply -f deployment.yml
- kubectl exec -it <kiwi-web-pod> -- /Kiwi/manage.py migrate
- kubectl exec -it <kiwi-web-pod> -- /Kiwi/manage.py createsuperuser
- kubectl exec -it <kiwi-web-pod> -- /Kiwi/manage.py refresh_permissions
- /Kiwi/manage.py set_domain public.tenant.kiwitcms.org
- browser: public.tenant.kiwitcms.org

## API
https://kiwitcms.readthedocs.io/en/latest/modules/tcms.rpc.api.testcase.html#tcms.rpc.api.testcase.TestCase.comments
