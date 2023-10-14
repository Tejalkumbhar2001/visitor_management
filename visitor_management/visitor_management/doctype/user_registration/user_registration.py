# Copyright (c) 2023, Tejal KUmbhar and contributors
# For license information, please see license.txt

import frappe
import re
from frappe.model.document import Document

class UserRegistration(Document):
	def before_save(self):
		if self.password != self.confirm_password:
			frappe.throw("password not matching")
		self.company_doc_create()
		self.user_doc_create()
		self.RRR() 
		self.docstatus=1
		 
		
		

	def on_trash(self):
		self.delete_company_name_field_from_user_permission()	
		self.delete_company_name_field_from_user()
		self.delete_company_name_field_from_company()

	
	def on_cancel(self):
		self.delete_company_name_field_from_user_permission()
		self.delete_company_name_field_from_user()
		self.delete_company_name_field_from_company()



	def user_doc_create(self):
		doc = frappe.new_doc('User')
		doc.first_name= self.first_name
		doc.last_name=self.last_name
		doc.email=self.email
		doc.mobile_no=self.mobile
		doc.company=self.company_nameas_per_your_gst
		doc.new_password=self.password
		doc.role_profile_name="Visitor Administrator"
		doc.insert()
		doc.save()					
		

	def company_doc_create(self):
		doc = frappe.new_doc('Company')
		doc.company_name=self.company_nameas_per_your_gst
		doc.default_currency=self.currency
		doc.country=self.country
		doc.insert()
		doc.save()
		self.company_name=self.company_nameas_per_your_gst
	def RRR(self):
		k = frappe.new_doc('User Permission')
		k.user = self.email
		k.allow='Company'
		k.for_value=self.company_nameas_per_your_gst
		k.apply_to_all_doctypes =1
		k.insert()
		k.save()

	# def user_permission_doc(self):
	# 	doc = frappe.new_doc('User Permission')
	# 	doc.user = self.email
	# 	doc.allow='Company'
	# 	doc.for_value=self.company_nameas_per_your_gst
	# 	doc.insert()
	# 	doc.save()
		

	
	def delete_company_name_field_from_user_permission(self):
		bat =frappe.get_all("User Permission", filters = {"user":self.email} )
		if bat:
			for b in bat:
				po = frappe.get_doc("User Permission",b.name)
				po.delete()

	def delete_company_name_field_from_company(self):
		mat =frappe.get_all("Company", filters = {"name":self.company_nameas_per_your_gst} )
		if mat:
			p=frappe.get_doc("Company",mat[0].name)
			p.delete()
		# frappe.delete_doc('Company', self.company_nameas_per_your_gst)

	# Deleting the 'company_name' field from the 'User' document
	def delete_company_name_field_from_user(self):
		hat =frappe.get_all("User", filters = {"name":self.email} )
		if hat:
			p=frappe.get_doc("User",hat[0].name)
			p.delete()
		# frappe.delete_doc('User', self.email)

																											
	
		
		
																																				