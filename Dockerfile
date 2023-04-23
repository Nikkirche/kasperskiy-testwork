FROM ubuntu:18.04

LABEL maintainer="Sven-Hendrik Haase <svenstaro@gmail.com>"
ARG PTS_VERSION=8.0.1
RUN apt-get update && \
    apt-get -y install --no-install-recommends curl php-cli php-gd php-xml php-zip php-posix && \
    curl -LO http://phoronix-test-suite.com/releases/repo/pts.debian/files/phoronix-test-suite_${PTS_VERSION}_all.deb && \
    dpkg -i phoronix-test-suite_${PTS_VERSION}_all.deb && \
    rm phoronix-test-suite_${PTS_VERSION}_all.deb && \
    rm -rf /var/lib/apt/lists/* && \
    mv /var/lib/phoronix-test-suite /.phoronix-test-suite

RUN chgrp -R 0 /.phoronix-test-suite && \
    chmod -R g=u /.phoronix-test-suite

ADD user-config.xml ~/.phoronix-test-suite/user-config.xml
