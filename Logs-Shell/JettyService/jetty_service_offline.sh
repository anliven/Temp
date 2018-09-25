#!/bin/sh

hostNode=`hostname`

CreateJettyFolder()
{
  if [ -d "/opt/jetty_backup/jetty" ]; then
      rm -rf /opt/jetty
      mv -f /opt/jetty_backup/jetty /opt/jetty
      rm -rf /opt/jetty_backup
  fi
}

cmd_list=(
"smanager.pl maintenance jetty-$hostNode on"
"smanager.pl stop service jetty-$hostNode"
"CreateJettyFolder"
"chown -R jettysrv:sysop /var/opt/oss/log/jetty"
"systemctl disable jetty"
"rm -rf /etc/init/jetty.conf"
"rm -rf /etc/init.d/jetty"
"cp /opt/oss/NSN-cse_jetty/bin/jetty.service /usr/lib/systemd/system/jetty.service"
"chmod 644 /usr/lib/systemd/system/jetty.service"
"systemctl enable jetty"
"smanager.pl start service jetty-$hostNode"
"smanager.pl maintenance jetty-$hostNode off"
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
