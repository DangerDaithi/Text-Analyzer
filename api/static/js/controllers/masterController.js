/**
 * masterController Controller
 * @namespace Controllers
 */
'use strict';

app.controller('masterController', masterController);

/**
   * @namespace masterController
   * @desc The Master/ root controller of the truth engine angular app
   * @memberOf Controllers
   */
function masterController(truthEngineApi) {
    var vm = this;


     /**
       * @name successCallback
       * @desc The successCallback handler, handles success call backs to API (e.g. 200)
       * @memberOf Controllers.masterController
       */
    function successCallback(){

    };

     /**
      * @name errorCallback
      * @desc The errorCallback handler, handles failed call backs to API (e.g. 500/ 400 server errors)
      * @memberOf Controllers.masterController
      */
    function errorCallback(error){
        console.log(error);
    };
};