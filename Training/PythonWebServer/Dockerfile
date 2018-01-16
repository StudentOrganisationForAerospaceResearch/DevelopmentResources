FROM python:3.6.3

# include the psutil package here
RUN \
 pip install --no-cache-dir -U \
	pip && \
 pip install --no-cache-dir -U \
	psutil

RUN pip install pytz

WORKDIR /python_webserver_training