# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_pos_sync"
app_title = "Frappe POS Sync"
app_publisher = "Bai Web and Mobile Lab"
app_description = "Frappe POS ERPNext Sync"
app_icon = "octicon octicon-file-directory"
app_color = "#3498db"
app_email = "hello@bai.ph"
app_license = "MIT"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Customer-note",
                    "Customer-phonenumber",
                    "Customer-email",
                    "Customer-id",
                    "Customer-date_updated",
                    "Deleted Document-sync_status",
                    "Item-tail_sb",
                    "Item-tail_cb",
                    "Item-date_updated",
                    "Item-id",
                    "Item-favorite",
                    "Item-barcode",
                    "Item-in_frappe_pos",
                    "Item-sku",
                    "Item-color",
                    "Item-shape",
                    "Item-category",
                    "Item-color_or_image",
                    "Payment Entry-wallet_card_number",
                    "Payment Entry-top_up_wallet",
                    "Customer Credit Limit-total_prepaid_balance",
                    "Error Log-device_id",
                    "Error Log-wallet_card",
                    "Error Log-pin",
                    "Sales Invoice-receipt"
                ]
            ]
        ]
    }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_pos_erpnext/css/frappe_pos_erpnext.css"
# app_include_js = "/assets/frappe_pos_erpnext/js/frappe_pos_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_pos_erpnext/css/frappe_pos_erpnext.css"
# web_include_js = "/assets/frappe_pos_erpnext/js/frappe_pos_erpnext.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Payment Entry" : "public/js/payment_entry.js",
    "Customer" : "public/js/customer.js",
    "Sales Invoice" : "public/js/sales_invoice.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappe_pos_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_pos_erpnext.install.before_install"
# after_install = "frappe_pos_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_pos_erpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Item": {
        "validate": "frappe_pos_sync.doc_events.item.validate",
        "before_save": "frappe_pos_sync.doc_events.item.before_save"
    },
    "Sales Invoice": {
        "validate": "frappe_pos_sync.doc_events.sales_invoice.validate",
        "before_submit": "frappe_pos_sync.doc_events.sales_invoice.before_submit",
        "after_submit": "frappe_pos_sync.doc_events.sales_invoice.after_submit",
    },
    "Payment Entry": {
        "on_submit": "frappe_pos_sync.doc_events.payment_entry.on_submit",
    },
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    "hourly": [
        "frappe_pos_sync.background_jobs.generate_si"
    ]
    # "* * * * *": [
    #     "frappe_pos_erpnext.tasks.sync_couchdb"
    # ],
    # "all": [
    #     "frappe_pos_erpnext.tasks.sync_couchdb"
    # ],
    # "daily": [
    # 	"frappe_pos_erpnext.tasks.daily"
    # ],
    # "hourly": [
    # 	"frappe_pos_erpnext.tasks.hourly"
    # ],
    # "weekly": [
    # 	"frappe_pos_erpnext.tasks.weekly"
    # ]
    # "monthly": [
    # 	"frappe_pos_erpnext.tasks.monthly"
    # ]
}

# Testing
# -------

# before_tests = "frappe_pos_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_pos_erpnext.event.get_events"
# }