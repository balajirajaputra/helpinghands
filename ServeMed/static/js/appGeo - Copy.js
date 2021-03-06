// Width and height
var chart_width     =   800;
var chart_height    =   600;
var color           =   d3.scaleQuantize().range([
    'rgb(255,245,240)', 'rgb(254,224,210)', 'rgb(252,187,161)',
    'rgb(252,146,114)', 'rgb(251,106,74)', 'rgb(239,59,44)',
    'rgb(203,24,29)', 'rgb(165,15,21)', 'rgb(103,0,13)'
]);

// Projection
var projection      =   d3.geoAlbersUsa()
    .translate([ 0,0 ]);
var path            =   d3.geoPath( projection );
    // .projection( projection );




// Create SVG
var svg             =   d3.select("#chart")
    .append("svg")
    .attr("width", chart_width)
    .attr("height", chart_height);

var zoom_map        =   d3.zoom()
    .scaleExtent([ 0.5, 3.0 ])
    .translateExtent([
        [ -1000, -500 ],
        [ 1000, 500 ]
    ])
    .on( 'zoom', function(){
     console.log( d3.event );
    var offset      =   [
        d3.event.transform.x,
        d3.event.transform.y
    ];
    var scale       =   d3.event.transform.k * 1100;

    projection.translate( offset )
        .scale( scale );

    svg.selectAll( 'path' )
        .transition()
        .attr( 'd', path );

    svg.selectAll( 'circle' )
        .transition()
        .attr( "cx", function(d) {
            return projection([d.Longitude, d.Latitude])[0];
        })
        .attr( "cy", function(d) {
            return projection([d.Longitude, d.Latitude])[1];
        });
});

var barTooltip = d3.select("body").append("div")
	    .attr("class", "tooltip")
	    .style("opacity", 0)
	    .style("width",800);
		
var map             =   svg.append( 'g' )
    .attr( 'id', 'map' )
    .call( zoom_map )
    .call(
        zoom_map.transform,
        d3.zoomIdentity
            .translate( chart_width / 2, chart_height / 1.8 )
            .scale( 1 )
    );

map.append( 'rect' )
    .attr( 'x', 0 )
    .attr( 'y', 0 )
    .attr( 'width', chart_width )
    .attr( 'height', chart_height )
    .attr( 'opacity', 0 );

// Data

//d3.json( 'Med.json', function( zombie_data ){
//		console.log('Min ---- > '+ d3.min(zombie_data, function(d){ return d.DistinctcountofProductName; }));
//		console.log('Max ---- > '+  d3.max(zombie_data, function(d){ return d.DistinctcountofProductName; }));
//	});
	
d3.json( 'data/Med.json', function( zombie_data ){
    color.domain([
		
        d3.min( zombie_data, function(d){
			//console.log('d.MedicaidAmountReimbursed ->>> '+ d.DistinctcountofProductName + '     Latitude + - Longitude - ' + d.Latitude + '- '+ d.Longitude);
			       return Math.sqrt(parseInt(d.MedicaidAmountReimbursed) * 0.00000005 );
			//console.log('d.MedicaidAmountReimbursed   -->' + d.MedicaidAmountReimbursed);
        }),
        d3.max( zombie_data, function(d){
            return Math.sqrt(parseInt(d.MedicaidAmountReimbursed) * 0.00000005 );
        })
    ]);

    d3.json( 'data/us.json', function( us_data ){
        us_data.features.forEach(function(us_e, us_i){
            zombie_data.forEach(function(z_e,z_i){
				
                if( us_e.properties.name !== z_e.StateName ){
                    return null;
                }
				//console.log('z_e.DistinctcountofProductName  - '+ z_e.DistinctcountofProductName);
				//console.log('z_e.StateName & us_e.properties.name --> '+z_e.StateName + '  ' + us_e.properties.name);
                us_data.features[us_i].properties.num   =   Math.sqrt(parseInt(z_e.MedicaidAmountReimbursed) * 0.00000005) ;
				//console.log('us_data.features[us_i].properties.num -> '+ us_data.features[us_i].properties.num +'  z_e.StateName ' + z_e.StateName);
				
            });
        });

        // console.log(us_data);

        map.selectAll( 'path' )
            .data( us_data.features )
            .enter()
            .append( 'path' )
            .attr( 'd', path )
            .attr( 'fill', function( d ){
                var num         =   d.properties.num;
				//console.log (' StateName + d.properties.num  -' + d.StateName +' - '+ d.properties.num);
                return num ? color( num ) : '#ddd';
            })
            .attr( 'stroke', '#fff' )
            .attr( 'stroke-width', 1 )
			// **added new code for state name 
			.append( 'title' )
            .text(function(d){
                return d.StateName;
				//console.data('d.StateName --- '+ d.StateName);
			})

        Draw_State();
		
    });
});

function Draw_State(){
    d3.json( 'data/Med.json', function( State_data ){
        map.selectAll("circle")
            .data(State_data)
            .enter()
            .append( "circle" )
           // .style( "fill", "#9D497A" )
		    .style( "fill", "steelblue" )
            .style( "opacity", 0.8 )
            .attr( 'cx', function( d ){
				
                return projection([d.Longitude, d.Latitude])[0];
				
            })
            .attr( 'cy', function( d ){
                return projection([d.Longitude, d.Latitude])[1];
            })
            .attr( 'r', function(d){
                return Math.sqrt(parseInt(d.MedicaidAmountReimbursed) * 0.00000008 );
				//return Math.sqrt(d.MedicaidAmountReimbursed * 0.00005 );
				//console.log('Math.sqrt(parseInt(d.MedicaidAmountReimbursed) * 0.00005 ) --' + Math.sqrt(parseInt(d.MedicaidAmountReimbursed) * 0.00005 ));
				
            })
          
		  .append( 'title' )
           .text(function(d){
               return "State - " + d.StateName + " & Total Medicare Amount Reimbursed - $" + d.MedicaidAmountReimbursed;
			   //return "State - " + d.StateName;
           });
		   
		   
			   
    });
}

d3.selectAll( '#buttons button.panning' ).on( 'click', function(){
    var x           =   0;
    var y           =   0;
    var distance    =   100;
    var direction   =   d3.select( this ).attr( 'class' ).replace( 'panning ', '' );

    if( direction === "up" ){
        y           +=  distance; // Increase y offset
    }else if( direction === "down" ){
        y           -=  distance; // Decrease y offset
    }else if( direction === "left" ){
        x           +=  distance; // Increase x offset
    }else if( direction === "right" ){
        x           -=  distance; // Decrease x offset
    }

    map.transition()
        .call( zoom_map.translateBy, x, y );
});

d3.selectAll( '#buttons button.zooming' ).on( 'click', function(){
    var scale       =   1;
    var direction   =   d3.select(this).attr("class").replace( 'zooming ', '' );

    if( direction === "in" ){
        scale       =  1.25;
    }else if(direction === "out"){
        scale       =  0.75;
    }

    map.transition()
        .call(zoom_map.scaleBy, scale);
});