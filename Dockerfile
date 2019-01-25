FROM python:3.7.1-slim

COPY ["./requirements.txt", "/usr/src/"]
WORKDIR /usr/src/
RUN pip install --no-cache-dir -r requirements.txt

COPY [".", "."]

ARG user
ENV USERNAME=${user}
ARG playlist
ENV ARTIST_PLAYLIST=${playlist}

ARG id
ENV CLIENT_ID=${id}
ARG secret
ENV CLIENT_SECRET=${secret}
ARG uri
ENV REDIRECT_URI=${uri}

CMD ["python", "main.py"]