FROM condaforge/mambaforge:latest AS builder
COPY ../environment.yaml .

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        git \
        ca-certificates \
        build-essential \
        cmake \
        cargo \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN ls -l ./environment.yaml && \
    mkdir -p /usr/local/conda && \
    mamba env create -f ./environment.yaml -p /usr/local/conda -y

FROM nmskm240/ubuntu_devtools:latest AS main

COPY --from=builder /usr/local/conda /usr/local/conda
ENV PATH=/usr/local/conda/bin:${PATH}
