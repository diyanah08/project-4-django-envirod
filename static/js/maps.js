/* global mapboxgl */


mapboxgl.accessToken = 'pk.eyJ1IjoiZGl5YW5haDA4IiwiYSI6ImNrMHlwam9pNzBoc2QzYnA4ZXgydXFvY2cifQ.5Ou3JPEXHCQOJ-0H4Blltw';

let map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [103.8198, 1.3521], 
    zoom: 11,
});

map.on('load', function() {
    map.addLayer({
        "id": "points",
        "type": "symbol",
        "source": {
            "type": "geojson",
            "data": {
                "type": "FeatureCollection",
                "features": [{
                        "type": "Feature",
                        "properties": {
                            "name": "SHOP1",
                            "icon": "marker",
                            "color": "#EC1212",
                            "description": "<p>DETAILS</p>"
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [103.8937, 1.3180]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {
                            "name": "SHOP2",
                            "icon": "marker",
                            "color": "#EC1212",
                            "description": "<p>DETAILS</p>"
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [103.8384, 1.3009]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {
                            "name": "SHOP3",
                            "icon": "marker",
                            "color": "#EC1212",
                            "description": "<p>DETAILS</p>"
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [103.8486, 1.3505]
                        }
                    },
                ]
            }
        },
        "layout": {
            "icon-image": "{icon}-15",
            "text-field": "{name}",
            "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
            "text-offset": [0, 0.6],
            "text-anchor": "top"
        },
        "paint": {
            "text-color": ["get", "color"]
        }
    });

    map.on('click', 'points', function(e) {
        let coordinates = e.features[0].geometry.coordinates.slice();
        let description = e.features[0].properties.description;

        new mapboxgl.Popup({ offset: [0, 1] })
            .setLngLat(coordinates)
            .setHTML(description)
            .addTo(map);
    });
});