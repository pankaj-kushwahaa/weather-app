// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.
// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

function initMap(coord) {
  let mapel = document.getElementById("map");
  let input = document.getElementById("pac-input");

  let {latitude, longitude} = coord;

  const myLatlng = { lat: latitude, lng: longitude };
  const map = new google.maps.Map(mapel, {
    zoom: 10,
    center: myLatlng,
  });

  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
  // Create the initial InfoWindow.
  let infoWindow = new google.maps.InfoWindow({
    content: "Click the map to get Lat/Lng!",
    position: myLatlng,
  });

  infoWindow.open(map);
  // Configure the click listener.
  map.addListener("click", (mapsMouseEvent) => {
    let latInput = document.getElementById("latitude");
    let longInput = document.getElementById("longitude");
    let lati = mapsMouseEvent.latLng.lat()+"";
    let longi =  mapsMouseEvent.latLng.lng()+"";
    latInput.value = lati.substring(0, 9);
    longInput.value = longi.substring(0, 9);
    // Close the current InfoWindow.
    infoWindow.close();
    // Create a new InfoWindow.
    infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
    });
    infoWindow.setContent(
      JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
    );
    infoWindow.open(map);
  });
}

window.initMap = initMap;

// Get User input and auto complete the seach box
function initializeAutocomplete() {
  var input = document.getElementById('pac-input');
  var autocomplete = new google.maps.places.Autocomplete(input);

  autocomplete.addListener('place_changed', function () {
      var place = autocomplete.getPlace();
      if (!place.geometry) {
          console.log("No details available for input: " + place.name);
          return;
      }
      
      var lat = place.geometry.location.lat();
      var lng = place.geometry.location.lng();

      marker.setPosition(place.geometry.location);
      map.setCenter(place.geometry.location);

      console.log("Latitude: " + lat);
      console.log("Longitude: " + lng);
  });
}
google.maps.event.addDomListener(window, 'load', initializeAutocomplete);

// Get user location
function getLocation(){
  navigator.geolocation.getCurrentPosition((success) => {
    let {latitude, longitude } = success.coords;
    let obj = {
      latitude : latitude,
      longitude : longitude
    }
    google.maps.event.addDomListener(window, 'load', initMap(obj));
    getData(obj);
  }, (error)=> {
    console.log(error);
    let obj = {
      latitude : 30.5900,
      longitude : 76.844
    }
    google.maps.event.addDomListener(window, 'load', initMap(obj));
  });
}

getLocation();
