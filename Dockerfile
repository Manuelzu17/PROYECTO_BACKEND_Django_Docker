FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /my_app_django_dir
WORKDIR /my_app_django_dir
ADD requirements.txt /my_app_django_dir/
#RUN pip install -- upgrade pip && pip install -r requirements.txt
RUN pip install -r requirements.txt
ADD . /my_app_django_dir/