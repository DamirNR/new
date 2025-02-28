FROM python
RUN mkdir /app
COPY ./main.py /app
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]