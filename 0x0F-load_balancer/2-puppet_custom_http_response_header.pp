# Configure new machine
class { 'nginx':
  package_ensure => 'latest',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => 'Hello World!',
}

nginx::resource::vhost { 'default':
  www_root       => '/usr/share/nginx/html',
  error_page     => '404 /404.html',
  error_page_dir => '/usr/share/nginx/html',
  add_header     => {
    'X-Served-By' => '$HOSTNAME',
  },
  locations      => {
    '/redirect_me' => {
      ensure   => present,
      content  => 'return 301 http://youtube.com;',
    },
  },
}

file { '/usr/share/nginx/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/var/www/html/index.nginx-debian.html'],
}
