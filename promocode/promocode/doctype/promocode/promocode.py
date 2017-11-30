# -*- coding: utf-8 -*-
# Copyright (c) 2015, taher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Promocode(Document):
	pass
def apply_promo(doc, method):
	Promocode_list =frappe.db.sql("select promocode_name from tabPromocode",as_list=1)
	pl= [x[0] for x in Promocode_list]
	frappe.errprint([Promocode_list,pl])

	if doc.promocode !="0":
		if doc.promocode in pl:
			pro = frappe.get_doc("Promocode", doc.promocode)
			discount_per = pro.dis_per
			grand_total = doc.grand_total
			discount_amount = (float(grand_total) * float(discount_per))/100


			doc.discount_amount =discount_amount
		else:
			frappe.msgprint("inValid promocode")