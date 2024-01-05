#!/usr/bin/env ruby
puts ARGV[0].scan(/.*from:([\w\d\+]+).*to:([\d\+]+).*flags:([\-0-1:]+).*/).join(",")
