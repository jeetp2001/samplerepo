from alpine/git:v2.30.1 as code
run mkdir /repo
workdir /repo
run git clone https://github.com/jeetp2001/samplerepo.git

from php:7.2-apache
run docker-php-ext-install mysqli
copy --from=code /repo/samplerepo/. /var/www/html/
