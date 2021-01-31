/**
 * textAnalyzer Controller
 * @namespace Controllers
 */
'use strict';
app.controller('textAnalyzerController', textAnalyzerController);

/**
   * @namespace textAnalyzerController
   * @desc The textAnalyzer controller of the truth engine angular app
   * @memberOf Controllers
   */
function textAnalyzerController(truthEngineApi, $state, animationService, $timeout) {
    var vm = this;
    vm.text = "";
    vm.analysisResults = {};

     /**
       * @name getResourceText
       * @desc Calls the truthEngineApi factory to get the specified resource text
       * @param resource, the specified resource to get
       * @memberOf Controllers.textAnalyzerController
       */
    vm.getResourceText = function (resource)
    {
        if(resource === undefined)
        {
            return;
        }
        truthEngineApi.getResourceText(resource).then(resourceSuccessCallback, errorCallback);
    };


     /**
       * @name resourceSuccessCallback
       * @desc The resourceSuccessCallback handler, handles success call backs from API (e.g. 200)
       * @memberOf Controllers.textAnalyzerController
       */
    function resourceSuccessCallback(api){
         vm.text = api.data;
         animationService.addClass('textInput', 'animated tada');
    };


     /**
       * @name analyzeText
       * @desc Calls the truthEngineApi factory to get a user
       * @memberOf Controllers.textAnalyzerController
       */
    vm.analyzeText = function() {
        if(vm.text.length !== 0)
        {
            animationService.removeClass('textAnalyze', 'fadeInRight');
            animationService.addClass('textAnalyze', 'zoomOutLeft');
            animationService.removeClass('buttons', 'bounceInUp');
            animationService.addClass('buttons', 'bounceOutDown');

            // wait for animation to finish
            $timeout(function() {
                truthEngineApi.getTopTerms(vm.text).then(successCallback, errorCallback);
                // transition to the loading state
                $state.go('loading');
            }, 1000);
        }
        else
        {
            console.log('Text length is empty!');
        }
    };

     /**
       * @name successCallback
       * @desc The successCallback handler, handles success call backs to API (e.g. 200)
       * @memberOf Controllers.textAnalyzerController
       */
    function successCallback(api){
         vm.analysisResults = api.data;
         $state.go('analysisResults');
    };

     /**
      * @name errorCallback
      * @desc The errorCallback handler, handles failed call backs to API (e.g. 500 server errors)
      * @memberOf Controllers.textAnalyzerController
      */
    function errorCallback(error){

        animationService.addClass('loading', 'hinge');

        // wait for hinge animation to finish
        $timeout(function() {
              $state.go('error');
        }, 5000);

        console.log(error);
    };
};