# Client configuratation file (w/Puppet)

# use private key ~/.ssh/school
file_line { 'use private key':
	ensure => present,
	path   => '/etc/ssh/ssh_config',
	line   => 'IdentityFile ~/.ssh/school',
}

# refuse to authonticate using a password
file_line { 'refuse authentication using password':
	ensure => present,
	path   => '/etc/ssh/ssh_config',
	line   => 'PasswordAuthentication no',
}
