FROM ubuntu:22.04@sha256:cb2af41f42b9c9bc9bcdc7cf1735e3c4b3d95b2137be86fd940373471a34c8b0 AS app
FROM pwn.red/jail

COPY --from=app / /srv

COPY ./vuln /srv/app/run

COPY ./flag.txt /srv/app/flag.txt

EXPOSE 5000

RUN chmod 444 /srv/app/flag.txt
RUN chmod +x /srv/app/run