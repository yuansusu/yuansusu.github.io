#!/bin/env sh
files=$(find  /data/app/qa01  -maxdepth 4 -name ".env")

baseDir="/env_back/qa01/"


echo " 执行备份qa01";
for fileName in  ${files}
do
  echo ${fileName};
  basepath=$(cd `dirname ${fileName}`; pwd) ;
 #echo ${basepath}
 projectName="${baseDir}$(basename ${basepath})" ;
 echo ${projectName}
 [ ! -d ${projectName} ] && mkdir -p ${projectName} || echo ${projectName}"目录已经存在"
 envfile="${projectName}/.env"
 [ ! -f "${projectName}/.env" ] && cp  ${fileName} ${projectName} || echo "${envfile}文件已经存在"

done ;