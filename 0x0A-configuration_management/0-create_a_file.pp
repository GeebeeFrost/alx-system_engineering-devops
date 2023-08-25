# This manifest creates a file named school in /tmp
$content = 'I love Puppet'

file { 'school':
  ensure  => file,
  path    => '/tmp/school'
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => $content
}
