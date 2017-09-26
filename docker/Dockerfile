FROM python:2.7.14

COPY ./newspaper-demo /demo

RUN pip install --no-cache-dir -r demo/requirements.txt

EXPOSE 5000

CMD ["python", "/demo/runserver.py"]
