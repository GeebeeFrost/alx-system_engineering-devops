# configures an Nginx server to listen on port 80 and other options

package { 'nginx':
  ensure => installed
}

exec { 'allow_HTTP':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
  require => Package['nginx']
}

file { 'index.html':
  ensure  => file,
  path    => '/var/www/html/index.html',
  content => '<h2>Hello World!<h2>'
}


$lines = ['    location /redirect_me {',
          '         return 301 http://youtube.com;',
          '    }']

$lines.each |$line| {
  file_line { "add_line_${line}":
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => $line,
    match  => 'server_name _;'
  }
}

exec { 'restart_nginx':
  command => 'usr/sbin/service nginx restart'
}
