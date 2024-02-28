# Installs pip3
package { 'python3-pip':
  ensure => installed,
}

# Install flask=2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Install wrkseug 2.2.1
package { 'Werkzeug':
  ensure   => '2.2.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
