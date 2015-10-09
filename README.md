zombie-watchtower
=================

Simple script to observe the zombie status of nations in a region and save it to a json file

May be combined with other tools to make a helpful webpage

Do not use in a way that does not comply with the API Rate limits, please.

# Example Web Page Fragment

```html
<script type="text/javascript">

var region_name = 'Your Region Name';

function action_filter(action) {
  $('#top_nations tbody tr').hide();
  $('.'+action).show();
}

$(document).ready(function(){
  $.getJSON("zombie_info.json", function(data) {
    $("noscript").after('<p style="font-style:italic; font-weight:bold; font-size:12pt;">'+region_name+' Nations</p><p>by survivors, zombies, or dead</p><p>Filter by <a href="#research" onclick="action_filter('+"'research'"+');" name="show_all">research</a>, <a href="#exterminate" onclick="action_filter('+"'exterminate'"+');" name="show_all">exterminate</a>, <a href="#export" onclick="action_filter('+"'export'"+');" name="show_all">export</a>, or <a href="#null" onclick="action_filter('+"'null'"+');" name="show_all">considering options</a>.</p>',$("<table>",{
      id:'top_nations',
      class:'tablesorter',
      width:'300'
    }).append('<thead><tr><th>#</th><th>Nation</th><th>Survivors</th><th>Zombies</th><th>Dead</th></tr></thead>',$('<tbody>').append($.map( data, function(nation,idx){
      return '<tr class="'+(nation.action ? nation.action : 'null' )+'"><th>'+(idx+1)+'</th><th><a href="https://www.nationstates.net/nation='+nation.name+'">'+nation.Name+'</a></th><td>'+nation.survivors+'<td>'+nation.zombies+'</td><td>'+nation.dead+'</td></tr>' ;
    }).join())));
    $("#top_nations").tablesorter({sortList:[[3,1]],headers:{0:{sorter:false},1:{sorter:false}}});
    $("#top_nations").bind('sortStart',function(){
      $("#top_nations tbody th:first-child").text(function(idx,o){return '';});
    }).bind('sortEnd',function(){
      $("#top_nations tbody th:first-child").text(function(idx,o){return idx+1;});
    });
    if( window.location.hash ) {
      document.getElementById('top_nations').scrollIntoView(true);
      var action = {'#null':'null','#research':'research','#exterminate':'exterminate','#export':'export'}[window.location.hash];
      if( action ){
        action_filter(action);
      }
    }
  });
});
</script>
</head>
<body>
<div id="main_b"><div class="wrapper"><div id="main_content">
<center><h1>Zombie Observation Post</h1>
<img src="http://some.site.com/your_regional_image.jpg" alt="">
<br><noscript><p style="font-style:italic; font-weight:bold; font-size:12pt; color:red;">Because you have javascript disabled, this page will not work.</p></noscript>
</div></div></div>
```
