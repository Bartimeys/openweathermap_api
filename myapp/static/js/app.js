"use strict";

angular.module("myApp", [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('@@');
    $interpolateProvider.endSymbol('@@');
})
.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);