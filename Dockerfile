FROM python:3.12

RUN mkdir PYTHON

COPY ./ PYTHON/

WORKDIR /PYTHON

RUN pip3 install -r requirements.txt

EXPOSE 5000 5001

ENTRYPOINT [ "python3", "flask_app.py"]