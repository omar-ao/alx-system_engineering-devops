# Puppet script to fix Apache 500 error.

# Replace class name extension from phpp to php
$file = '/var/www/html/wp-settings.php'
exec { 'fix 500 error':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${file}",
  path    => ['/bin', '/usr/bin']
}
