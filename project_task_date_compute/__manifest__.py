# Copyright 2024 Unai Beristain - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Compute Task Start and End Dates",
    "summary": "Module to compute task start and end dates based on time entries and stage",
    "website": "https://github.com/avanzosc/project-addons",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "version": "14.0.1.0.0",
    "depends": ["base", "project", "hr_timesheet"],
    "data": [
        "views/project_task_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
