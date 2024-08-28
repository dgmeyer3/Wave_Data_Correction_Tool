// Please see documentation at https://learn.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

function routeToSpot(){
    document.getElementById("spot-dropdown").classList.toggle("show");
}

window.onclick = function(event) {
    
    if (!event.target.matches('.btn')) {
      var unhiddenElements = document.getElementsByClassName("dropdown-content");
      var i;
      
      for (i = 0; i < unhiddenElements.length; i++) {
       
        var openDiv = unhiddenElements[i];
        if (openDiv.classList.contains('show')) {
          openDiv.classList.remove('show');
        }
      }
    }
  } 