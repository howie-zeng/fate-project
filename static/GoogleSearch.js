
// Global Variable
var index = 0;
var responseData;
var userResponse = "";
var startTime;
var endTime;
var timeRemaining;
var choice = 4;
var count = 0;

 (function() {
   "use strict";

   let timerId = null;
   let set = "";
   let timerMode = false;
   let seconds = 20;
   let seen = [];
   let timeSpent = 20;
   let numQuestions = 40;
   const ALGORITHM = new Array("0g", "03gfp", "05gfp", "09gfp");

   window.addEventListener("load", init);

   function init() {
     let submitButton = document.querySelector(".submit");
     submitButton.disabled = true;
     submitButton.addEventListener("click", submit_form);
     let ratingButton = document.getElementsByName("rating");
     for (let i = 0; i < ratingButton.length; i++) {
       ratingButton[i].addEventListener("click", chooseRating);
     }
     generateRandom();
     fillColumn();
   }

   function generateRandom() {
     let randomCount = Math.floor(Math.random() * ALGORITHM.length);
     if (seen.includes(randomCount) && seen.length != 4) {
       generateRandom();
     } else {
       if (seen.length != 4) {
         seen.push(randomCount);
         set = ALGORITHM[randomCount];
         if (set == "0g" || set == "03gfp") {
           index = 0;
         } else {
           index = 10;
         }
       }
     }
   }

   function updateResults() {
     index++;
     count++;
     if (count == 11 || count == 21 || count == 31) {
       generateRandom();
       index++;
     }
     if (index <= 10 || (index > 10 && index <= 20)) {
       populateResults();
     }
     if (count == 41) {
       window.location = window.location + "end/" + userResponse.trim();
     }
   }

   function startTimer() {
     timerId = setInterval(function() {
       if (seconds == 0) {
         clearInterval(timerId);
         timerId = null;
         seconds = 20;
         timeSpent = 20;
         let questionCounter = document.getElementById("questions");
         numQuestions--;
         questionCounter.innerHTML = " " + numQuestions;
         let searchEngine = document.getElementById("search-word");
         let searchEngineValue = searchEngine.value.replace(/\s/g, "");
         userResponse += set + " " + searchEngineValue + " -1 " + timeSpent + " ";
         document.querySelector(".submit").disabled = true;
         var rate = document.getElementsByName('rating');
         for(var i=1; i<rate.length; i++) {
             if (rate[i].checked) {
                 rate[i].checked = false;
             }
         }
         updateResults();
       } else {
         timerMode = true;
         seconds--;
         chooseRating();3
       }
       let time = document.getElementById("clock");
       time.textContent = seconds;
     }, 1000)
   }

   function chooseRating() {
     var rate = document.getElementsByName('rating');
     for(var i=1; i<rate.length; i++) {
         if (rate[i].checked && seconds <= 18) {
           let submitButton = document.querySelector(".submit");
           submitButton.disabled = false;
         }
     }
     /*if (seconds <= 18 && ) {
       let submitButton = document.querySelector(".submit");
       submitButton.disabled = false;
     } */
   }

   function handleRequest(data) {
     responseData = data;
     updateResults();
   }

   function populateResults() {
     // update search box placeholder
     let searchEngine = document.getElementById("search-word");
     searchEngine.value = responseData[index][1][0];

     // display results, but clear all previous results first
     let resultInfo = document.querySelector(".resultInfo");
     resultInfo.innerHTML = "";
     for (let i = 0; i < 5; i++) {
       let title = document.createElement("a");
       let description = document.createElement("div");
       let link = document.createElement("div");
       title.className = "title";
       link.className = "url";
       description.className = "description";
       title.innerHTML = responseData[index][i][1];
       link.innerHTML = responseData[index][i][2];
       description.innerHTML = responseData[index][i][3];
       resultInfo.appendChild(title);
       resultInfo.appendChild(link);
       resultInfo.appendChild(description);
     }

     //start counting
     startTimer();
   }

  function fillColumn() {
    let column = document.querySelector(".resultInfo");
    column.innerHTML = "";
    let currentUrl = window.location.href;
    let url = currentUrl.substring(0, currentUrl.length - 5) + set + "/results/";
    fetch(url)
      .then(checkStatus)
      .then(JSON.parse)
      .then(handleRequest)
      .catch(console.error);
  }

  /**
    * Checks to see if the data that is being fetched can be used.
    * @param {string} response = JSON data that was fetched from the API
    * @return {string} Returns the data that fits the condition
  */
  function checkStatus(response) {
    if (response.status >= 200 && response.status < 300) {
      return response.text();
    } else {
      return Promise.reject(new Error(response.status + ": " +
      response.statusText));
    }
  }

  function submit_form() {
    let submitButton = document.querySelector(".submit");
    submitButton.disabled = true;
    let questionCounter = document.getElementById("questions");
    numQuestions--;
    questionCounter.innerHTML = " " + numQuestions;
    let searchEngine = document.getElementById("search-word");
    let searchEngineValue = searchEngine.value.replace(/\s/g, "");
    timeSpent = timeSpent - seconds;
    //console.log("time took:" + seconds)
    //return selected rating value
    var rate = document.getElementsByName('rating');
    for(var i=1; i<rate.length; i++){
        if(rate[i].checked){
            userResponse += set + " " + searchEngineValue + " " + i + " "+ timeSpent + " ";
            rate[i].checked = false;
        }
    }
    clearInterval(timerId)
    timerId = null;
    seconds = 20;
    timeSpent = 20;
    updateResults();
  }
})();
