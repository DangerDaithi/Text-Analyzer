/**
 * truthEngineApi Factory
 * @namespace Factories
 */

'use strict';

app.factory('truthEngineApi', truthEngineApi);

/**
   * @namespace truthEngineApi
   * @desc Service module for making http calls to truth engine API
   * @memberOf Factories
   */
function truthEngineApi($http) {
    /*Factory fields and methods*/
    var apiBaseUrl = 'http://127.0.0.1:5000/'; // private
    var truthEngineApiFactory = {
        getUser: getUser,
        getTopTerms: getTopTerms,
        getResourceText: getResourceText
    };
    return truthEngineApiFactory;

    ////////////

      /**
       * @name getUser
       * @desc Makes a http get request to get a User object from the API
       * @memberOf Factories.truthEngineApi
       * @returns call back containing requested User
       */
    function getUser() {
        var config = {
         headers : {'Accept' : 'application/json'}
        };
        return $http.get(apiBaseUrl + 'user', config);
    };

     /**
       * @name getTopTerms
       * @desc Makes a http post request to get top terms
       * @memberOf Factories.truthEngineApi
       * @returns call back containing top terms
       */
    function getTopTerms(text) {
        var config = {
         headers : {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        };

        var data = JSON.stringify(text);
        return $http.post(apiBaseUrl + 'analyze', data, config);
    };

     /**
       * @name getTopTerms
       * @desc Makes a http post request to get top terms
       * @memberOf Factories.truthEngineApi
       * @returns call back containing top terms
       */
    function getResourceText(resource){
        var config = {
         headers : {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
        };
        var data = JSON.stringify(resource);
        return $http.post(apiBaseUrl + 'textResource', data, config);
    };
};