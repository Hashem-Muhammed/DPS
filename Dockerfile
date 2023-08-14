FROM python:3

ENV PYTHONUNBUFFERED 1


WORKDIR /dps-app

COPY requirements.txt .
# COPY Pipfile* .

# Install project dependencies
RUN pip install -r requirements.txt

# Install poppler-utils
RUN apt-get update && apt-get install -y poppler-utils

# Copy the Django project to the container
COPY . .

EXPOSE 8000

# Make migrations
RUN python manage.py makemigrations

# Run migrations
RUN python manage.py migrate

# Run the Django development server
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]