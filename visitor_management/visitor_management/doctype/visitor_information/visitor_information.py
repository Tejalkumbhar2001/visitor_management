# Copyright (c) 2023, Tejal KUmbhar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VisitorInformation(Document):
	def before_save(self):
		# self.full_name = f'{self.first_name} {self.last_name or ""}'		
		email = self.email
		# whatsapp_no =self.whatsapp_no
		self.send_email(email)
		
		
		
	def send_email(self,email):
		frappe.sendmail(
			recipients=[email],
			subject= self.company_name,
			message="Thank you for Visiting at "+ self.company_name,
			sender=email
		)



	def delete_prodcut_name_field_from_product(self):
		prodct =frappe.get_all("Designations", filters = {"name":self.product_name} )
		if prodct:
			p=frappe.get_doc("Designations",prodct[0].name)
			p.delete()