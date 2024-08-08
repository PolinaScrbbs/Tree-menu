1. Клонируйте репозиторий с GitHub


2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv
   ```
   ```bash
    source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv
   ```
   ```bash
    venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pi
```
```bash
pip install -r requirements.txt
```

4. Выполните миграции, загрузку данных, создание суперюзера и запустите приложение:
```bash
python manage.py makemigrations
```
```bash
manage.py migrate
```
```bash
python manage.py loaddata fixtures/db.json
```
```bash
python manage.py create_superuser
```
```bash
python manage.py runserver
```

Сервер запустится локально по адресу `http://127.0.0.1:8000/`

5. Остановить приложение можно комбинацией клавиш Ctl-C.
<h1></h1>
