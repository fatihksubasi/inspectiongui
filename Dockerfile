FROM thewtex/opengl

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    python-pip \
    mesa-common-dev \
    software-properties-common \
    python-setuptools \
    python-pygame \
    python-opengl \
    python-enchant \
    python-dev \
    build-essential \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    zlib1g-dev \
  && rm -rf /var/lib/apt/lists/*

RUN  pip install --upgrade --no-cache-dir pillow \
  && pip install --upgrade --no-cache-dir h5py \
  && pip install --upgrade --no-cache-dir --ignore-installed numpy==1.13.3 \
  && pip install --upgrade --no-cache-dir tensorflow \
  && pip install --upgrade --no-cache-dir keras \
  && pip install --upgrade --no-cache-dir docutils \
  && pip install --upgrade --no-cache-dir Cython==0.28

RUN cd && git clone git://github.com/kivy/kivy.git && cd kivy && make && make install

COPY at_runtime.sh /tmp/
RUN chmod +x  /tmp/*.sh

ENTRYPOINT ["/tmp/at_runtime.sh"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

