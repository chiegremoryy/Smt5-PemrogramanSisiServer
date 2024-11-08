FROM php:8.3.12-apache
WORKDIR /var/www/html

RUN apt-get update && \
    apt-get install -y libpng-dev && \
    docker-php-ext-install pdo pdo_mysql gd && \
    docker-php-ext-install mysqli && \
    docker-php-ext-enable mysqli

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Pastikan pecl di jalankan dengan cara yang benar
RUN apt-get install -y libzip-dev && \
    pecl install redis && \
    docker-php-ext-enable redis

EXPOSE 80

CMD ["apache2-foreground"]
