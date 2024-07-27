#modules\heatmap_tracker\controllers\controllers.py

from odoo import http
from odoo.http import request
import json

class HeatmapTracker(http.Controller):

    @http.route('/track_user_interaction', type='json', auth='public')
    def track_user_interaction(self, **kwargs):
        tracker_model = request.env['heatmap.tracker'].sudo()
        interaction_model = request.env['heatmap.interaction'].sudo()
        
        tracker = tracker_model.search([('ip_address', '=', kwargs.get('ip_address'))], limit=1)
        
        if not tracker:
            tracker = tracker_model.create({
                'user_agent': kwargs.get('user_agent'),
                'click_counts': kwargs.get('click_counts', 0),
                'ip_address': kwargs.get('ip_address'),
                'location': kwargs.get('location'),
                'device_type': kwargs.get('device_type'),
            })
        else:
            tracker.write({
                'click_counts': tracker.click_counts + kwargs.get('click_counts', 0),
            })

        interaction = interaction_model.search([
            ('tracker_id', '=', tracker.id),
            ('url', '=', kwargs.get('urls'))
        ], limit=1)

        if interaction:
            interaction.write({
                'click_counts': interaction.click_counts + kwargs.get('click_counts', 0),
                'hovered_elements': json.dumps(kwargs.get('hovered_elements')),
                'time_spent_on_page': sum(kwargs.get('time_spent_on_page', [])),
                'time_spent_on_elements': json.dumps(kwargs.get('time_spent_on_elements')),
                'click_elements': json.dumps(kwargs.get('click_elements')),
            })
        else:
            interaction_model.create({
                'tracker_id': tracker.id,
                'url': kwargs.get('urls'),
                'page_name': kwargs.get('page_names'),
                'click_counts': kwargs.get('click_counts', 0),
                'hovered_elements': json.dumps(kwargs.get('hovered_elements')),
                'time_spent_on_page': sum(kwargs.get('time_spent_on_page', [])),
                'time_spent_on_elements': json.dumps(kwargs.get('time_spent_on_elements')),
                'click_elements': json.dumps(kwargs.get('click_elements')),
            })

        return {'status': 'success'}
