# Change the OS configuration so that it is possible to login with
# the holberton user and open a file without any error message.
exec {'change hard limit':
  command  => 'sed -i "/^holberton/s/ [0-9]$/ 10000/"  /etc/security/limits.conf',
  provider => shell,
}
