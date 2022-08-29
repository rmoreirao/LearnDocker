FROM python:3.9-rc-buster

WORKDIR /app_code

#Copy requirements file from current directory to file in 
#containers code directory we have just created.
COPY requirements.txt requirements.txt

#Run and install all required modules in container
RUN pip3 install -r requirements.txt

#Copy current directory files to containers code directory
COPY . .

CMD ["python", "app.py"]