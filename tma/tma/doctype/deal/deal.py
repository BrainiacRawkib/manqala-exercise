# -*- coding: utf-8 -*-
# Copyright (c) 2021, brainiac and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Deal(WebsiteGenerator):
	def before_submit(self):
		if self.status == '':
			pass
