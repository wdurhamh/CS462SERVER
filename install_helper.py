# this needs to be run as super user
#open /etc/sudoers
orig = open('/etc/sudoers', 'r')
edited = ''
for line in orig:
    if 'secure_path =' in line:
	line = line.replace('\n', ':/usr/local/bin\n')
    edited += line
orig.close()

f_new = open('/etc/sudoers', 'w')
f_new.write(edited)
f_new.close()
