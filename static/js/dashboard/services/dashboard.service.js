/**
* Drive
* @namespace crowdsource.dashboard.services
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.dashboard.services')
    .factory('Dashboard', Dashboard);

  Dashboard.$inject = ['$cookies', '$http', '$q', '$location', 'HttpService'];

  /**
  * @namespace Dashboard
  * @returns {Factory}
  */

  function Dashboard($cookies, $http, $q, $location, HttpService) {
    /**
    * @name Dashboard
    * @desc The Factory to be returned
    */
    var Dashboard = {
      getTasksByStatus: getTasksByStatus
    };
    return Dashboard;

    function getTasksByStatus() {
      var settings = {
        url: '/api/task-worker/list_by_status/',
        method: 'GET'
      };
      return HttpService.doRequest(settings);
    }

    function getSavedTask(task_worker_id) {
      var settings = {
        url: '/api/task-worker/' + task_worker_id + '/retrieve_with_data_and_results/',
        method: 'GET',
        params: {
          id: task_worker_id
        }
      };
      return HttpService.doRequest(settings);
    }

    function dropSavedTask(task_id) {
      var settings = {
        url: '/api/task-worker/' + task_id + '/drop_saved_task/',
        method: 'DELETE'
      };
      return HttpService.doRequest(settings);
    }
  }
})();