# This manifest fixes an issue with an Apache server
# by correcting a typo in the Wordpress settings

exec { 'fix_wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin']
}
