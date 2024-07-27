/* modules\heatmap_tracker\static\src\js\heatmap_tracker.js */

odoo.define('heatmap_tracker.HeatmapTracker', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    function getIPAddress() {
        return new Promise(function(resolve, reject) {
            fetch('https://api.ipify.org?format=json')
                .then(response => response.json())
                .then(ipData => resolve(ipData.ip))
                .catch(error => reject(error));
        });
    }

    function getUserLocation(ip) {
        return new Promise(function(resolve, reject) {
            fetch('https://ipapi.co/' + ip + '/json/')
                .then(response => response.json())
                .then(locData => {
                    var location = locData.city + ', ' + locData.region + ', ' + locData.country_name;
                    resolve(location);
                })
                .catch(error => reject(error));
        });
    }

    $(document).ready(function () {
        var sessionData = {
            urls: window.location.href,
            user_agent: navigator.userAgent,
            click_counts: 0,
            hovered_elements: [],
            time_spent_on_page: [],
            time_spent_on_elements: {},
            page_names: document.title,
            ip_address: '',
            location: '',
            device_type: /Mobi|Android/i.test(navigator.userAgent) ? 'Mobile' : 'Desktop',
            click_elements: {}
        };

        var pageStartTime = performance.now();
        var hoverStartTimes = {};
        var pageVisible = true;

        getIPAddress().then(function(ip) {
            sessionData.ip_address = ip;
            return getUserLocation(ip);
        }).then(function(location) {
            sessionData.location = location;
        });

        $(document).on('click', function(event) {
            sessionData.click_counts++;
            var elementTag = event.target.tagName;
            var elementText = event.target.innerText || event.target.alt || event.target.src || '';
            var key = elementText || elementTag;

            if (!sessionData.click_elements[key]) {
                sessionData.click_elements[key] = 0;
            }
            sessionData.click_elements[key]++; // Increment click count on element
        });

        $(document).on('mouseover', function(event) {
            var elementTag = event.target.tagName;
            var elementText = event.target.innerText || event.target.alt || event.target.src || '';
            var key = elementText || elementTag;

            hoverStartTimes[key] = performance.now();

            if (!sessionData.hovered_elements.includes(key)) {
                sessionData.hovered_elements.push(key);
            }
        });

        $(document).on('mouseout', function(event) {
            var elementTag = event.target.tagName;
            var elementText = event.target.innerText || event.target.alt || event.target.src || '';
            var key = elementText || elementTag;

            var hoverEndTime = performance.now();
            var hoverTime = (hoverEndTime - hoverStartTimes[key]) / 1000; // Convert to seconds

            if (sessionData.time_spent_on_elements[key]) {
                sessionData.time_spent_on_elements[key] += hoverTime;
            } else {
                sessionData.time_spent_on_elements[key] = hoverTime;
            }
        });

        $(document).on('visibilitychange', function() {
            if (document.hidden) {
                pageVisible = false;
            } else {
                pageVisible = true;
            }
        });

        function sendSessionData() {
            if (pageVisible) {
                var pageEndTime = performance.now();
                var timeSpent = (pageEndTime - pageStartTime) / 1000; // Convert to seconds
                sessionData.time_spent_on_page.push(timeSpent);
                ajax.jsonRpc('/track_user_interaction', 'call', sessionData);
                pageStartTime = performance.now(); // Reset start time for next interval
            }
        }

        // Send session data every 30 seconds
        setInterval(sendSessionData, 30000);

        $(window).on('beforeunload', function() {
            sendSessionData();
        });
    });
});

