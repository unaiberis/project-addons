from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    start_date = fields.Date(
        string="Start Date", compute="_compute_start_date", store=True
    )
    end_date = fields.Date(string="End Date", compute="_compute_end_date", store=True)

    @api.depends("timesheet_ids.date")
    def _compute_start_date(self):
        for task in self:
            task.start_date = min(task.timesheet_ids.mapped("date"), default=False)

    @api.depends("timesheet_ids.date", "stage_id")
    def _compute_end_date(self):
        for task in self:
            if task.stage_id.fold:
                task.end_date = max(task.timesheet_ids.mapped("date"), default=False)
            else:
                task.end_date = False
