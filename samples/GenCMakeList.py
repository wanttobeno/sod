import os
import sys
import string
# copy
import shutil

path=os.path.dirname(os.path.realpath(__file__))
alllist=os.listdir(path)
file = u"CMakeLists.in"
destfile = u"CMakeLists.txt"
srcFile= path+"\\"+file
# read file
f = open(srcFile,'r')
f_data = f.read()
#print(f_data)
for fileFind in alllist:
    if(".c" in fileFind):
        srcName,temp = fileFind.split(".")
        srcFile = path+"\\"+fileFind
        dirPath,fileExt = srcFile.split(".")
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        newname = dirPath + "\\" + fileFind

        print("add_subdirectory(samples/"+srcName+")") 
        #print(srcFile)
        #print(newname)
        if not os.path.exists(newname):
            shutil.copyfile(srcFile,newname)
        
        makeFile = dirPath + "\\CMakeLists.txt"
       
        if  os.path.exists(makeFile):
            os.remove(makeFile)
        fwrite=open(makeFile,'wb')
        fwrite.write('############ Gen By Python Script ############\n\n')
        fwrite.write('project('+srcName+')\n')

        fwrite.write('add_executable (${PROJECT_NAME} ')

        fwrite.write(fileFind+" ")
        #print fileIn

        fwrite.write(')\n\n')
        fwrite.write('############ Gen By Python Script ############\n\n')
        fwrite.write(f_data)
        #else:
        #print(srcFile)
     