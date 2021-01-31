'use strict';   

var app = angular.module('truthEngineApp', [
 'ui.router',
]);

app.config(function($stateProvider, $urlRouterProvider) {

   $urlRouterProvider.otherwise('/truthengine');

    $stateProvider

        .state('textAnalyze', {
            url: '/truthengine',
            templateUrl: '../static/templates/textAnalyze.html'
        })

        .state('analysisResults', {
            url: '/results',
            templateUrl: '../static/templates/textAnalysisResult.html'
        })

        .state('about', {
            url: '/about',
            templateUrl: '../static/templates/about.html'
        })

        .state('loading', {
            url: '/loading',
            templateUrl: '../static/templates/loading.html'
        })

        .state('error', {
            url: '/error',
            templateUrl: '../static/templates/error.html'
        })

        .state('404', {
            url: '/404',
            templateUrl: '/static/partials/404.html '
        });
});
