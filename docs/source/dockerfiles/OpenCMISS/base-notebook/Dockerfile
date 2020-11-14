# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Modified from Jupyter Docker Stacks base-notebook (Ubuntu 20.04 focal).

# Ubuntu 16.04 (xenial) 
# https://hub.docker.com/_/ubuntu/?tab=tags&name=xenial
# OS/ARCH: linux/amd64
ARG ROOT_CONTAINER=ubuntu:xenial-20200903

ARG BASE_CONTAINER=$ROOT_CONTAINER
FROM $BASE_CONTAINER

LABEL maintainer="OpenCMISS-Iron <psam012@aucklanduni.ac.nz>"
ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    run-one \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

#----------------------------
# Install OpenCMISS dependencies.
RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
    libpthread-stubs0-dev \
    libmpich-dev \
    mpich \
    libmpich12 \
 && apt-get clean && rm -rf /var/lib/apt/lists/*


RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
    gcc \
    gfortran \
    g++ \
    libblas-dev \
    liblapack-dev \
    git \
    make \
    cmake \
    libssl-dev \
    libglew-dev \
    swig \
    sudo \
    cifs-utils \
    systemd \
    openssh-server \
 && apt-get clean && rm -rf /var/lib/apt/lists/*


# Install cmake.
ENV CMAKE_VERSION=3.7.2 \
    CMAKE_DIR=/cmake

RUN wget --quiet https://cmake.org/files/v3.7/cmake-${CMAKE_VERSION}-Linux-x86_64.sh && \
    mkdir $CMAKE_DIR && \
    /bin/bash cmake-${CMAKE_VERSION}-Linux-x86_64.sh --skip-license --prefix=$CMAKE_DIR && \
    rm cmake-${CMAKE_VERSION}-Linux-x86_64.sh
ENV PATH=$CMAKE_DIR/bin:$PATH

#----------------------------

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Configure environment
ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    NB_USER=$NB_USER \
    NB_UID=$NB_UID \
    NB_GID=$NB_GID \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$NB_USER

# Copy a script that we will use to correct permissions after running certain commands
COPY fix-permissions /usr/local/bin/fix-permissions
RUN chmod a+rx /usr/local/bin/fix-permissions

# Enable prompt color in the skeleton .bashrc before creating the default NB_USER
RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' /etc/skel/.bashrc

# Create NB_USER with name jovyan user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
RUN echo "auth requisite pam_deny.so" >> /etc/pam.d/su && \
    sed -i.bak -e 's/^%admin/#%admin/' /etc/sudoers && \
    sed -i.bak -e 's/^%sudo/#%sudo/' /etc/sudoers && \
    useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p $CONDA_DIR && \
    chown $NB_USER:$NB_GID $CONDA_DIR && \
    chmod g+w /etc/passwd && \
    fix-permissions $HOME && \
    fix-permissions $CONDA_DIR

USER $NB_UID
WORKDIR $HOME
ARG PYTHON_VERSION=default

# Setup work directory for backward-compatibility
RUN mkdir /home/$NB_USER/work && \
    fix-permissions /home/$NB_USER

# Install conda as jovyan and check the md5 sum provided on the download site
ENV MINICONDA_VERSION=4.8.3 \
    MINICONDA_MD5=d63adf39f2c220950a063e0529d4ff74 \
    CONDA_VERSION=4.8.3

WORKDIR /tmp
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-py38_${MINICONDA_VERSION}-Linux-x86_64.sh && \
    echo "${MINICONDA_MD5} *Miniconda3-py38_${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c - && \
    /bin/bash Miniconda3-py38_${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-py38_${MINICONDA_VERSION}-Linux-x86_64.sh && \
    echo "conda ${CONDA_VERSION}" >> $CONDA_DIR/conda-meta/pinned && \
    conda config --system --prepend channels conda-forge && \
    conda config --system --set auto_update_conda false && \
    conda config --system --set show_channel_urls true && \
    conda config --system --set channel_priority strict && \
    if [ ! $PYTHON_VERSION = 'default' ]; then conda install --yes python=$PYTHON_VERSION; fi && \
    conda list python | grep '^python ' | tr -s ' ' | cut -d '.' -f 1,2 | sed 's/$/.*/' >> $CONDA_DIR/conda-meta/pinned && \
    conda install --quiet --yes conda && \
    conda install --quiet --yes pip && \
    conda update --all --quiet --yes && \
    conda clean --all -f -y && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Install Tini
RUN conda install --quiet --yes 'tini=0.18.0' && \
    conda list tini | grep tini | tr -s ' ' | cut -d ' ' -f 1,2 >> $CONDA_DIR/conda-meta/pinned && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Install Jupyter Notebook, Lab, and Hub
# Generate a notebook server config
# Cleanup temporary files
# Correct permissions
# Do all this in a single RUN command to avoid duplicating all of the
# files across image layers when the permissions change
RUN conda install --quiet --yes \
    'numpy' \
    'virtualenv' \
    'notebook=6.1.3' \
    'jupyterhub=1.1.0' \
    'jupyterlab=2.2.5' && \
    conda clean --all -f -y && \
    npm cache clean --force && \
    jupyter notebook --generate-config && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

EXPOSE 8888

# Configure container startup
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

# Copy local files as late as possible to avoid cache busting
COPY start.sh start-notebook.sh start-singleuser.sh /usr/local/bin/
COPY jupyter_notebook_config.py /etc/jupyter/

# Fix permissions on /etc/jupyter as root
USER root
RUN fix-permissions /etc/jupyter/

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

WORKDIR $HOME

#----------------------------
# Install OpenCMISS

# Make RUN commands use the new miniconda environment:
SHELL ["conda", "run", "/bin/bash", "-o", "pipefail", "-c"]
RUN mkdir /home/$NB_USER/opencmiss-build
WORKDIR /home/$NB_USER/opencmiss-build
RUN mkdir opencmiss && \
    mkdir setup-build && \
    git clone https://github.com/OpenCMISS/setup.git && \
    cd setup-build && \
    cmake -DOPENCMISS_LIBRARIES=iron -DOPENCMISS_ROOT=../opencmiss ../setup && \
    cmake --build . && \
    rm -rf ../opencmiss/build

ENV PYTHONPATH=/home/jovyan/opencmiss-build/opencmiss/install/lib/python3.8/opencmiss.iron:$PYTHONPATH


WORKDIR $HOME

# Jupyter docker-stacks minimal-notebook

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    emacs-nox \
    vim-tiny \
    git \
    inkscape \
    jed \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    netcat \
    python-dev \
    # ---- nbconvert dependencies ----
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic \
    # ----
    tzdata \
    unzip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID


# Jupyter docker-stacks scipy-notebook

USER root

# ffmpeg for matplotlib anim & dvipng+cm-super for latex labels.
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg dvipng cm-super && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install ssh server.
RUN mkdir /var/run/sshd
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

USER $NB_UID

# Install Python 3 packages
RUN conda install --quiet --yes \
    'conda-forge::blas=*=openblas' \
    'ipympl=0.5.*'\
    'ipywidgets=7.5.*' \
    'matplotlib-base=3.3.*' \
    'widgetsnbextension=3.5.*'\
    'pythreejs' \
    'k3d' \
    'xeus-python' \
    'pytables' \
    && \
    conda clean --all -f -y && \
    # Activate ipywidgets extension in the environment that runs the notebook server
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    # Also activate ipywidgets extension for JupyterLab
    # Check this URL for most recent compatibilities
    # https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@^2.0.0 --no-build && \
    jupyter labextension install @bokeh/jupyter_bokeh@^2.0.0 --no-build && \
    jupyter labextension install jupyter-matplotlib@^0.7.2 --no-build && \
    jupyter labextension install @jupyterlab/debugger --no-build && \
    jupyter lab build -y && \
    jupyter lab clean -y && \
    npm cache clean --force && \
    rm -rf "/home/${NB_USER}/.cache/yarn" && \
    rm -rf "/home/${NB_USER}/.node-gyp" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Install facets which does not have a pip or conda package at the moment
WORKDIR /tmp
RUN git clone https://github.com/PAIR-code/facets.git && \
    jupyter nbextension install facets/facets-dist/ --sys-prefix && \
    rm -rf /tmp/facets && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME="/home/${NB_USER}/.cache/"

RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions "/home/${NB_USER}"

RUN jupyter labextension install jupyter-threejs && \
    jupyter lab clean -y && \
    npm cache clean --force && \
    rm -rf "/home/${NB_USER}/.cache/yarn" && \
    rm -rf "/home/${NB_USER}/.node-gyp" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

ENV JUPYTER_ALLOW_INSECURE_WRITES=true

ENV PATH="/home/${NB_USER}/.local/bin":$PATH

USER root

# Pycharm dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  less \
  libxtst-dev libxext-dev libxrender-dev libfreetype6-dev \
  libfontconfig1 libgtk2.0-0 libxslt1.1 libxxf86vm1 \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Visual studio code dependencies 
RUN apt-get update && apt-get install --no-install-recommends -y \
  libc6-dev libgtk2.0-0 libgtk-3-0 libpango-1.0-0 libcairo2 \
  libfontconfig1 libgconf2-4 libnss3 libasound2 libxtst6 unzip \
  libglib2.0-bin libcanberra-gtk-module libgl1-mesa-glx curl \
  build-essential gettext libstdc++6 software-properties-common \
  wget git xterm automake libtool autogen nodejs libnotify-bin \
  aspell aspell-en htop git mono-complete gvfs-bin libxss1 \
  rxvt-unicode-256color x11-xserver-utils sudo vim libxkbfile1 libnss3 \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

USER $NB_UID

WORKDIR $HOME

# Expose multiple ports (Jupiter notebook and ssh).
EXPOSE 8888 22


