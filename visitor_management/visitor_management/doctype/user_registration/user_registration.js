// Copyright (c) 2023, Tejal KUmbhar and contributors
// For license information, please see license.txt

frappe.ui.form.on('User Registration', {
	refresh: function(frm) {
		frm.set_df_property('gst_or_pan', 'reqd', 1);
        frm.set_df_property('gst', 'reqd', frm.doc.gst_or_pan === 'GST');
        frm.set_df_property('pan', 'reqd', frm.doc.gst_or_pan === 'PAN');

	},

	gst_or_pan: function(frm) {
        // Handle changes in the "gst_or_pan" field
        frm.set_df_property('gst', 'reqd', frm.doc.gst_or_pan === 'GST');
        frm.set_df_property('pan', 'reqd', frm.doc.gst_or_pan === 'PAN');
    },

    // validate: function(frm) {
     
    //     var mobile = frm.doc.mobile;

        
    //     var indianMobilePattern = /^[789]\d{9}$/;

    //     if (!indianMobilePattern.test(mobile)) {
    //         frappe.throw('Please enter a valid Indian mobile number.');
    //         frappe.validated = false; // Prevent form submission
    //     }
    // }
   
});


frappe.ui.form.on('User Registration', {
    validate: function(frm) {
        
        var email = frm.doc.email;

       
        var EmailPatttern = /^[\w\.-]+@[\w\.-]+\.\w+$/

        if (!EmailPatttern.test(email)){
            frappe.throw('Please enter a valid Email.');
            frappe.validated = false; // Prevent form submission
        }
    }

});

frappe.ui.form.on('User Registration', {
    validate: function(frm) {
        
        var gst = frm.doc.gst;

      
        var GSTPatttern = /^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d{1}[Z]{1}[A-Z\d]{1}$/

       if (!GSTPatttern.test(gst)){
            frappe.throw('Please enter a valid GST.');
            frappe.validated = false; // Prevent form submission
        }
    }

});