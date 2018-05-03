#!/bin/bash


# help funciton
help()
{
cat << EOF

Usage: $0 <NE name> <csv file name>

1 - The NE list: "oa" or "blade"
2 - The content formats of csv file must be as follows:
ALARM NUMBER : ## : SEVERITY : ## : ALARM TEXT : ## : MEANING : ## : INSTRUCTIONS : ## : EFFECT : ## : ADDITION INFORMATION : ## : CANCELLING : ## : ALARM TYPE

Sample: $0 oa test.csv

EOF
}


# create man funciton
Part()
{
cat >> $outFileName << EOF
<?xml version="1.0" encoding="UTF-8"?><com.nokia.oss.fm.fmbasic:AlarmDescription xmi:version="2.0" xmlns:xmi="http://www.omg.org/XMI" xmlns:com.nokia.oss.fm.fmbasic="http:///com/nokia/oss/fm/fmbasic.ecore" patchLevel="00.001" specificProblem="$alarmNumber" alarmText="$alarmText" alarmType="$alarmType" meaning="$meaning" effect="$effect" supplementaryInformationFields="$additionInfo" instructions="$instructions" cancelling="$cancelling" perceivedSeverityInfo="$severity"><Adaptation href="../com.nsn.hp.$NE.common#/"/></com.nokia.oss.fm.fmbasic:AlarmDescription>
EOF

}


# log funciton
Logging()
{
cat << EOF
......NE: $NE
......ALARM_NUMBER: $alarmNumber 
......ALARM_TEXT: $alarmText 
......ALARM_TYPE: $alarmType 
......MEANING: $meaning 
......EFFECT: $effect 
......ADDITION INFORMATION: $additionInfo 
......INSTRUCTIONS: $instructions 
......CANCELLING: $cancelling 
......SEVERITY: $severity 
EOF
}


# check arguments
if [ -z $1 ] || [ -z $2 ];then
  echo -e "\n!!!Script not implemented for that parameter."
  help  
  exit
fi

if [ $1 = "-h" ];then
  help
  exit
elif [ $1 = "oa" ];then
  NE=hphw
  echo "...Start createing man file of hphw."
elif [ $1 = "blade" ];then 
  NE=serverblade
  echo "...Start createing man file of serverblade."
elif [ $1 != "oa" ] && [ $1 != "blade" ];then
  help
  exit
fi


# split file and create directory 
dos2unix $2
split -l 1 $2 temp_
rm -rf temp_aa
outDir="Output_Man_$NE"
rm -rf $outDir
mkdir -p $outDir


# create man files one by one
for filelist in `ls temp_*`
do
    alarmNumber=`cat $filelist |awk -F ',##,' '{print $1}'`
    severity=`cat $filelist |awk -F ',##,' '{print $2}'`
    alarmText=`cat $filelist |awk -F ',##,' '{print $3}'`
    meaning=`cat $filelist |awk -F ',##,' '{print $4}'`
    instructions=`cat $filelist |awk -F ',##,' '{print $5}'`
    effect=`cat $filelist |awk -F ',##,' '{print $6}'`
    additionInfo=`cat $filelist |awk -F ',##,' '{print $7}'`
    cancelling=`cat $filelist |awk -F ',##,' '{print $8}'`
    alarmType=`cat $filelist |awk -F ',##,' '{print $9}'`

    outFileName=./"$outDir"/"$alarmNumber".man
    if [ $severity = "clear" ];then
      echo "...No man file for the clear type alarm."
    else
      echo "...Start creating man file: $outFileName"
      Logging
      Part $alarmNumber $alarmText $alarmType $meaning $effect $additionInfo $instructions $cancelling $severity $NE
      echo "...The man file is complete."
    fi
done


# clear temp files 
rm -rf temp*
echo -e "...All of the work has been finished! The output traps in dir: ./$outDir"
ls -l ./$outDir
