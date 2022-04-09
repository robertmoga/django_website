FROM ubuntu:20.04
ENV TZ=Europe/Bucharest
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y nano python3.8-venv virtualenv
RUN apt-get install -y apache2
RUN apt-get -y install libapache2-mod-wsgi-py3 

RUN ln /usr/bin/python3 /usr/bin/python 
RUN apt-get -y install python3-pip 

ADD ./www/django_website/requirements.txt /var/www/html 
ADD ./site-config.conf /etc/apache2/sites-available/000-default.conf
ADD ./www/ /var/www/html 

WORKDIR /var/www/html

RUN python -m venv /var/venv
ENV VIRTUAL_ENV /var/venv
ENV PATH /var/venv/bin:$PATH 
RUN which python 

RUN pip install -r requirements.txt 

#RUN python django_website/manage.py collectstatic -y

RUN chown :www-data django_website/db.sqlite3
RUN chmod 664 django_website/db.sqlite3

RUN chown :www-data django_website/
RUN chmod 775 django_website/

RUN chown -R :www-data django_website/media/
RUN chmod -R 775 django_website/media

EXPOSE 80 3500 

CMD ["apache2ctl", "-D", "FOREGROUND"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
