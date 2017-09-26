FROM python:2.7.14

COPY ./newspaper-demo .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "./runserver.py"]
