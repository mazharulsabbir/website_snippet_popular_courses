// this class will handle the data fetching from the server

odoo.define('course_attendees.website_popular_course', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.dynamic_modules = publicWidget.Widget.extend({
        selector: '.s_website_popular_course_section',
        disabledInEditableMode: false,
        start: function () {
            var self = this;
            if (!this.editableMode) {
                this._rpc({
                    route: '/popular_courses',
                }).then((data) => {
                    self.$target.empty().append(data);
                })
            }
        },
    });
});