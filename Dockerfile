# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY . .

# install dependencies
RUN pip install -e .

# command to run on container start
CMD [ "python", "./app.py" ]