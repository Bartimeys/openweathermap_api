angular.module("myApp")
    .directive('hcChart', function () {
        return {
            restrict: 'E',
            template: '<div></div>',
            scope: {
                options: '='
            },
            link: function (scope, element) {
                Highcharts.chart(element[0], scope.options);
            }
        };
    })
    // Directive for pie charts, pass in title and data only
    .directive('hcPieChart', function () {
        return {
            restrict: 'E',
            template: '<div></div>',
            scope: {
                title: '@',
                data: '='
            },
            link: function (scope, element) {
                Highcharts.chart(element[0], {
                    chart: {
                        type: 'pie'
                    },
                    title: {
                        text: scope.title
                    },
                    plotOptions: {
                        pie: {
                            allowPointSelect: true,
                            cursor: 'pointer',
                            dataLabels: {
                                enabled: true,
                                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                            }
                        }
                    },
                    series: [{
                        data: scope.data
                    }]
                });
            }
        };
    })
    .controller("mainController",
        [
            "$scope", "$http", function ($scope, $http) {
            /*start pagination*/

            /*end pagination*/

            /*start opemweathermap parsing data*/
            $scope.searchCity = function ($event) {
                $event.preventDefault();

                $http({
                    method: 'POST',
                    url: '/myapp/',
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                    transformRequest: function (obj) {
                        var str = [];
                        str.push(encodeURIComponent('city') + "=" + encodeURIComponent($scope.city));
                        return str.join("&");
                    },
                    data: {username: $scope.userName, password: $scope.password}
                })
                    .then(
                        function (response) {

                            $scope.result = response.data;

                            // console.log($scope.time, $scope.wind, $scope.temperature_day, $scope.longitude, $scope.latitude,
                            //     $scope.temperature_night, $scope.description, $scope.temperature_min, $scope.pressure,
                            //     $scope.temperature_max, $scope.city, $scope.cloudiness);
                        },
                        function (response) {
                            alert('Error');
                            console.log(response);
                        });
            };
            /*end of working with api*/


            /*get data frpm sqlite*/
            $scope.customerTable = [];
            $scope.getTable = function () {
                $http({
                    url: "/pressure-data/",
                    headers: {'Content-Type': 'application/json'},
                    metdod: 'GET'
                }).success(function (data) {
                    $scope.customerTable = data;
                    for (var key in $scope.customerTable) {
                        $scope.time = $scope.customerTable[key]['time'];
                        $scope.name = $scope.customerTable[key]['name'];
                        $scope.pressure = $scope.customerTable[key]['pressure'];
                        $scope.pressurechart = $scope.pressure
                    }

                }).error(function (response) {
                    alert({
                        title: "Attention",
                        text: response.message.text,
                        type: response.message.type
                    });
                });
            };
            /*end of code that get data from table*/

            /*hightchart options*/
            // Sample options for first chart
            $scope.chartOptions = {
                title: {
                    text: 'Temperature data'
                },
                xAxis: {
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                },

                series: [{
                    data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
                }]
            };

            // Sample data for pie chart
            $scope.pieData = [{
                name: "Microsoft Internet Explorer",
                y: 56.33
            }, {
                name: "Chrome",
                y: 24.03,
                sliced: true,
                selected: true
            }, {
                name: "Firefox",
                y: 10.38
            }, {
                name: "Safari",
                y: 4.77
            }, {
                name: "Opera",
                y: 0.91
            }, {
                name: "Proprietary or Undetectable",
                y: 0.2
            }]
        }
        ]);