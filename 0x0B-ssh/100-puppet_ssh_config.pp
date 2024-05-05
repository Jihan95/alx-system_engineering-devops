# Client Configuration file
file { '/root/.ssh/config':
  ensure  => 'present',
  path    => '/root/.ssh/config',
  mode    => '0600',
  content => @(EOT)
   Host
    HostName 52.3.243.155
    FileName ~/.ssh/school
    PasswordAuthintication no
  EOT
  }
