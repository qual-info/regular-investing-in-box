#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os

mdFiles = []
hasReadMe = False
for root, dirs, files in os.walk("."):
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list

    # 遍历文件
    for f in files:
        if f.endswith(".md"):
            fileName = os.path.join(root, f)[2:]
            if "_book" in fileName:
                continue
            if "SUMMARY.md" == fileName:
                continue
            if "/" not in fileName:
                # 只取更目录的md文件
                if fileName == "README.md":
                    hasReadMe = True
                else:
                    mdFiles.append(fileName)

mdFiles = sorted(mdFiles)
summaryContent = "# Summary\n\n"
if hasReadMe:
    summaryContent += "* [README.md](README.md)\n"
exitFold = []
for mdFile in mdFiles:
    files = mdFile.split("/")
    if len(files) == 1:
        summaryContent += "* [{0}]({0})\n".format(mdFile)
    else:
        if files[0] not in exitFold:
            summaryContent += "* [{0}]({0}/README.md)\n".format(files[0])
            exitFold.append(files[0])
        summaryContent += "	* [{1}]({0}/{1})\n".format(files[0], files[1])

with open("SUMMARY.md",'w') as file_obj:
    file_obj.write(summaryContent)
