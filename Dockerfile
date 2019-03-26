FROM centos:latest
MAINTAINER <Arnab Kumar Nandy>
RUN yum install httpd -y
WORKDIR /var/www/html
RUN mkdir images
ADD images/logo.png images/logo.png
ADD index.html index.html
CMD ["httpd","-DFOREGROUND"]