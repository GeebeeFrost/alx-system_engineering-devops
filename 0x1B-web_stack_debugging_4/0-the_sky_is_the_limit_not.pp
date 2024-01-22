# This manuscript fixes an issue with an Apache web server

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/bin', '/usr/local/bin', '/usr/sbin', '/usr/bin']
}

exec { 'restart_nginx':
  command => 'service nginx restart',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  require => Exec['fix--for-nginx']
}
