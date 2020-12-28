ARG PYTHON_VERSION=3.9.1-alpine3.12

FROM python:${PYTHON_VERSION}

WORKDIR /usr/src/code

COPY [ "./code", "." ]

CMD [ "python", "main.py" ]
