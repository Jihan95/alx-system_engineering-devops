# Client Configuration file
file { '/root/.ssh/config':
  ensure  => 'present',
  mode    => '0600',
  content => 'Host \n\t FileName ~/.ssh/school\n\t PasswordAuthentication no',
  }
