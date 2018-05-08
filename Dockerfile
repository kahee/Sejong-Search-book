FROM        ygh131/toy_project
MAINTAINER  yuygh131@gmail.com

ENV         BUILD_MODE              production
ENV         DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

COPY        . /srv/project

RUN         cp -f   /srv/project/.config/${BUILD_MODE}/nginx.conf       /etc/nginx/nginx.conf &&\
            cp -f   /srv/project/.config/${BUILD_MODE}/nginx-app.conf   /etc/nginx/sites-available/ &&\
            rm -f   /etc/nginx/sites-enabled/* &&\
            ln -sf  /etc/nginx/sites-available/nginx-app.conf   /etc/nginx/sites-enabled/

RUN         cp -f   /srv/project/.config/${BUILD_MODE}/supervisord.conf /etc/supervisor/conf.d/

#pkill
CMD         pkill nginx; supervisord -n

#EB에서 프록시로 연결될 port를 열어줌
EXPOSE      80