import os


def collectAllTextFilesInDirectory(path='' , target_path=''):
    result = ''
    for linkFile in os.listdir():
        if linkFile.endswith(path+'.txt'):
            result += open(linkFile , 'r').read()

    open(target_path+'/result.txt' , 'a+').write(result)