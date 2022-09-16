#!/usr/bin/env ruby
# Match "hbttn, hbtttn, hbttttn"

puts ARGV[0].scan(/hbt+n/).join
