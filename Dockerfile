FROM python:3.11

# Set the working directory in the container.
WORKDIR /opt/project

# To prevent writing .pyc files on disk.
ENV PYTHONDONTWRITEBYTECODE 1
# To disable python's input & output buffering.
ENV PYTHONUNBUFFERED 1
# To add current directory to python's path --> When importing my own modules, it makes it easier for Python to find those.
ENV PYTHONPATH .
# In order to enable env-prefix from core/project/settings/__init__.py so that a if statement from docker.py to be true.
ENV CORE_SETTINGS_IN_DOCKER true

# Install system dependencies(?)
RUN set -xe \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install virtualenvwrapper poetry==2.1.2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install --no-root

# Copy project files
COPY ["README.rst", "Makefile", "./"]
# Copying where our actual sourcecode is
COPY core core
COPY local local

# Expose port 8080
EXPOSE 8080

# Set up the entrypoint
# As soon as a container starts up, the following script will be run
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
