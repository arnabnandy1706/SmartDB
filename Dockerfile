FROM centos:latest
MAINTAINER <Arnab Kumar Nandy>
RUN yum install httpd -y
WORKDIR /var/www/html
RUN mkdir images
ADD images/learn-blockchain.png images/learn-blockchain.png
ADD index.html index.html
USER apache
EXPOSE 80
CMD ["httpd","-DFOREGROUND"]
