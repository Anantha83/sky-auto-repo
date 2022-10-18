FROM python:latest

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py /app/

# Install packages from requirements.txt
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

ENV PYTHONPATH=/app

# Define our command to be run when launching the container
EXPOSE 8080
CMD [ "python" , "./app.py" ]
