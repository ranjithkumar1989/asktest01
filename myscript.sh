apt-get update && \
apt-get install -y python3 python3-pip && \
pip3 install requests && \
python3 /scripts/api.py >> /tmp/out.txt &&
sleep 3600
