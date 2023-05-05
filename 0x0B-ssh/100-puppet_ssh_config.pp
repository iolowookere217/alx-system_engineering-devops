#SSH client configuration
exec { 'No passwd auth':
command => 'bash -c "echo PasswordAuthentication no >> /etc/ssh/ssh_config"',
path    => '/usr/bin:/usr/sbin:/bin'
}
exec { 'Identity file':
command => 'bash -c "echo IdentityFile \'~/.ssh/school\' >> /etc/ssh/ssh_config"',
path    => '/usr/bin:/usr/sbin:/bin'
}
exec { 'Pubkey auth':
command => 'bash -c "echo PubkeyAuthentication yes >> /etc/ssh/ssh_config"',
path    => '/usr/bin:/usr/sbin:/bin'
}
