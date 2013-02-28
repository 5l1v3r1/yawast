require 'socket'
require './scanner/http'

def scan(uri)
  begin
    server_info(uri)
  rescue
    puts_error 'Fatal Error: Can not continue.'
  end
end

def server_info(uri)
  begin
    puts_info "Full URI: #{uri}"

    puts_info 'IP(s):'
    dns = Resolv::DNS.new()
    addr = dns.getaddresses(uri.host)
    addr.each do |ip|
      host_name = dns.getname(ip.to_s)
      puts_info "\t\t#{ip} (#{host_name})"
    end
    puts ''

    head = head(uri)
    puts_info 'HEAD:'
    head.each { |k, v| puts_info "\t\t#{k}: #{v}" }
  rescue => e
    puts_error "Error getting basic information: #{e.message}"
    raise
  end
end