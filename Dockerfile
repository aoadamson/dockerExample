FROM postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB testdb
COPY test.sql /docker-entrypoint-initdb.d