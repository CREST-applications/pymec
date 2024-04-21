# =============================================================

# written by Hajime Sasaki


# =============================================================

FROM python:3.10.14


# locale
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
ENV LANG en_US.UTF-8

# =============================================================

# python mec client generated

# You must `git clone` the repository brefore building the image.
# Check the README.md.


ENV PYTHON_CLIENT_DIR /usr/lib/python-client-generated

COPY ./python-client-generated ${PYTHON_CLIENT_DIR}

RUN pip3 install \
    setuptools \
    requests

# install
WORKDIR ${PYTHON_CLIENT_DIR}
RUN pip3 install .

# =============================================================

# add user


RUN apt-get install -y curl

RUN addgroup --gid 1000 docker && \
    adduser --uid 1000 --ingroup docker --home /home/docker --shell /bin/sh --disabled-password --gecos "" docker

RUN USER=docker && \
    GROUP=docker && \
    curl -SsL https://github.com/boxboat/fixuid/releases/download/v0.6.0/fixuid-0.6.0-linux-amd64.tar.gz | tar -C /usr/local/bin -xzf - && \
    chown root:root /usr/local/bin/fixuid && \
    chmod 4755 /usr/local/bin/fixuid && \
    mkdir -p /etc/fixuid && \
    printf "user: $USER\ngroup: $GROUP\n" > /etc/fixuid/config.yml

USER docker:docker
ENTRYPOINT ["fixuid"]
