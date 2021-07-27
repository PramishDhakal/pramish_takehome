<<<<<<< HEAD
#maintainer : Pramish Dhakal
=======
>>>>>>> 138d947244b3665cb455cdf636288c37da00d201
FROM python:3.7
ENV PYTHONUNDUFFERED 1
WORKDIR /app
COPY requirments.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD python main.py