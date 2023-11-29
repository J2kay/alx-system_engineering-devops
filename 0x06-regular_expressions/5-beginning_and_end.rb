#!/usr/bin/env ruby
# A regular expression matching a string starts with h 
# and ends with an n
puts ARGV[0].scan(/h.n/).join
