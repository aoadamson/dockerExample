FROM postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB testdb
COPY sql_files/test.sql /docker-entrypoint-initdb.d