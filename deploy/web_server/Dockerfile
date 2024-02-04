FROM python:3.9.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG INSTALL_DIR=/workspaces
WORKDIR $INSTALL_DIR

COPY web_server/requirements.txt .

### Install dependencies
RUN \
 apt update && \
 apt install netcat lsof libpq-dev python3-dev gcc -y && \
 pip install --upgrade pip && \
 pip install -r requirements.txt


ARG INSTALL_DIR=/workspaces

### Pull code
COPY . /workspaces/.

WORKDIR $INSTALL_DIR

ENV WORKDIR=$INSTALL_DIR
ENV PYTHONPATH=$INSTALL_DIR:$INSTALL_DIR/web_server


## Port expose
EXPOSE 8000

## Run entrypoint.sh
ENTRYPOINT ["deploy/web_server/entrypoint.sh"]
