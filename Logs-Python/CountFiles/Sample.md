
# 使用示例
- 本脚本用来统计man文件指定字段的数目
- 在man文件所在目录运行，或者指定man文件所在目录的绝对路径

```Shell
MINGW64 /d/Anliven-Running/Zen/PycharmProjects
$ py -3 CountFiles.py /D/CI-Git-Files/adap_core4/com.nsn.hp.hphw/com.nsn.hp.hphw-10isdk_man/implementation/o2ml/content/amanual/
The sum total of man files:  61

### Fragment - effect
*** count:49 - None:
 100000.man 350002.man 350003.man 350004.man 350005.man 350006.man 350007.man 350008.man 350009.man 350010.man 350011.man 350012.man 350013.man 350014.man 350015.man 350016.man 350017.man 350018.man 350019.man 350020.man 350021.man 350022.man 350023.man 350024.man 350025.man 350026.man 350027.man 350028.man 350029.man 350030.man 350031.man 350032.man 350033.man 350034.man 350035.man 350036.man 350037.man 350038.man 350039.man 350040.man 350041.man 350042.man 350043.man 350044.man 350045.man 350046.man 350047.man 350048.man 350049.man
*** count:10 - Empty:
 350257.man 350572.man 350573.man 350574.man 350575.man 350576.man 350577.man 350579.man 350580.man 350581.man
*** count:2 - Have:
 350000.man 350001.man

### Fragment - supplementaryInformationFields
*** count:49 - None:
 100000.man 350000.man 350001.man 350002.man 350003.man 350004.man 350005.man 350006.man 350007.man 350008.man 350009.man 350010.man 350011.man 350012.man 350013.man 350014.man 350015.man 350016.man 350017.man 350018.man 350019.man 350020.man 350021.man 350022.man 350023.man 350024.man 350025.man 350026.man 350027.man 350028.man 350029.man 350030.man 350033.man 350034.man 350035.man 350036.man 350037.man 350038.man 350039.man 350040.man 350041.man 350042.man 350043.man 350044.man 350045.man 350046.man 350047.man 350048.man 350049.man
*** count:10 - Empty:
 350257.man 350572.man 350573.man 350574.man 350575.man 350576.man 350577.man 350579.man 350580.man 350581.man
*** count:2 - Have:
 350031.man 350032.man

### Fragment - instructions
*** count:21 - None:
 100000.man 350002.man 350005.man 350014.man 350016.man 350024.man 350026.man 350029.man 350030.man 350031.man 350032.man 350033.man 350040.man 350041.man 350042.man 350043.man 350044.man 350045.man 350046.man 350047.man 350048.man
*** count:7 - Empty:
 350257.man 350572.man 350573.man 350574.man 350579.man 350580.man 350581.man
*** count:33 - Have:
 350000.man 350001.man 350003.man 350004.man 350006.man 350007.man 350008.man 350009.man 350010.man 350011.man 350012.man 350013.man 350015.man 350017.man 350018.man 350019.man 350020.man 350021.man 350022.man 350023.man 350025.man 350027.man 350028.man 350034.man 350035.man 350036.man 350037.man 350038.man 350039.man 350049.man 350575.man 350576.man 350577.man

MINGW64 /d/Anliven-Running/Zen/PycharmProjects
$
```