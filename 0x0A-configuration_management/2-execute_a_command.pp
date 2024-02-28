# This manifest kills `killmenow` process

exec {'killmenow':
  command => '/usr/bin/pkill killmenow'
}
