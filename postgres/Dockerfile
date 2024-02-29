# Use the official PostgreSQL image
FROM postgres:latest

# Set environment variables
ENV POSTGRES_USER=${DATABASE_USER}
ENV POSTGRES_PASSWORD=${DATABASE_PASS}
ENV POSTGRES_DB=${DATABASE_NAME}

# Copy the initialization script into the container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432
