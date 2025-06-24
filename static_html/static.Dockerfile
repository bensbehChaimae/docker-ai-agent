# Declare what image to use 
# From image_name:latest
FROM python:3.13.4-slim-bullseye

WORKDIR /app

# Copy Home.html to the container 
# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder 
COPY ./src /app

# RUN echo "Hello, Docker!" > index.html


# docker build -f Dockerfile -t pyapp . 
# docker run -it pyapp 

# docker push pyapp => unthorization failed 

# docker build -f Dockerfile -t amanar123/ai-py-app:latest .
# docker push amanar123/ai-py-app:latest


# add another tag
# docker build -f Dockerfile -t amanar123/ai-py-app:v1 .
# docker push amanar123/ai-py-app:v1


# Run python web server
# python -m http.server 8000
# to run the server in docker container image 
CMD ["python", "-m", "http.server", "8000"]



# Start everything
# docker-compose up

# Stop everything (Ctrl+C first, then:)
# docker-compose down












