FROM python:3.6

ADD ./ /admin_panel
WORKDIR /admin_panel

RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

EXPOSE 8900

CMD ["django-admin", "runserver", "0.0.0.0:8900"]