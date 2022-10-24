{
    'name': 'Popular Course Snippet',
    'version': '14.0.1.0.0',
    'summary': 'This module is for custom snippet',
    'description': """The purpose to create this module is generate a custom module in website snippet.""",

    'author': "Md Mazharul Islam",
    'website': "https://www.github.com/mazharulsabbir",

    'category': 'Tools',
    'depends': [
        'base',
        'web',
        'website',
        'website_slides',
    ],
    'data': [
        "views/assets.xml",
        "views/snippet.xml",
        "views/top_course_snippet_template.xml",
        "views/course_card_inherit.xml",
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto-install': False,
    'license': 'LGPL-3',
    'contributors': [
        'Md Mazharul Islam',
    ],
}
