#!/bin/bash


# help funciton
help()
{
cat << EOF

Usage: $0 <csv file name>

The content formats of csv file must be as follows:
    OID :: TRAP NAME :: ALARM NUMBER :: SEVERITY :: ALARM TEXT :: VARIABLE
    
EOF
}


# trap funciton - part1
TrapPartOne()
{
echo -e "...trapName: $trapName \n...alarmNumber: $alarmNumber \n...alarmText: $alarmText \n...severity: $severity"
cat >> $outFileName << EOF
            <Alarm AlarmIdentifier="$trapName">
                <MappingConfig>
                    <SystemDN/>
                    <EventTime>
                        <dateFormatMapping/>
                    </EventTime>
                    <SpecificProblem>
                        <DefaultMapping>
                            <Text>$alarmNumber</Text>
                        </DefaultMapping>
                    </SpecificProblem>
                    <AlarmText>
                        <AdvancedMapping>
                            <AdvancedMappingType value="Text">
                                <Text>$alarmText</Text>
                            </AdvancedMappingType>
                        </AdvancedMapping>
                    </AlarmText>
                    <PerceivedSeverity>
                        <DefaultMapping>
                            <Text>$severity</Text>
                        </DefaultMapping>
                    </PerceivedSeverity>
                    <AdditionalText5>
                        <AdvancedMapping>
EOF
}


# trap funciton - part2
TrapPartTwo()
{   
echo "...variable: "
    echo $variable | sed 's/#/\n/g' | tr -d '\r' | while read line
    do
      # echo "line ======" $line
      VTEXT=`echo $line |awk -F '=' '{print $1}'`
      VID=`echo $line |awk -F '=' '{print $2}'`
      echo "......" $VTEXT
      echo "......" $VID   
      echo "                            <AdvancedMappingType value=\"Text\">" >> $outFileName
      if [ $VTEXT == "sysName" ];then
        echo "                                <Text>$VTEXT:</Text>" >> $outFileName
      else
        echo "                                <Text>&#xD;&#xA;$VTEXT:</Text>" >> $outFileName     
      fi
      echo "                            </AdvancedMappingType>" >> $outFileName
      echo "                            <AdvancedMappingType value=\"Varbind-OID\">" >> $outFileName
      echo "                                <varBind OID=\"$VID\"/>" >> $outFileName
      echo "                            </AdvancedMappingType>" >> $outFileName
    done
}


# trap funciton - part3
TrapPartThree()
{
echo "...oid: $oid"
cat >> $outFileName << !
                        </AdvancedMapping>
                    </AdditionalText5>
                    <EventType>
                        <DefaultMapping>
                            <Text>processingError</Text>
                        </DefaultMapping>
                    </EventType>
                    <AlarmId>
                        <AdvancedMapping>
                            <AdvancedMappingType value="Text">
                                <Text>0</Text>
                            </AdvancedMappingType>
                        </AdvancedMapping>
                    </AlarmId>
                </MappingConfig>
                <Criteria>
                    <AlarmNewCriteria>
                        <TrapOIDCriteria>
                            <OID>$oid</OID>
                        </TrapOIDCriteria>
                    </AlarmNewCriteria>
                </Criteria>
            </Alarm>
!
}


# trap funciton for clear type
ClearPart()
{
echo -e "...trapName: $trapName \n...alarmNumber: $alarmNumber \n...oid: $oid"
cat >> $outFileName << EOF
        <Alarm AlarmIdentifier="$trapName">
            <MappingConfig>
                <SystemDN/>
                <EventTime>
                    <dateFormatMapping/>
                </EventTime>
                <SpecificProblem>
                    <DefaultMapping>
                        <Text>$alarmNumber</Text>
                    </DefaultMapping>
                </SpecificProblem>
                <AlarmId>
                    <AdvancedMapping>
                        <AdvancedMappingType value="Text">
                            <Text>0</Text>
                        </AdvancedMappingType>
                    </AdvancedMapping>
                </AlarmId>
            </MappingConfig>
            <Criteria>
                <AlarmClearedCriteria>
                    <TrapOIDCriteria>
                        <OID>$oid</OID>
                    </TrapOIDCriteria>
                </AlarmClearedCriteria>
            </Criteria>
        </Alarm>
EOF
}


# check arguments
if [  -z $1 ];then
  echo "No file!!!"
  help  
  exit
fi

if [ $1 = "-h" ];then
  help
  exit
fi


# split file and create Directory
dos2unix $1
split -l 1 $1 temp_  # split by row
rm -rf temp_aa
outDir=Output_Trap
rm -rf $outDir
mkdir -p $outDir


# creae trap file one by one
for filelist in `ls temp_*`
do
    oid=`cat $filelist |awk -F ',' '{print $1}'`
    trapName=`cat $filelist |awk -F ',' '{print $2}'`
    alarmNumber=`cat $filelist |awk -F ',' '{print $3}'`
    severity=`cat $filelist |awk -F ',' '{print $4}'`
    alarmText=`cat $filelist |awk -F ',' '{print $5}'`
    variable=`cat $filelist |awk -F ',' '{print $6}'`

    if [ $severity = "clear" ];then
      outFileName=./"$outDir"/output_trap_"$alarmNumber"_"$trapName"_clear.xml
      echo "# Start creating clear trap file: $outFileName"
      ClearPart $trapName $alarmNumber $oid
      echo "# The clear trap file is complete."
    else
      outFileName=./"$outDir"/output_trap_"$alarmNumber"_"$trapName".xml
      echo "# Start creating trap file: $outFileName"
      TrapPartOne $trapName $alarmNumber $alarmText $severity
      TrapPartTwo $variable $outFileName
      TrapPartThree $oid
      echo "# The trap file is complete."
    fi
done

# clear temp files and create all_output_traps
rm -rf temp*
for filelist in `ls ./"$outDir"/output_trap*`
do
  cat  $filelist >> ./"$outDir"/all_output_traps.xml
done
echo -e "!!! All of the work has been finished! \nThe output traps in dir: ./$outDir"
ls -l ./$outDir
