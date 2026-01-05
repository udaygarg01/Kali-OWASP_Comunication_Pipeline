FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y zaproxy python3 && \
    apt clean

RUN ln -s /usr/share/zaproxy/zap.sh /usr/local/bin/zap.sh

WORKDIR /app

COPY runner.py /app/runner.py

ENTRYPOINT ["python3", "/app/runner.py"]
