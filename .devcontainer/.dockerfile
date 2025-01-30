FROM condaforge/mambaforge:latest AS builder
COPY ../environment.yaml .
RUN ls -l ./environment.yaml && \
    mkdir -p /usr/local/conda && \
    mamba env create -f ./environment.yaml -p /usr/local/conda

FROM nmskm240/ubuntu_devtools:latest AS main

COPY --from=builder /usr/local/conda /usr/local/conda
ENV PATH=/usr/local/conda/bin:${PATH}
