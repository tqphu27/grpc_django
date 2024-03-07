# Pull base image
FROM python:3.8

# Set environmental variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

EXPOSE 50052

# Copy project
COPY .env /code/
COPY . /code/
