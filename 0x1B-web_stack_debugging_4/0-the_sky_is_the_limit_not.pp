# A puppet manifest that increases Ulimit to accommodate large requests
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 2048'\nCONCURRENCY=100\n",
}
