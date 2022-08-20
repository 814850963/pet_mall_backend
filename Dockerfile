FROM python
EXPOSE 8000
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt