#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Windows():
	@staticmethod	
	def Run(os):
		_ = False
		try:
			for item in os.items():
				_ = re.search(r'windows|win32',str(item),re.I) is not None
				if _:
					return "Windows"
					break
		except Exception,ERROR:
			print ERROR