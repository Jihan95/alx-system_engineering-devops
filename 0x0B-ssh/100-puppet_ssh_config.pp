# Client Configuration file
File_line { 'Turn off passwd auth':
  path    => '/root/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
}

File_line { 'Declare identity file':
  path    => '/root/.ssh/config',
  line    => 'FileName ~/.ssh/school',
  match   => '^FileName',
}


