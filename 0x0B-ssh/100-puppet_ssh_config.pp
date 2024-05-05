# Client Configuration file
file { '/root/.ssh/config':
  ensure  => 'present',
  mode    => '0600',
  content => 'Host \n\t HostName 52.3.243.155 \n\t FileName ~/.ssh/school\n\t PasswordAuthentication no',
  }
