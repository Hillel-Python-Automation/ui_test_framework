FROM python:3.11-bookworm

RUN python --version
RUN pip --version
COPY requirements.txt .
RUN ls
RUN pip install -r requirements.txt

RUN apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

CMD ["python"]
