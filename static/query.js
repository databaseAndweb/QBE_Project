$(document).ready(function(){
    
    $("#form1").on('submit', function(e){
        e.preventDefault();
        
        // const user = $("#user").val();
        // const pwd = $("#pwd").val();
        // const db = $("#db").val();

        console.log("MESSSADRFE")
        var text = document.getElementById("showDatabaseTableForm");
                if (text.style.display === "none"){
                    text.style.display = "block";
                } else{
                    text.style.display = "none";
                }
        var login = {
            user: $("#user").val(),
            pwd: $("#pwd").val(),
            db: $("#db").val()
        }

        $.ajax({url: 'http://127.0.0.1:5000/qbe/?query={login(user:"'+$("#user").val()+ '",pwd:"'+
        $("#pwd").val()+ '",db:"'+$("#db").val()+ '"){table}}',
        "headers": {
            "accept": "application/json",
            "Access-Control-Allow-Origin":"*"
        }, 
        
        type:'POST',
        data: login,
        success: function(result){
            data = result.data.login;
            console.log(data)       
            var htmlCode = "<table><tr>";
            arr = [];
            console.log(data);
            for(var i = 0; i < data.length; i++){
                var item = Object.values(data[i]);
                //arr.push(item);
                console.log(item);
                
                 htmlCode+= '<td><b>'+item+":"+'</b></td>'
                     htmlCode +='<td><select id="tnames" onchange="populateTables()">'+
                    '<option id="None" value="0">0</option>'; 
                    
                    for (var j = 1; j<  3; j++){
                        htmlCode+='<option value="'+item+'">'+j+'</option>';
                        
                        
                    }

                    htmlCode +=  "</td></select></tr><table>";
                    
            }
            //htmlCode += "</select></td></tr><table>";
            htmlCode +='<input type="button" value="Get Skeletons" onclick="populateTables()"><input type="reset" value="Reset Skeletons">'
            $("#showDatabaseTableForm").html(htmlCode);
        },
        error: function(error){
            alert("ERROR");
            console.log(console.error);
        }
    });
    });
});


function populateTables() {
    console.log("hgjghjjjjjjjjjjjjjjjg");
    //An example :
    //var tnames = $("#dropdwn").children("option:selected").text(); 
    //var tnames = $("#dropdwn").children("option:selected").val();
    //console.log(tnames);
    //var tnames = "ROOM";
    
    
    var url = 'http://127.0.0.1:5000/qbe/?query={skeletons(tnames:["'+$("#tnames").val()+'"],user:"'+$("#user").val()+ '",pwd:"'+
    $("#pwd").val()+ '",db:"'+$("#db").val()+ '"){table colAndtype}}'
    $.ajax({
      url: url,
      type: 'GET',
      success: function(response) {
        var skel = response.data.skeletons;
        newTable = [];
        for(var j = 0; j < skel.length; j++){
            newTable.push(skel[j].table);

        }
        var htmlCode = '<table class="borderedtables">'+
                   '<tr class="tableheader"><tr class="tableheader">'+
                   '<td class="borderedtables">'+newTable[0]+'</td>';
        for (var i=0; i<skel.length; i++){
            //var item = Object.values(skel[i]);
            htmlCode += '<td class="borderedtables">'+skel[i].colAndtype+'</td>';
            // htmlCode+='<tr class=""><td><input type="text"></td>test</td></tr>';
        }
        htmlCode +='</tr><tr class="borderedtables">';
        for(var i=0; i<skel.length+1; i++){
            htmlCode+='<td><input type="text"></td>';
        }

        htmlCode += '</tr></table>';
        $("#interface").html(htmlCode);
      },
      error: function(error) {
        alert("ERROR");
        console.log(error);
      }
    });
  };
  
  $(document).ready(function(){

    $("#lastPart").on('submit', function(e){
        e.preventDefault();

        const tabPar = $("#user").val();
        const colPar = $("#pwd").val();
        const condPar = $("#db").val();


    })

    

 });