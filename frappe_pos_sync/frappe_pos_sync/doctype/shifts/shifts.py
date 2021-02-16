# -*- coding: utf-8 -*-
# Copyright (c) 2018, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe_pos_sync.utils import set_date_updated

import uuid


class Shifts(Document):
	def autoname(self):
		if not self.id:
			self.id = 'Shift/' + str(uuid.uuid4())
		self.name = self.id

	def validate(self):
		set_date_updated(self)
