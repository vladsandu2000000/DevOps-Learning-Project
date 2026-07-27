# 1. Plecăm de la o imagine oficială și ușoară de Python
FROM python:3.12-slim

# 2. Setări recomandate pentru Python în containere (evită buffering-ul și fișierele .pyc)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Setăm directorul de lucru în interiorul containerului
WORKDIR /app

# 4. Copiem fișierul de dependențe și le instalăm
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiem tot codul sursă al proiectului în container
COPY . /app/

# 6. Documentăm portul pe care va asculta aplicația
EXPOSE 8000

# 7. Comanda implicită care pornește serverul Django când se lansează containerul
CMD ["python", "spa_salon/manage.py", "runserver", "0.0.0.0:8000"]
