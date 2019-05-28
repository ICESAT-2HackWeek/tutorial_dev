import paramiko  # pip install paramiko


def list_files(host, user, pwd, cmd):
    # And create a client instance.
    client = paramiko.SSHClient()

    # Create a 'host_keys' object
    # and load our local known hosts  
    host_keys = client.load_system_host_keys()

    # Connect to our client w/remote machine credentials
    client.connect(host, username=user, password=pwd)

    # Assign input, output and error variables to a
    # command we will be issuing on the remote system
    stdin, stdout, stderr = client.exec_command(cmd)

    # We iterate over stdout
    files = [line.strip('\n') for line in stdout]

    # Close the connection to our client
    client.close()
    return files


host, user, pwd = 'devon.jpl.nasa.gov', 'paolofer', 'Buzios19@' 
cmd = 'ls /u/devon-r2/shared_data/icesat2/atl06/rel205/raw/*.h5'

files = list_files(host, user, pwd, cmd)

print files[0]
print len(files)
