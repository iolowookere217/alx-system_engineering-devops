# A puppet file that automatically fix error 500 returned by Apache 
file { '/var/www/html/wp-settings.php':
  ensure => present,
  replace => true,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub("phpp", "php") %>'),
}
