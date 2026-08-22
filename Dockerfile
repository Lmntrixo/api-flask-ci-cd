FROM python:3.12-alpine 
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY .. .
RUN addgroup -S pygroup && adduser -S pyuser -G pygroup

RUN chown -R pyuser:pygroup /app

USER pyuser

EXPOSE 5000 

CMD ["python", "app.py"]
