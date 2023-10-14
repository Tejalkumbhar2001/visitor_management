// Copyright (c) 2023, Tejal KUmbhar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Add Team Member', {
	setup: function(frm) {
		frm.set_query("role", function(doc) {
			return {
				filters: [
				    ['Role Profile', 'name', 'in', ["Visitor Administrator","web user"]],
				]
			};
		});
	},

	// validate: function(frm) {
    //     // Get the value entered in the mobile field
    //     var mobile = frm.doc.mobile;

    //     // Regular expression for Indian mobile numbers (10 digits, starting with 7, 8, or 9)
    //     var indianMobilePattern = /^[789]\d{9}$/;

    //     if (!indianMobilePattern.test(mobile)) {
    //         frappe.throw('Please enter a valid Indian mobile number.');
    //         frappe.validated = false; // Prevent form submission
    //     }
    // }

	
});

frappe.ui.form.on('Add Team Member', {
    validate: function(frm) {
    
        var email = frm.doc.email;

        var EmailPatttern = /^[\w\.-]+@[\w\.-]+\.\w+$/

        if (!EmailPatttern.test(email)){
            frappe.throw('Please enter a valid Email.');
            frappe.validated = false; // Prevent form submission
        }
    }

});