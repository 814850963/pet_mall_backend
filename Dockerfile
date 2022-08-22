FROM python
EXPOSE 8000
COPY . /code
WORKDIR /code/django_pet_mall
RUN pip install -r requirements.txt
