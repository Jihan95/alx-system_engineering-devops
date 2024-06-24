#update ulimit in nginx
exec { 'update ulimit variable':
 command => 'sed -i \'s/^ULIMIT=.*/ULIMIT="-n 4096"/\' /etc/default/nginx',
 provider => 'shell',
}
-> exec { 'restart':
  command  => 'service nginx restart',
  provider => 'shell',
}
