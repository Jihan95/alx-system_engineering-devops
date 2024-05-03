# installi flask
package {'flask':
  ensure               => '2.1.0',
  provider             => 'pip3',
  reinstall_on_refresh => true,
}
