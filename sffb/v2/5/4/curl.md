```bash
curl -s -X 'GET' \
  'http://127.0.0.1:8000/user?people=user01&people=user02&people=user03' \
  -H 'accept: application/json' | jq

```