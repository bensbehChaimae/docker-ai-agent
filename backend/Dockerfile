# Switch from Alpine to Debian which handles this better
FROM python:3.13.4-slim-bullseye

# host.docker.internal is used to access the host machine from the container 
# instead of using the default gateway localhost 


# curl -X POST -d '{"message": "Hello, world!"}' -H "Content-Type: application/json" http://host.docker.internal:8000/api/chat/
RUN apt-get update && apt-get install -y curl


# Create a python virtual environment (isolate python from the system)
RUN python3 -m venv /opt/venv
   # add the VE into the PATH
ENV PATH="/opt/venv/bin:$PATH"


WORKDIR /app

# Get the requirements :
    # COPY local_file to container_destination
COPY requirements.txt /tmp/requirements.txt
# Install the requirements:
    # RUN whithin_container_while_building
RUN pip install -r /tmp/requirements.txt


COPY ./src /app


CMD ["python", "-m", "http.server", "8000"]















