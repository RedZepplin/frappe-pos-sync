# import frappe
from frappe import _

def get_data():
	return [
		{
			"label": _("Frappe POS"),
			"items": [
				{
					"type": "doctype",
					"name": "Attendants",
				},
                {
                    "type": "doctype",
                    "name": "Item",
                },
                {
                    "type": "doctype",
                    "name": "Categories",
                },
                {
                    "type": "doctype",
                    "name": "Discounts",
                },
                {
                    "type": "doctype",
                    "name": "Receipts",
                },
                {
                    "type": "doctype",
                    "name": "Payments",
                },
                {
                    "type": "doctype",
                    "name": "Shifts",
                },
                {
                    "type": "doctype",
                    "name": "Device",
                },
                {
                    "type": "doctype",
                    "name": "Frappe POS Settings",
                },
                {
                    "type": "doctype",
                    "name": "Wallet",
                },
                {
                    "type": "doctype",
                    "name": "Wallet Logs",
                }
			]
		}]