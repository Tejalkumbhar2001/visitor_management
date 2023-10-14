# Copyright (c) 2023, Tejal KUmbhar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AddTeamMember(Document):
	def before_submit(self):
		self.user_doc_create()
		self.RRR()
		frappe.set_value("User",self.email,"role_profile_name",self.role)
	def before_save(self):
		if self.password != self.confirm_password:
			frappe.throw("password not matching")

	def on_cancel(self):
		self.delete_company_name_field_from_user_permission()
		self.delete_designation_name_field_from_designation()
		self.delete_company_name_field_from_user()
		
	def user_doc_create(self):
		doc = frappe.new_doc('User')
		doc.first_name= self.first_name
		doc.last_name=self.last_name
		doc.email=self.email   
		doc.mobile_no=self.mobile
		doc.company=self.company
		doc.new_password=self.password
		doc.role_profile_name=self.role
		doc.insert()
		doc.save()	

		

	def RRR(self):
		k = frappe.new_doc('User Permission')
		k.user = self.email
		k.allow='Company'
		k.for_value=self.company
		k.apply_to_all_doctypes =1
		k.insert()
		k.save()

	def delete_company_name_field_from_user(self):
		hat =frappe.get_all("User", filters = {"name":self.email} )
		if hat:
			p=frappe.get_doc("User",hat[0].name)
			p.delete()

	
	def delete_company_name_field_from_user_permission(self):
		bat =frappe.get_all("User Permission", filters = {"user":self.email} )
		if bat:
			for b in bat:
				po = frappe.get_doc("User Permission",b.name)
				po.delete()

	
	def delete_designation_name_field_from_designation(self):
		position =frappe.get_all("Company", filters = {"name":self.designation_name} )
		if position:
			p=frappe.get_doc("Company",position[0].name)
			p.delete() 