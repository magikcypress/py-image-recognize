FROM python:3.9-slim-buster

RUN echo "Europe/London" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

COPY requirements.txt app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8585", "--reload"]
