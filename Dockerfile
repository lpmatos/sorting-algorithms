# =============================================================================
# BASE CONFIGURATION
# =============================================================================

ARG PYTHON_VERSION=3.7.4-alpine3.10

# =============================================================================
# BASE ENV
# =============================================================================

FROM python:${PYTHON_VERSION}

LABEL maintainer="Lucca Pessoa da Silva Matos - luccapsm@gmail.com"

ENV LANG=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN set -ex && apk update && apk upgrade -U && \
    addgroup -S python-group && adduser -S -D -h /usr/src/code python-user python-group && \
    chown -R python-user:python-group /usr /var

WORKDIR /usr/src/code

# =============================================================================
# DOCKER USER
# =============================================================================

USER python-user

# =============================================================================
#COPY TO CONTAINER
# =============================================================================

COPY --chown=python-user:python-group [ "./code", "." ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;

# =============================================================================
# ENTRYPOINT AND CMD
# =============================================================================

ENTRYPOINT []

CMD []
