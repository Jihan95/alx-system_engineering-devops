# Client Configuration file
file { '/root/.ssh/config':
  ensure  => 'present',
  path    => '/root/.ssh/config',
  mode    => '0600',
  content => @(EOT)
   Host 52.3.243.155
    HostName 52.3.243.155
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  EOT
  }
