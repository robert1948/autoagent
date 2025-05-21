FROM mcr.microsoft.com/devcontainers/python:3.10

RUN apt-get update && apt-get install -y \
    nodejs npm curl git build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /workspaces/autoagent
COPY requirements.txt /workspaces/autoagent/requirements.txt
RUN pip install -r requirements.txt
COPY . /workspaces/autoagent
RUN pip install -e .
RUN pip install -e .[dev]
RUN pip install -e .[all]