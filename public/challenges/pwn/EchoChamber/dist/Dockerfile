FROM ubuntu:22.04@sha256:cb2af41f42b9c9bc9bcdc7cf1735e3c4b3d95b2137be86fd940373471a34c8b0 AS ub

RUN mkdir /app
COPY chall /app/run
COPY flag /flag
RUN chmod +x /app/run

FROM pwn.red/jail
COPY --from=ub / /srv