# This manifest ensures that SSH connections don't use password authentication

file_line { 'Turn off pwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
