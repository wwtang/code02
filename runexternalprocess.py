def listdir(dir):
    cmd = 'ls -l' +dir
    print "command to run", cmd 
   # (status, output) = commands.getstatusoutput(cmd)
    (status, output) = commands.getstatusoutput(cmd)
    
    if status:
        sys.stderr.write(output)
        sys.exit(1)
    print output


def main():
    import commands
    import sys
     
    dir = "/bin/ls"
    listdir(dir)
if __name__=="__main__":
    main()
