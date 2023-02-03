FROM ubuntu

WORKDIR /

RUN apt update && apt install python3 -y

COPY Scriptpython.py .

CMD python3 Scriptpython.py

#EXPOSE 5000