ARG IDF_VERSION=latest

FROM alpine as download_qemu

# QEMU
ARG QEMU_REL=esp-develop-20220203
ARG QEMU_SHA256=c83e483e3290f48a563c2a376b7413cd94a8692d8c7308b119f4268ca6d164b6
ENV QEMU_DIST=qemu-${QEMU_REL}.tar.bz2
ENV QEMU_URL=https://github.com/espressif/qemu/releases/download/${QEMU_REL}/${QEMU_DIST}

RUN wget --no-verbose ${QEMU_URL} \
  && echo "${QEMU_SHA256}  ${QEMU_DIST}" | sha256sum -c - \
  && tar -xf $QEMU_DIST -C /opt \
  && rm ${QEMU_DIST}

FROM espressif/idf:$IDF_VERSION

ENV DEBIAN_FRONTEND=nointeractive

RUN apt-get update \
  && apt install -y -q \
  cmake \
  git \
  hwdata \
  linux-tools-virtual \
  && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip | tail -n1` 20

# pre-commit
RUN python -m pip install pre-commit

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY --from=download_qemu /opt/qemu /opt/qemu

ENV PATH=/opt/qemu/bin:${PATH}

RUN echo "source /opt/esp/idf/export.sh > /dev/null 2>&1" >> ~/.bashrc

ENTRYPOINT [ "/opt/esp/entrypoint.sh" ]

CMD ["/bin/bash"]
