```
FastAPI для начинающих

https://stepik.org/course/180000/info
```

```bash
python3 -m venv sffb
cd sffb/
source bin/activate
# source ~/git/github/ilyabobrusev/stepik_fastapi_for_beginners/sffb/bin/activate
pip3 install fastapi uvicorn
pip3 freeze > requirements.txt
# pip3 install -r requirements.txt
deactivate
```

```bash
uvicorn main:app --port 8000 --reload
```
