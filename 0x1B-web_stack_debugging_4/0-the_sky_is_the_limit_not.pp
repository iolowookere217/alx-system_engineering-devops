# A puppet manifest that increases Ulimit to accommodate large requests
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 4096'\n",
}
