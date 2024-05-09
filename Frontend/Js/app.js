function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; 
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; 
  }

  function getResaleValue() {
    var uiResale = document.getElementsByName("uiResale");
    for(var i in uiResale) {
        if(uiResale[i].checked) {
            return parseInt(uiResale[i].value);
        }
    }
    return -1; // Invalid Value
 }

  

  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_home_price"; 
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    },function(data, status) {
        
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }

  function onClickedEstimatePrice1() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var carparking = getBathValue();
    var location = document.getElementById("uiLocations1");
    var estPrice = document.getElementById("uiEstimatedPrice1");

    
    var url1= "http://127.0.0.1:5000/predict_home_price1";
    $.post(url1, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        carparking: carparking,
        location: location.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + (data.estimated_price / 100000).toFixed(3) + " Lakh</h2>";
        console.log(status);
    });
  }

  function onClickedEstimatePrice2() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations2");
    var estPrice = document.getElementById("uiEstimatedPrice2");
  
    var url2 = "http://127.0.0.1:5000/predict_home_price2"; 
    $.post(url2, {
        sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    },function(data, status) {
        
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + (data.estimated_price / 100000).toFixed(3) + " Lakh</h2>";
        console.log(status);
    });
  }

  function onClickedEstimatePrice3() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue();
    var resale = getResaleValue();
    var location = document.getElementById("uiLocations3").value;
    var estPrice = document.getElementById("uiEstimatedPrice3");
  
    var url3 = "http://127.0.0.1:5000/predict_home_price3"; 
    $.post(url3, {
        area: parseFloat(sqft),
        num_bedrooms: bhk,
        resale: resale,
        location: location
    }, function(data, status) {
        console.log(data.estimated_price);
        var price = Math.abs(data.estimated_price); // Take absolute value
        estPrice.innerHTML = "<h2>" + (price / 100000).toFixed(3) + " Lakh</h2>";
        console.log(status);
    });
}
  
function onPageLoad() {
    console.log("document loaded");

    // Define the URLs for both requests
    var Url1 = "http://127.0.0.1:5000/get_location_names";
    var Url2 = "http://127.0.0.1:5000/get_location_names1";
    var Url3=  "http://127.0.0.1:5000/get_location_names2";
    var Url4=  "http://127.0.0.1:5000/get_location_names3";

    // Make the request for location names
    $.get(Url1, function (locationData, status) {
        console.log("got response for get_location_names request");
        if (locationData) {
            var locations = locationData.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });

    
    $.get(Url2, function (anotherData, status) {
        console.log("got response for get_location_names1 request");
        if (anotherData) {
            var locations = anotherData.locations;
            var uiLocations1 = document.getElementById("uiLocations1"); 
            $('#uiLocations1').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations1').append(opt);
            }
        }
    });

    $.get(Url3, function (anotherData1, status) {
        console.log("got response for get_location_names2 request");
        if (anotherData1) {
            var locations = anotherData1.locations;
            var uiLocations2 = document.getElementById("uiLocations2");
            $('#uiLocations2').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations2').append(opt);
            }
        }
    });

    $.get(Url4, function (anotherData2, status) {
        console.log("got response for get_location_names3 request");
        if (anotherData2) {
            var locations = anotherData2.locations;
            var uiLocations3 = document.getElementById("uiLocations3");
            $('#uiLocations3').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations3').append(opt);
            }
        }
    });
}

  
  window.onload = onPageLoad;