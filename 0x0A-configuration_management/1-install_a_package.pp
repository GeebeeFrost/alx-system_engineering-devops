
# This manifest installs the package flask from pip3.

exec { 'apt-get update':
  command => ' sudo usr/bin/apt-get update'
}

package { 'pip3':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

package { 'flask':
  ensure  => '2.1.0',
  require => Package['pip3']
}
