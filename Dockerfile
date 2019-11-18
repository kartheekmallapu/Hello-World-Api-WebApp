FROM python:2.7
MAINTAINER Kartheek Reddy Mallapu "kloudviva@gmail.com"
COPY . /webapp
WORKDIR /webapp
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["webapp.py"]
