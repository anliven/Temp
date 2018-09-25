#!/bin/sh

source_files=(
/opt/oss/NSN-cse_jetty/conf/webapps/command-executor.war
/opt/oss/NSN-cse_jetty/conf/etc/jetty.xml
/opt/oss/NSN-cse_jetty/conf/etc/jetty-http.xml
/opt/oss/NSN-cse_jetty/conf/etc/command-executor.xml
/opt/oss/NSN-cse_jetty/conf/start.ini
/opt/oss/NSN-cse_jetty/conf/logback.xml
/opt/oss/NSN-cse_jetty/conf/etc/jetty-requestlog.xml
)

target_files=(
/opt/jetty/webapps/command-executor.war
/opt/jetty/etc/jetty.xml
/opt/jetty/etc/jetty-http.xml
/opt/jetty/webapps
/opt/jetty/start.ini
/opt/jetty/resources/logback.xml
/opt/jetty/etc/jetty-requestlog.xml
)

CopyFiles()
{
  for i in "${!source_files[@]}"
  do
      if [ -f ${source_files[i]} ];then
        cp -f ${source_files[i]} ${target_files[i]}
      else
        echo "No such file : ${source_files[i]}" 
        exit 1
      fi
  done
  chown -R jettysrv:sysop /opt/jetty
  chown omc:sysop /opt/jetty/etc
}

StartJetty()
{
  hostNode=`hostname`
  smanager.pl start service jetty-$hostNode
}

cmd_list=(
'/opt/oss/NSN-cse_jetty/bin/jetty_create_user_install.sh jettysrv'
'mkdir -p /var/opt/oss/log/jetty'
'chown -R jettysrv:sysop /var/opt/oss/log/jetty'
'chmod 775 /var/opt/oss/log/jetty'
'unzip -o /opt/oss/NSN-cse_jetty/install/zip/jetty.zip -d /opt/'
'CopyFiles'
'cp /opt/oss/NSN-cse_jetty/bin/jetty.service /usr/lib/systemd/system/jetty.service'
'chmod 644 /usr/lib/systemd/system/jetty.service'
'systemctl enable jetty'
'StartJetty'
)

for index in "${!cmd_list[@]}"
do
    ${cmd_list[index]}
    if [ $? -ne 0 ];then
      echo "${cmd_list[index]} failed."
      exit 1
    fi
done

exit 0
