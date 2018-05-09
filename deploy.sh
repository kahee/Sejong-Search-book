#!/usr/bin/env bash
#1.Dockerfile.base를 사용해서 eb-docker:base를 생성
# eb-docker:base에 <username>/eb-docker:base 태그를 붙이고
# docker push

#2. eb-deploy시 .secrets폴더를 stage영역에 추가한 후 작업완료 후 삭제
git add -f .secrets && eb deploy --staged --profile=eb; git reset HEAD .secrets

