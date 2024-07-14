# наша апишка

## и как ее затестить

1. **установить необходимые библиотеки из файла `requirements.txt`**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```


2. **Запустить приложение**
    ```bash
    uvicorn main:app --reload
    ```

Документация доступна по ссылке [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

