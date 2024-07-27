#modules\heatmap_tracker\models\heatmap_tracker.py

from odoo import models, fields, api
import json

class HeatmapTracker(models.Model):
    _name = 'heatmap.tracker'
    _description = 'Heatmap Tracker'

    user_agent = fields.Char(string='User Agent')
    click_counts = fields.Integer(string='Total Click Counts')
    ip_address = fields.Char(string='IP Address')
    location = fields.Char(string='Location')
    device_type = fields.Char(string='Device Type')
    interaction_ids = fields.One2many('heatmap.interaction', 'tracker_id', string='Interactions')

class HeatmapInteraction(models.Model):
    _name = 'heatmap.interaction'
    _description = 'Heatmap Interaction'

    tracker_id = fields.Many2one('heatmap.tracker', string='Tracker')
    url = fields.Char(string='URL')
    page_name = fields.Char(string='Page Name')
    click_counts = fields.Integer(string='Click Counts')
    hovered_elements = fields.Text(string='Hovered Elements')
    time_spent_on_page = fields.Float(string='Time Spent on Page')
    time_spent_on_elements = fields.Text(string='Time Spent on Elements')
    click_elements = fields.Text(string='Click Elements')

    @api.model
    def create(self, vals):
        if 'hovered_elements' in vals:
            vals['hovered_elements'] = json.dumps(json.loads(vals['hovered_elements']), indent=4, sort_keys=True)
        if 'time_spent_on_elements' in vals:
            vals['time_spent_on_elements'] = json.dumps(json.loads(vals['time_spent_on_elements']), indent=4, sort_keys=True)
        if 'click_elements' in vals:
            vals['click_elements'] = json.dumps(json.loads(vals['click_elements']), indent=4, sort_keys=True)
        return super(HeatmapInteraction, self).create(vals)

    def write(self, vals):
        if 'hovered_elements' in vals:
            vals['hovered_elements'] = json.dumps(json.loads(vals['hovered_elements']), indent=4, sort_keys=True)
        if 'time_spent_on_elements' in vals:
            vals['time_spent_on_elements'] = json.dumps(json.loads(vals['time_spent_on_elements']), indent=4, sort_keys=True)
        if 'click_elements' in vals:
            vals['click_elements'] = json.dumps(json.loads(vals['click_elements']), indent=4, sort_keys=True)
        return super(HeatmapInteraction, self).write(vals)
