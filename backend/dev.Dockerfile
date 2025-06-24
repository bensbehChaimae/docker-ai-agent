# Switch from Alpine to Debian which handles this better
FROM python:3.13.4-slim-bullseye


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















