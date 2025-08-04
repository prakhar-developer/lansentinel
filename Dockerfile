# 🔧 Base Image: Use lightweight official Python image
FROM python:3.11-slim

# 🏷️ Metadata
LABEL maintainer="Prakhar Srivastava"
LABEL description="LANSentinel++: Encrypted LAN Peer System with Proctoring and AI Monitoring"

# 🗂️ Set working directory inside container
WORKDIR /app

# 🚚 Copy project files
COPY . /app

# 🔐 Optional: Avoid running as root (good practice)
RUN adduser --disabled-password --gecos '' lansentinel
USER lansentinel

# 🐍 Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🧪 Expose ports if you're doing peer-to-peer across LAN
EXPOSE 5000-5100/tcp

# ✅ Run the CLI entrypoint (you can also change to server.py if needed)
CMD ["python", "__main__.py"]
