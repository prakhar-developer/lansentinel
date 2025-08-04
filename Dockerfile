# 🔧 Base Image
FROM python:3.11-slim

# 🏷️ Metadata
LABEL maintainer="Prakhar Srivastava"
LABEL description="LANSentinel++: Encrypted LAN Peer System with Proctoring and AI Monitoring"

# 🛠️ Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    net-tools \
    lsof \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# 🗂️ Set working directory
WORKDIR /app

# 🚚 Copy files
COPY . /app

# 🔐 Create user + set permissions before switching user
RUN adduser --disabled-password --gecos '' lansentinel \
    && mkdir -p /app/logs \
    && chown -R lansentinel:lansentinel /app

# 👤 Switch to non-root
USER lansentinel

# 🐍 Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🧪 Expose LAN ports
EXPOSE 5000-5100/tcp

# ✅ Run app
CMD ["python", "__main__.py"]
