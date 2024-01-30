#!/usr/bin/env ruby
if ARGV.length == 1
  arg = ARGV[0]
  matches = arg.scan(/School/)
  puts matches.join("")
end
