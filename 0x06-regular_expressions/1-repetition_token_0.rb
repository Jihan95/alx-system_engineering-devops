#!/usr/bin/env ruby
if ARGV.length == 1
  arg = ARGV[0]
  matches = arg.scan(/hbt{2,5}n/)
  puts matches.join("")
end
