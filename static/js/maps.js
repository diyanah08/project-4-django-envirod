/* global mapboxgl */


let places = [{
        'name': "Shop 1",
        'position': [103.8937, 1.3180],
        'image': '',
        'description': "Details"
    },
    {
        'name': "Shop 2",
        'position': [103.8384, 1.3009],
        'image': '',
        'description': "Details"
    },
    {
        'name': 'Shop 3',
        'position': [103.8486, 1.3505],
        'image': '',
        'description': "Details"
    }
]

mapboxgl.accessToken = "pk.eyJ1IjoiZGl5YW5haDA4IiwiYSI6ImNrMHlwam9pNzBoc2QzYnA4ZXgydXFvY2cifQ.5Ou3JPEXHCQOJ-0H4Blltw";

let mapOptions = {
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11', 
    center: [103.8198, 1.3521], 
    zoom: 11, 
};
let map = new mapboxgl.Map(mapOptions);

// Create a Marker
for (let each_place of places) {
    let m = new mapboxgl.Marker();
    let p = new mapboxgl.Popup({
        offset: 25
    });
    m.setLngLat(each_place.position);
    p.setHTML(`<h1>${each_place.name}</h1>
                <p>${each_place.description}</p>`);
    m.setPopup(p);
    m.addTo(map);
}