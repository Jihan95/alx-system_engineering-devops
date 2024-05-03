# installi flask
package {'flask':
  ensure               => '2.1.0',
  provider             => 'pip3',
  reinstall_on_refresh => true,
}

package {'werkzeug':
  ensure               => '2.1.1',
  provider             => 'pip3',
  reinstall_on_refresh => true,
}
