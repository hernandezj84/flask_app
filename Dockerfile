FROM python:3.9
EXPOSE 8080
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["/app/app-service", "start"]