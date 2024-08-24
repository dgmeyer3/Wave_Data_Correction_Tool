# Use the official PostGIS image as the base image
FROM postgis/postgis:16-3.3

# Set environment variables
ENV POSTGRES_DB=wavedb
ENV POSTGRES_USER=postgres

# Copy initialization scripts
# COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432

# Set the default command to run when starting the container
CMD ["postgres"]

