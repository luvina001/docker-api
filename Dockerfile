FROM python:3-alpine

RUN adduser --disabled-password user
WORKDIR /home/user

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app app
COPY myapp.py config.py boot.sh .env ./

ENV FLASK_APP myapp.py

RUN chown -R user:user ./ && chmod +x boot.sh
USER user

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
