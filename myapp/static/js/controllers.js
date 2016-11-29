angular.module("myApp")
    .controller("mainController",
    [
        "$scope", "$http", function($scope, $http) {
            $scope.searchCity = function($event){
                $event.preventDefault();

                $http({
                    method: 'POST',
                    url: '/myapp/',
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                    transformRequest: function(obj) {
                        var str = [];
                        str.push(encodeURIComponent('city') + "=" + encodeURIComponent($scope.city));
                        return str.join("&");
                    },
                    data: {username: $scope.userName, password: $scope.password}
                })
                .then(
                function(response){
                    $scope.result = response.data['info'];
                    // $scope.wind = $scope.result['info']['wind'];
                    // $scope.t_day = $scope.result['info']['t_day'];
                    // $scope.longitude = $scope.result['info']['longitude'];
                    // $scope.latitude = $scope.result['info']['longitude'];
                    // $scope.t_night = $scope.result['info']['t_night'];
                    // $scope.description = $scope.result['info']['description'];
                    // $scope.t_min = $scope.result['info']['t_min'];
                    // $scope.time = $scope.result['info']['time'];
                    // $scope.pressure = $scope.result['info']['pressure'];
                    // $scope.t_max = $scope.result['info']['t_max'];
                    // $scope.city = $scope.result['info']['city'];
                    // $scope.clouds = $scope.result['info']['clouds'];
                    //
                    // console.log($scope.result['info']['wind']);
                },
                function(response){
                    alert('Error');
                    console.log(response);
                });
            };
        }
    ]);