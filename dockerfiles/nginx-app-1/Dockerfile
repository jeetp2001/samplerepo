from alpine/git:v2.30.1 as first
run mkdir /dir1
workdir /dir1
run git clone https://github.com/jeetp2001/http-templates.git

from nginx:1.17.1-alpine as second
copy --from=first /dir1/http-templates/index.html /usr/share/nginx/index.html

