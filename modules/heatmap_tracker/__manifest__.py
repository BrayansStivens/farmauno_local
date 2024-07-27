{
    'name': 'Heatmap Tracker',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Track user interactions on the website',
    'description': 'A module to track user interactions on the website and display heatmap data',
    'depends': ['base', 'web', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/heatmap_tracker_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'heatmap_tracker/static/src/js/heatmap_tracker.js',
        ],
    },
    'installable': True,
    'application': True,
}
