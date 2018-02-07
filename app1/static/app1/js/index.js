
var app1 = angular.module('app1',['ngMaterial','ngResource','ngMessages']);

app1.controller('forumController', function($http){
    var self = this;

    self.onProceed = function(){
        $http({
        url : '/api/app1/user/',
        method: 'POST',
        data : {
                    "firstName": self.firstName,
                    "lastName": self.lastName,
                    "emailId": self.emailId,
                    "number": self.mobileNum,
                    "age": self.age
                }
        }).then(function(response){
            console.log(JSON.stringify(response.data));
            window.location = response.data['url'];
        }, function(response){
            console.log(JSON.stringify(response.data));
        })
    }
});

app1.controller('eligibleController', function(){
    var self = this;

    self.onBack = function(){
        window.location = '/app1/'
    }
});

app1.controller('notEligibleController', function(){
    var self = this;

    self.onBack = function(){
        window.location = '/app1/'
    }
});