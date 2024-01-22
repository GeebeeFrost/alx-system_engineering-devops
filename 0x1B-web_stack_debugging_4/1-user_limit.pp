# This manifest allows holberton user to login and open files without error

exec { 'hard-limit':
  command => 'sed -i "/holberton hard/s/5/5000/" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/local/bin', '/usr/sbin']
}

exec { 'soft-limit':
  command => 'sed -i "/holberton soft/s/4/5000/" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/local/bin', '/usr/sbin']
}
