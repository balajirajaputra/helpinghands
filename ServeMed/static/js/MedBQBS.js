
var svg = d3.select("svg"),
    margin = {top: 25, right: 25, bottom: 50, left: 75},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom;


	
var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
    y = d3.scaleLinear().rangeRound([height, 0]);

var g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


d3.tsv("data/MedBQBS1.tsv", function(d) {
  return d;
}, function(error, data) {
  if (error) throw error;

  // filter year/quarter
	// Get every column value
	var elements = Object.keys(data[0])
		.filter(function(d){
			return (d != "State");
		});
	
  var selection = elements[0];
  
  x.domain(data.map(function(d) { return d.State; }));
  
  y.domain([0, d3.max(data, function(d) { return +d[selection]; })]);
  
     g.append("g")
      .attr("class", "axis axis--y")
	  .call(d3.axisLeft(y));
	//  .call(d3.axisLeft(y).ticks(8).tickSizeInner([-width])); //This line shows the bars
	
  g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

	  //label for the X axis
	  
	  svg.append("text")             
      .attr("transform",
            "translate(" + (width/2) + " ," + 
                           (height + margin.top + 35) + ")")
      .style("text-anchor", "middle")
      .text("State");

	svg.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 95)
      .attr("dy", "0.40em")
      .attr("text-anchor", "end")
      .text('Amount Reimbursed');

  g.selectAll(".bar")
    .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d, i) { return (width / data.length) * i ; })
      .attr("y", function(d) { return y(+d[selection]); })
	  .attr("width", 15)
      .attr("height", function(d) {  return height - y(+d[selection]); })
	  .append("title")
		.text(function(d){
			return ' '+ d.State + " :  $" +d[selection];
		});
	 
	var selector = d3.select("#drop")
    	.append("select")
    	.attr("id","dropdown")
    	.on("change", function(d){
        	selection = document.getElementById("dropdown");
		
		y.domain([0, d3.max(data, function(d) { return +d[selection.value]; })]);
	
		d3.select("g")
		.attr("class", "axis axis--y")
		.transition()
		.call(d3.axisLeft(y));
	
		x.domain(data.map(function(d) { return d.State; }));

	g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));
				
		d3.selectAll(".bar")
           		.transition()
	            .attr("height", function(d){
					return height - y(+d[selection.value]);
				})
				.attr("x", function(d, i){
					return (width / data.length) * i ;
				})
				.attr("y", function(d){
					return y(+d[selection.value]);
				})
           		.duration(2000)
           		.select("title")
           		.text(function(d){
					
           			return ' '+ d.State + " :  $" + d[selection.value];
           		});
		})
	
	selector.selectAll("option")
      .data(elements)
      .enter().append("option")
      .attr("value", function(d){
        return d;
      })
      .text(function(d){
        return d;
      })
	/*  
	 .on( 'mouseover', function(d) {
		d3.select( '#tooltip')
			.style("top", (event.pageY-10)+"px")
			.style("left",(event.pageX+10)+"px")
			.style( 'display', 'block' )
			.html(('State Name  : ' + d.StateName) + "<br>" + d[selection] + "Medicaid Amount Reimbursed : $" + d[selection.value]
					+ "<br>" + ('Number Of Prescriptions : ' + data.NumberofPrescriptions ) + "<br>" + ('Distinct Number of Drugs Prescribed : ' + d.DistinctcountofProductName ) 
					+ "<br>" + ('Number Of Units Reimbursed : ' + d.UnitsReimbursed ));
		
	})
	
	.on( 'mouseout', function(){
			d3.select( '#tooltip')
			.style( 'display' ,'none')
		
	});*/
});

