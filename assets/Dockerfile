# Define function directory
ARG FUNCTION_DIR="/function"

# Multi-stage build: grab a fresh copy of the base image
FROM --platform=amd64 rocker/rstudio:4.2.2 as build

ENV FOLDER="/home/rstudio"
COPY  rstudio_fordead/install_geospatial.sh rstudio_fordead/install2.r rstudio_fordead/auth_theia.txt $FOLDER
RUN chown -R rstudio:rstudio $FOLDER

RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  curl \
  libcurl4-openssl-dev 


WORKDIR $FOLDER
RUN chmod +x $FOLDER/install_geospatial.sh
RUN $FOLDER/install_geospatial.sh
RUN rm $FOLDER/install_geospatial.sh
RUN rm $FOLDER/install2.r
RUN mv $FOLDER/auth_theia.txt /usr/local/lib/R/site-library/theiaR
RUN pip install numpy fiona geopandas rasterio xarray scipy dask pathlib rioxarray path plotly netcdf4 matplotlib
RUN git clone https://gitlab.com/fordead/fordead_package.git
RUN cd fordead_package
RUN pip install /home/rstudio/fordead_package

#RUN Rscript -e "install.packages(c('httr', 'jsonlite', 'logger', 'logging'), repos = 'https://cloud.r-project.org/')"

# Include global arg in this stage of the build
ARG FUNCTION_DIR
ENV LAMBDA_RUNTIME_DIR="/var/runtime"
ENV LAMBDA_TASK_ROOT="/function"
ENV ENV PATH="${PATH}:/tmp/data/lib"


RUN mkdir /var/runtime
RUN printf '#!/bin/sh\ncd $FUNCTION_DIR\nRscript bootstrap.R' > /var/runtime/bootstrap \
  && chmod o+rx /var/runtime/bootstrap
RUN chmod 755 -R /var/runtime/

RUN pip install awslambdaric

# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the build image dependencies

# Copy function code
COPY runtime.R functions.R bootstrap.R rstudio_fordead/s2_list.R  ${FUNCTION_DIR}/
RUN chmod +x -R /function/

COPY rstudio_fordead/  ${FUNCTION_DIR}/.
RUN chmod +x -R  $FUNCTION_DIR


RUN mkdir /tmp/data
RUN chmod +rw /tmp/data

RUN mkdir /tmp/data/lib
RUN chmod rwx /tmp/data/lib

ENTRYPOINT ["sh", "/var/runtime/bootstrap"]
CMD [ "functions.download" ]
        