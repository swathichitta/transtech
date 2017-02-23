from openerp.osv import fields, osv
import datetime


class Site_inspection(osv.osv):

	_name = 'site.inspection'

	_columns={
		'name':fields.char('Inspection ID'),
        'site_type':fields.selection([('ttw','TTW'),
								    ('lobby', 'LOBBY'),
								    ('other', 'Other'),
								    ('walkup', 'Walk UP'),
								    ('driveup', 'Drive UP')], 'Site Type'),
        'surveyor':fields.many2one('res.users','Site Inspector Name'),
		'date_assigned':fields.datetime('Date Assigned'),
		'date_of_visit':fields.datetime('Date of Visit'),
		'customer':fields.many2one('customer.info','Customer Name'),
		'site_address':fields.text("Site Address"),
		'site_lat':fields.char("Latitude"),
		'site_long':fields.char("Longitute"),
		'contact_person':fields.char("Contact Person Name"),
		'contact_mobile':fields.char("Mobile Number"),
		'job_description':fields.text("Job Description"),
		'atm_brand':fields.char("ATM Brand/Model/Class"),
		'access_for_truck':fields.selection([('yes','Yes'),
											 ('no','No')],"Access For Truck"),
		'access_for_truck_crane':fields.selection([('yes','Yes'),
												   ('no','No')],"Access For Truck with Crane"),
		'hole_inside_height':fields.char("Hole Height from inside"),
		'inside_outside':fields.char("Hole Height from inside"),
		'hole_height':fields.char("Hole Height from Customer standing area"),
		'hole_height_outside':fields.char("Hole height from Outside"),
		
	}

	def create(self, cr, uid, vals, context=None):
   		vals['name']= self.pool.get('ir.sequence').get(cr, uid, 'site.insp')
   		return super(Site_inspection, self).create(cr, uid, vals, context=context)

Site_inspection()