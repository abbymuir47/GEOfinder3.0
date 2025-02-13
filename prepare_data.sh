#! /bin/bash

set -o errexit

all_geo_tsv_file_path="data/AllGEO.tsv.gz"
filtered_geo_tsv_file_path="data/FilteredGEO.tsv.gz"
embeddings_dir_path="data/Embeddings"

mkdir -p tmp/GSE tmp/Embeddings tmp/Models

##docker run -i -t --rm \
#docker run --rm \
#    -v "$(pwd)":/app \
#    --user $(id -u):$(id -g) \
#    srp33/geofinder \
#        python getAllGEO.py /app/tmp/GSE "${all_geo_tsv_file_path}"

##docker run -i -t --rm \
#docker run --rm \
#    -v "$(pwd)":/app \
#    --user $(id -u):$(id -g) \
#    srp33/geofinder \
#        python filterGEO.py "${all_geo_tsv_file_path}" "${filtered_geo_tsv_file_path}"

##docker run -i -t --rm \
#docker run --rm \
#    -v "$(pwd)":/app \
#    -v $(pwd)/tmp/Models:/Models \
#    --user $(id -u):$(id -g) \
#    srp33/geofinder \
#        python saveEmbeddings.py "${filtered_geo_tsv_file_path}" "thenlper/gte-large" "${embeddings_dir_path}"

##docker run -i -t --rm \
#docker run --rm \
#    -v "$(pwd)":/app \
#    --user $(id -u):$(id -g) \
#    srp33/geofinder \
#        python normalizeFilteredData.py "${filtered_geo_tsv_file_path}" data
