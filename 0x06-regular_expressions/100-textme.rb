#!/usr/bin/env ruby
#  Guillaume Plessis's job
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
