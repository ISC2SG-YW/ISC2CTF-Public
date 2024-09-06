# Use an official PHP runtime as a parent image
FROM php:8.1-apache

# Set working directory
WORKDIR /var/www/html

# Flag?
ENV FLAG="ISC2CTF{!_lOve_pOlLuTIoN_\$0_MuCH!}"
# Install SQLite3 and PHP SQLite extension
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev \
    && docker-php-ext-install pdo_sqlite

# Copy the current directory contents into the container at /var/www/html
COPY . /var/www/html

RUN chmod -R 777 /var/www/html/pollution.db
RUN chmod -R 777 /var/www/html/

# Expose port 483 for the PHP server
EXPOSE 483

# Change Apache to listen on port 483
RUN sed -i 's/80/483/' /etc/apache2/ports.conf /etc/apache2/sites-available/000-default.conf


# Start Apache server
CMD ["apache2-foreground"]
