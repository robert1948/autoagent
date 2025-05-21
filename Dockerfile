# Base Python image with devcontainers support
FROM mcr.microsoft.com/devcontainers/python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    gnupg \
    ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Node.js 20 from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    # rm -f /etc/apt/sources.list.d/nodesource.list
    rm -f /etc/apt/sources.list.d/nodesource.list

# Upgrade pip
RUN pip install --upgrade pip

# Set working directory
WORKDIR /workspaces/autoagent

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .requirements.txt
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; else echo "requirements.txt not found, skipping pip install"; fi

# Copy the rest of the application
COPY . .

# Optional: Set default shell to bash for convenience
# SHELL ["/bin/bash", "-c"]
