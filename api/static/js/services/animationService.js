/**
 * animation service
 * @namespace Services
 */

'use strict';

app.service('animationService', animationService);

/**
   * @namespace animationService
   * @desc Service module for adding animation effects to elements on view
   * @memberOf Services
   */

function animationService() {

      /**
       * @name addClass
       * @desc Adds a css class to an element
       * @param {String} id of the element
       * @param {String} the class to add to the element
       * @memberOf Services.animationService
       */
    this.addClass = function(id, classToAdd){
        var div = angular.element( document.querySelector( '#' + id ) );
        div.addClass('animate ' + classToAdd);
    };

      /**
       * @name removeClass
       * @desc Removes a css class from an element
       * @param {String} id of the element
       * @param {String} the class to remove from the element
       * @memberOf Services.animationService
       */
    this.removeClass = function(id, classToRemove){
        var div = angular.element( document.querySelector( '#' + id ) );
        div.removeClass(classToRemove);
    };
};