# A puppet manifest that increases Ulimit to accommodate large requests
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='N 1000'\nCONCURRENCY=100\n",
}
