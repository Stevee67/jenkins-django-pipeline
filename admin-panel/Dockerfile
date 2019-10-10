FROM python:3.6

ADD ./ /src
WORKDIR /src

RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

EXPOSE 8900

ENTRYPOINT ["python", "src/admin_panel/manage.py"]
CMD ["runserver", "0.0.0.0:8900"]