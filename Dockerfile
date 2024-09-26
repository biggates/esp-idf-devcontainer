ARG IDF_VERSION=latest

FROM alpine as download_qemu

ARG QEMU_SHA256

RUN --mount=type=bind,source=qemu.tar.gz,target=/qemu.tar.gz \
  echo "${QEMU_SHA256}  /qemu.tar.gz" | sha256sum -c - \
  && tar -xf /qemu.tar.gz -C /opt

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
RUN /opt/esp/entrypoint.sh python -m pip install pre-commit

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY --from=download_qemu /opt/qemu /opt/qemu

ENV PATH=/opt/qemu/bin:${PATH}

RUN echo "source /opt/esp/idf/export.sh > /dev/null 2>&1" >> ~/.bashrc

ENTRYPOINT [ "/opt/esp/entrypoint.sh" ]

CMD ["/bin/bash"]
