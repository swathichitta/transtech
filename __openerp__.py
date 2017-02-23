# description about module 

{
    "name": "ATM Survey Management",
    "author": "ehapi Technologies",
    "version": "1.0",
    'author': 'ehapi',
    'description': """Transtech ATM Survey Management Module""", 
	"category" : "Tools",
	"depends" : ['base','mail'],
	"demo_xml" : [], 
	"data" : [		
				"security/transtech_security_view.xml",
				"security/ir.model.access.csv",
					
				"sequence/sequence.xml",

				"wizard/survey_report_view.xml",
				"wizard/upload_images_view.xml",
				"wizard/atm_move_view.xml",
				"wizard/surveys_approve_view.xml",

				"views/template_view.xml",
				"views/tasks_inqueue_view.xml",
				"views/alerts_foru_view.xml",
				"views/tasks_status_view.xml",
				"views/customer_details_view.xml",
				"views/atm_details_view.xml",
				"views/site_inspection_view.xml",
				"views/survey_details_view.xml",	
				"views/schedule_tasks_view.xml",
				"views/plan_tasks_view.xml",
				"views/customer_alerts_view.xml",
				"views/internal_alerts_view.xml",
				"views/public_holidays_view.xml",
				"views/state_setup_view.xml",
				"views/reason_code_setup_view.xml",
				"views/manage_remark_category_view.xml",

			],

	'auto_install': False,
    'application': True, 
	"installable": True,
}
