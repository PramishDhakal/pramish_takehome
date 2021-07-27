FROM python:3.7
ENV PYTHONUNDUFFERED 1
WORKDIR /app
COPY requirments.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD python main.py