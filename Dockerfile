FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install requests

# COPY files
COPY DonationLib.py
COPY __init__.py	
COPY donation.py	
COPY setup.py	
COPY variables.py

CMD ["python", "donation.py"]
