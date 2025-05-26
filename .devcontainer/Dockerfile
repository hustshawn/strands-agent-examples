FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set up a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set up Python environment
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install pip and upgrade it
RUN pip install --upgrade pip

# Create workspace directory with correct permissions
WORKDIR /workspace
RUN chown -R $USERNAME:$USERNAME /workspace

# Switch to non-root user
USER $USERNAME

# Install Python packages from requirements.txt at container build time
# This will be overridden by postCreateCommand if requirements.txt changes
COPY --chown=$USERNAME:$USERNAME requirements.txt /tmp/
RUN pip install --user -r /tmp/requirements.txt

# Add .local/bin to PATH
ENV PATH="/home/$USERNAME/.local/bin:${PATH}"