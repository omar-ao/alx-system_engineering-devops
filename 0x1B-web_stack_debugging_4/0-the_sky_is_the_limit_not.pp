# Change file descripter limit from 15 to 4096

# Change file descripter limit
exec {'fix ULIMIT':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider => shell,
}

# Restart nginx
-> exec { 'restart nginx':
  command  => 'service nginx restart',
  provider => shell,
}
