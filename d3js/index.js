
var dataset = [80, 100, 56, 231, 412, 232, 34, 324];

var svgWidth = 500, svgHeight=300, barPadding=5;
var barWidth = (svgWidth / dataset.length);

var svg = d3.select('svg')
    .attr("width",svgWidth)
    .attr("height",svgHeight);

var barChart = svg.selectAll("rect") // no rectangles yet so empty selection
    .data(dataset)
    .enter() // applies code below to each item in dataset
    .append("rect") // add rect to svg
    .attr("y", function(d){
        return svgHeight - d;
    })
    .attr("height", function(d){
        return d;
    })
    .attr("width", barWidth - barPadding)
    .attr("class", "bar")
    .attr("transform",function(d,i){
        var translate = [barWidth * i,0];
        return "translate("+translate+")";
    })
    .attr("fill","#A64C38");

var text = svt.selectAll("text")
    .data(dataset)
    .enter()
    .append("text")
    .text(function(d){
        return d;
    })
    .attr("y", function(d,i){
        return svgHeight - d - 20;
    })
    .attr("x", function(d,i){
        return barWidth*i;
    })
    .attr("fill", "#A64C38");


/*d3.select();
d3.selectAll();

d3.select('h1').style('color','red')
    .attr('class','heading') 
    .text('Updated h1 tag');

d3.select('body').append('p').text("AAAA");
d3.select('body').append('p').text("BBBB");
d3.select('body').append('p').text("CCCC");
d3.select('body').append('p').text("CCCC");
d3.select('body').append('p').text("CCCC");
d3.select('body').append('p').text("CCCC");
d3.select('body').append('p').text("CCCC");

d3.selectAll('p').style('color', 'blue')

var dataset = [1,2,3,4,5];
d3.select('body')
    .selectAll('p')
    .data(dataset)
    .enter()
    .append('p')
    //.text('AAAAAAAAA');
    .text(function(a){return a;});*/

