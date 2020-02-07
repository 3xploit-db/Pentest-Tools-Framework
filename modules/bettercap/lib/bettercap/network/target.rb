# encoding: UTF-8
=begin

BETTERCAP

Author : Simone 'evilsocket' Margaritelli
Email  : evilsocket@gmail.com
Blog   : http://www.evilsocket.net/

This project is released under the GPL 3 license.

=end

module BetterCap
module Network
# This class represents a target, namely a single endpoint device on the
# network.
class Target
  # The IP address of this device.
  attr_accessor :ip
  # The MAC address of the device network interface.
  attr_accessor :mac
  # Network object.
  attr_accessor :network
  # Vendor of the device network interface if available.
  attr_accessor :vendor
  # NetBIOS hostname of the device if available OR interface name in case of
  # local address.
  attr_accessor :name
  # True if the IP attribute of this target needs to be updated.
  attr_accessor :ip_refresh

  # Timeout in seconds for the NBNS hostname resolution request.
  NBNS_TIMEOUT = 30
  # UDP port for the NBNS hostname resolution request.
  NBNS_PORT    = 137
  # Buffer size for the NBNS hostname resolution request.
  NBNS_BUFSIZE = 65536
  # NBNS hostname resolution request buffer.
  NBNS_REQUEST = "\x82\x28\x0\x0\x0\x1\x0\x0\x0\x0\x0\x0\x20\x43\x4B\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x0\x0\x21\x0\x1"

  @@prefixes = nil
  @@lock = Mutex.new

  # Create a +Target+ object given its +ip+ and (optional) +mac+ address.
  # The +ip+ argument could also be a MAC address itself, in this case the
  # ip address will be parsed from the computer ARP cache and updated
  # accordingly.
  def initialize( ip, mac=nil, network=nil, name=nil )
    if Network::Validator.is_ip?(ip)
      @ip         = ip
      @ip_refresh = false
    elsif Network::Validator.is_mac?(ip)
      @ip         = nil
      mac         = ip
      @ip_refresh = true
    else
      raise BetterCap::Error, "'#{ip}' is not a valid IP or MAC address."
    end

    @mac      = Target.normalized_mac(mac) unless mac.nil?
    @vendor   = Target.lookup_vendor(@mac) unless mac.nil?
    @name     = name
    @network  = network
    @resolver = Thread.new { resolve! } unless Context.get.options.core.no_target_nbns or @ip.nil? or !@network.nil?
  end

  # Return the integer representation of the +ip+ attribute which can be
  # used for sorting a list of +Target+ objects+
  def sortable_ip
    @ip.split('.').inject(0) {|total,value| (total << 8 ) + value.to_i}
  end

  # Return true if both the ip and mac are not nil.
  def spoofable?
    ( !@ip.nil? and !@mac.nil? )
  end

  # +mac+ attribute setter, it will normalize the +value+ and perform
  # a vendor lookup.
  def mac=(value)
    @mac = Target.normalized_mac(value)
    @vendor = Target.lookup_vendor(@mac) unless @mac.nil?
  end

  # Return a verbose string representation of this object.
  def to_s(padding=true)
    address = @ip.nil?? '???' : @ip
    fmt     = padding ? '%-15s : %-17s' : '%s : %s'
    vendor  = @vendor.nil?? " ( ??? )" : " ( #{@vendor} )"

    s = sprintf( fmt, address, @mac )
    s += " / #{@name}" unless @name.nil?
    s += vendor
    s
  end

  # Return a compact string representation of this object.
  def to_s_compact
    return "#{@name}/#{@ip}" if @name
    @ip
  end

  # Return true if this +Target+ is equal to the specified +ip+ and +mac+,
  # otherwise return false.
  def equals?(ip, mac = nil)
    # compare by ip if no mac
    return ( @ip == ip ) if mac.nil?
    # false if no mac or if it's different
    return false if @mac.nil? || ( @mac != mac )

    ###Logger.info "Found IP #{ip} for target #{@mac}!" if @ip.nil?
    @ip = ip
    return true
  end

  def self.normalized_mac(v)
    v.split(':').map { |e| e.size == 2 ? e.upcase : "0#{e.upcase}" }.join(':')
  end

private

  # Attempt to perform a NBNS name resolution for this target.
  def resolve!
    resp, sock = nil, nil
    begin
      sock = UDPSocket.open
      sock.send( NBNS_REQUEST, 0, @ip, NBNS_PORT )
      resp = if select([sock], nil, nil, NBNS_TIMEOUT)
        sock.recvfrom(NBNS_BUFSIZE)
      end
      if resp
        @name = parse_nbns_response resp
        ###Logger.info "Found NetBIOS name '#{@name}' for address #{@ip}"
      end
    rescue Exception => e
      Logger.debug e
    ensure
      sock.close if sock
    end
  end

  # Given the +resp+ NBNS response, parse the hostname from it.
  def parse_nbns_response resp
    resp[0][57,15].to_s.strip
  end

  # Lookup the given +mac+ address in order to find its vendor.
  def self.lookup_vendor( mac )
    @@lock.synchronize {
      if @@prefixes.nil?
        Logger.debug 'Preloading hardware vendor prefixes ...'

        @@prefixes = {}
        filename = File.dirname(__FILE__) + '/hw-prefixes'
        File.open( filename ).each do |line|
          if line =~ /^([A-F0-9]{6})\s(.+)$/
            @@prefixes[$1] = $2
          end
        end
      end
    }

    @@prefixes[ mac.split(':')[0,3].join('').upcase ]
  end
end
end
end
