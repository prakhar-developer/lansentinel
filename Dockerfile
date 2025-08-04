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

# 🚚 Copy project files
COPY . .

# 🔐 Create non-root user & set permissions
RUN adduser --disabled-password --gecos '' lansentinel \
    && mkdir -p /app/logs \
    && chown -R lansentinel:lansentinel /app

# 🐍 Install Python dependencies before switching user
RUN pip install --no-cache-dir --default-timeout=300 -r requirements.txt

# 👤 Switch to non-root user
USER lansentinel

# 🧪 Expose LAN ports for peer-to-peer + APIs
EXPOSE 5000-5100/tcp

# ✅ Run the app by default (can override via docker run)
CMD ["python", "-m", "core.server", "--host", "0.0.0.0", "--port", "5001"]
