from openerp.osv import fields, osv
import datetime
import time


class Survey_Details(osv.osv):

	_name = 'survey.details'


	def _check_customer(self, cr, uid, ids, name, args, context=None):

		result = {}

		groups_id = self.pool.get('res.users').read(cr, uid, uid)['groups_id']
		for obj in self.browse(cr, uid, ids):
			if len(groups_id) == 1:
				c_name = self.pool.get('res.users').read(cr, uid, uid)['name']
				if 'NBAD' in c_name:
					result[obj.id] = True

				else:
					result[obj.id] = False
			else:
				result[obj.id] = True

		return result


	_columns = {
		"name": fields.char("Survey id"),
		"surv_task": fields.many2one("atm.surverys.management", 'ATM Report Task ID'),
		'state': fields.many2one('res.country.state', 'State'),
		'month': fields.selection([('jan', 'January'),
									('feb', 'February'),
									('mar', 'March'),
									('apr', 'April'),
									('may', 'May'),
									('june', 'June'),
									('jul', 'July'),
									('aug', 'August'),
									('sep', 'September'),
									('oct', 'October'),
									('nov', 'November'),
									('dec', 'December')], 'Month'),
		'atm_surv': fields.many2one('atm.info', 'ATM'),
		'customer_surv': fields.many2one('customer.info', 'Customer'),
		'surveyor_surv': fields.many2one('res.users', 'Surveyor'),
		'remarks_survey': fields.many2one('remarks.category', 'Remarks Category'),
		'visit_tm': fields.datetime('Visit Time'),
		'bfr_img_front': fields.binary('Front View'),
		'bfr_img_side': fields.binary('Side View'),
		'bfr_img_back': fields.binary('Back View'),
		'after_img_front': fields.binary('Front View After'),
		'after_img_side': fields.binary('Side View After'),
		'after_img_back': fields.binary('Back View After'),

		'bfr_img_front2': fields.binary('Front View 2'),
		'bfr_img_side2': fields.binary('Side View 2'),
		'bfr_img_back2': fields.binary('Back View 2'),
		'after_img_front2': fields.binary('Front View After 2'),
		'after_img_side2': fields.binary('Side View After 2'),
		'after_img_back2': fields.binary('Back View After 2'),


		'bfr_img_front3': fields.binary('Front View 3'),
		'bfr_img_side3': fields.binary('Front View Side 3'),
		'after_img_front3': fields.binary('Front View After 3'),
		'after_img_side3': fields.binary('Side View After 3'),



		'check_list1': fields.boolean('No Comments'),
		'check_list3': fields.selection([('required', 'Required'),
										 ('damaged', 'Damaged'),
										 ('replaced', 'Replaced')], 'Collect Cash'),

		'check_list4': fields.selection([('required', 'Required'),
										 ('damaged', 'Damaged'),
										 ('replaced', 'Replaced')], 'Collect Receipt'),

		'insert_chq': fields.selection([('required', 'Required'),
										('damaged', 'Damaged'),
										('replaced', 'Replaced')], 'Insert Cheque'),

		'check_list5': fields.selection([('required', 'Required'),
										 ('damaged', 'Damaged'),
										 ('replaced', 'Replaced')], 'Insert Card'),

		'check_list6': fields.selection([('required', 'Required'),
										 ('damaged', 'Damaged'),
										 ('replaced', 'Replaced')], 'Insert Cash'),

		'check_list7': fields.selection([('required', 'Required'),
										 ('damaged', 'Damaged'),
										 ('replaced', 'Replaced')], 'Network Sticker'),

		'check_list8': fields.selection([('required', 'Required'),
										 ('damaged', 'Damaged'),
										 ('replaced', 'Replaced')], 'Instruction Sticker'),

		'check_list9': fields.selection([('required', 'Required'),
										 ('damaged', 'Damaged'),
										 ('replaced', 'Replaced')], 'Vault Branding'),

		'check_list10': fields.selection([('required', 'Required'),
										  ('damaged', 'Damaged'),
										  ('replaced', 'Replaced')], 'Terminal ID'),

		'check_list11': fields.selection([('required', 'Required'),
										  ('completed', 'Completed')], 'Cables Securing'),

		'check_list13': fields.selection([('required', 'Required'),], 'Trash bin Keys'),

		'check_list15': fields.selection([('required', 'Required')], 'Machine Surround Maintenance'),
		'check_list17': fields.selection([('off', 'Off'),
										  ('replaced', 'Replaced')], 'Spot Lights'),

		'check_list19': fields.selection([('damaged', 'Damaged')], 'Machine Surround Branding'),

		'check_list20': fields.selection([('damaged', 'Damaged')], 'Canopy branding'),

		'check_list21': fields.selection([('n/w_box_lock_damaged', 'Network Box Lock Damaged'),
										  ('vault_lock_damaged','Vault Lock Damaged'),
										  ('lock_repaired', 'Lock Repaired')], 'Surround Locks'),

		'check_list23': fields.selection([('off', 'Off'),
										  ('on', 'on')], 'Main board Lights'),

		'check_list25': fields.selection([('exposed', 'Exposed')], 'Security Camera Cables'),
		'check_list26': fields.selection([('yes', 'Yes'),
										  ('no', 'No')], 'Outdated Contact no on the Surround'),
		'check_list28': fields.selection([('open', 'Open'),
										  ('damaged', 'Damaged')], 'ATM Vault Door'),

		'check_list29': fields.selection([('required', 'Required'),
										  ('damaged', 'Damaged'),
										  ('replaced', 'Replaced')], 'DED Number'),

		'check_list27': fields.selection([('required', 'Required'),
										  ('damaged', 'Damaged'),
										  ('replaced', 'Replaced')], 'Card Reader'),

		'side_frames': fields.selection([('required', 'Required'),
										 ('damaged', 'Damaged'),
										 ('replaced', 'Replaced')], 'Side Frames/Posters on the Surround'),

		'black_notices': fields.selection([('required', 'Required'),
										   ('damaged', 'Damaged'),
										   ('replaced', 'Replaced'),], 'ATM Notices'),

		'keypad_condition': fields.selection([('displaced', 'Displaced'),
											  ('damaged', 'Damaged'),
											  ('faded', 'Number Faded'),
											  ('pinguard_damaged','Pinguard Damaged'),], 'Keypad Condition'),

		'ttw_branding': fields.selection([('damaged', 'Damaged'),
										  ], 'TTW Branding'),

		'scree_protector': fields.selection([('damaged', 'Damaged'),
											 ], 'ATM Screen Protector'),

		'trash_bin_repairs': fields.selection([('required', 'Required'),
											   ('damaged', 'Damaged'),
											   ('replaced', 'Replaced'),], 'Trash Bin repairs/ replacement to be completed ( as per the agreed contract)'),

		'protective_box': fields.selection([('required', 'Required'),
											('damaged', 'Damaged'),
											('replaced', 'Replaced')], 'Protective Box for Power Circuit'),

		'atm_status': fields.selection([('offline', 'Offline'),
										('off', 'Powered Off')], 'ATM Status'),

		'machine_security_camera': fields.selection([('glass_missing', 'Glass Missing'),
													 ('glass_broken','Glass Broken'),
													 ('out_of_focus','Out of Focus')], 'Machine Security Camera'),

		'fascia_condition': fields.selection([('faded_edges', 'Faded from Edges'),
											  ('faded_keypad','Faded from Keypad')], 'Fascia Condition'),

		# Branding Audit Check List sheet-1

		'dl_brochure_holder': fields.selection([('updated_inventory', ' Updated inventory available'),
												('outdated_inventory','Outdated inventory available'),
												('low_inventory','Low inventory - To be ordered')], 'DL Brochure Holder'),

		'brochure_holder_19x19': fields.selection([('updated_inventory', ' Updated inventory available'),
												   ('outdated_inventory','Outdated inventory available'),
												   ('low_inventory','Low inventory - To be ordered')], 'Brochure holder - 19 x 19'),

		'application_form': fields.selection([('updated_inventory', ' Updated inventory available'),
											  ('outdated_inventory','Outdated inventory available'),
											  ('low_inventory','Low inventory - To be ordered'),], 'Application form'),

		'poster_frames': fields.selection([('current_compaign', 'Current campaigns available'),
										   ('outdated', 'Outdated/old available - Reported')],'Poster Frames'),
		'internal_window_graphics': fields.selection([('current_compaign', 'Current campaigns available'), 
													('outdated', 'Outdated/old available - Reported')], 'Internal window graphics'),

		'advertising_stands': fields.selection([('current_compaign', 'Current campaigns available'), ('outdated', 'Outdated/old available - Reported')], 'Advertising stands'),
		'push/pull_stickers': fields.selection([('running', 'In running condition'),
												('req_replacement','Require replacement'),
												('missing', 'Missing'),], 'Push/Pull stickers'),

		'stationary_calendars': fields.selection([('updated_inventory', ' Updated inventory available'),
												  ('outdated_inventory','Outdated inventory available'),
												  ('low_inventory','Low inventory - To be ordered'),], 'Stationary - Calendars, annual reports, tissue boxes'),

		'store_inventory_cur_campaigns': fields.selection([('updated_inventory', ' Updated inventory available'),
														   ('outdated_inventory','Outdated inventory available'),
														   ('low_inventory','Low inventory - To be ordered'),], 'Store inventory - Current campaigns'),

		'led_screen_ad': fields.selection([('current_compaign', 'Current campaigns available'), ('outdated', 'Outdated/old available - Reported')], 'LED Screen advertisement'),
		'palm_leaf_strip_sticker': fields.selection([('running', 'In running condition'),
													 ('req_replacement','Require replacement'),
													 ('missing', 'Missing'),], 'Palm Leaf Strip Sticker'),
		'branding_conditions': fields.selection([('running', 'In running condition'),
												 ('req_replacement','Require replacement'),
												 ('missing', 'Missing'),], 'Branding condition (internal) -  Dusty/faded colors/torn'),
		'led_conditions': fields.selection([('running_updated_campaign', 'Running with updated campaigns'),
											('damaged', 'Not working/Damaged'),
											('running_outdated_campaign','Running with outdated campaigns'),], 'LED screen condition - Report in case damaged or not running'),

		'external_br_condition': fields.selection([('running', 'In running condition'),
												   ('req_replacement','Require replacement'),
												   ('missing', 'Missing'),], 'External branch branding condition'),

		'onsite_atm_branding': fields.selection([('running', 'In running condition'),
												 ('req_replacement','Require replacement'),
												 ('missing', 'Missing'),], 'Branding of on-site ATM'),

		'personal_loan_compaign': fields.selection([('available', 'Available'),
													('outdated','Not available/Outdated'),], 'Personal Loan Campaign'),

		'real_madrid_compaign': fields.selection([('available', 'Available'),
												  ('outdated','Not available/Outdated'),], 'Real-madrid Campaign'),
		'mobile_app_campaign': fields.selection([('available', 'Available'),
												 ('outdated','Not available/Outdated'),], 'Mobile App Campaign'),
		'mortgage_loan_campaign': fields.selection([('available', 'Available'),
													('outdated','Not available/Outdated'),], 'Mortgage Loan Campaign'),
		'other_compaign': fields.selection([('available', 'Available'),
											('outdated','Not available/Outdated'),], 'Any other campaign except ML,PL, RM & Mobile app'),
		'cur_longitude': fields.char('Current Longitude'),
		'cur_latitude': fields.char('Current Latitude'),
		'nxt_survey_distance': fields.integer('Next Survey Distance'),
		'nxt_taskid': fields.many2one('atm.surverys.management', 'Next Task ID'),
		'visits_done': fields.integer('Visits Done'),
		'visits_left': fields.integer('Visits Left'),
		'total_visits': fields.integer('Total Visits'),
		'status': fields.selection([('waiting_approval', 'Waiting for Approval'),
									('approved', 'Approved')], 'Status'),

		'is_nbad': fields.function(_check_customer, type='boolean', string='Is NBAD', method=True, store=False, multi=False),

		'card_pic': fields.selection([('required', 'Required'),
									('damaged', 'Damaged'),
									('replaced', 'Replaced')], 'Card Picture'),
		'trans_rec': fields.selection([('nt_avail', 'Not Available')], 'Transaction Receipt'),
		'dd_sticker': fields.selection([('required', 'Required'),
									('damaged', 'Damaged'),
									('replaced', 'Replaced')], "Do's and Don'ts sticker"),
		'cash_deposit': fields.selection([('nt_wrkng', 'Not Working')],  'Cash Deposit'),
		'screen_errors': fields.selection([('touch', 'Touch function not working'),
									('display', 'Display Distorted')], 'Touch Screen Errors'),
		'screeen': fields.selection([('blank', 'Blank'),
									('frozen', 'Frozen')], 'Screen'),
		'ac_issues': fields.selection([('nt_wrkng', 'Not Working')], 'AC Issues'),
		'pin_guard': fields.selection([('required', 'Required'),
									('damaged', 'Damaged')], 'Pin Guard'),
		'privacy_flap': fields.selection([('required', 'Required'),
									('damaged', 'Damaged')], 'Privacy Flap'),
		'kiosk_door': fields.selection([('open', 'Open'),
									('damaged', 'Damaged')], 'Kiosk Door'),
		'kiosk_lights': fields.selection([('off', 'Off'),
									('left', 'Left Off'),
									('top', 'Top Off'),
									('right', 'Right Off')], 'Kiosk Lights'),
		'fascia_light': fields.selection([('off', 'Off'),
										('replaced', 'Replaced'),
										('missing', 'Missing')], 'Fascia Light'),
		'boom_sign': fields.selection([('off', 'Off'),
										('replaced', 'Replaced'),
										('damaged', 'Damaged')], 'Boom Sign'),
	}

	_defaults = {
		'status': 'waiting_approval',
		'visit_tm': lambda * a: time.strftime('%Y-%m-%d %H:%M:%S'),
	}

	def create(self, cr, uid, vals, context=None):
   		vals['name']= self.pool.get('ir.sequence').get(cr, uid, 'survey.det')
   		return super(Survey_Details, self).create(cr, uid, vals, context=context)

   	def status_approve(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'status':'approved'},context=context)
		return True
		
	def onchange_taskid(self, cr, uid, ids, surv_task, context=None):
		res = {'value': {}}
		if surv_task:
			part = self.pool.get('atm.surverys.management').browse(cr, uid, surv_task, context)
			# print part.atm.id
			res['value'].update({'month': part.task_month})
			res['value'].update({'atm_surv': part.atm.id})
			res['value'].update({'surveyor_surv': part.surveyor.id})

			res['value'].update({'customer_surv': part.customer.id})
			res['value'].update({'visit_tm': part.visit_time})
			res['value'].update({'state': part.state.id})

		return res
Survey_Details()