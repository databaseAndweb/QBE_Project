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
            var htmlCode = "<table>";
            arr = [];
            for(var i = 0; i < data.length; i++){
                var item = Object.values(data[i]);
                //arr.push(item);
                //console.log(arr);
                
                 htmlCode+= '<tr><td><b>'+item+":"+'</b></td><td><select><option value="0">0</option><option value="1">1</option>' +
                 '<option value="2">2</option></select></td></tr>';
            }
            htmlCode += "<table>";
            htmlCode +='<input type="button" value="Get Skeletons" onclick="getSkel()"><input type="reset" value="Reset Skeletons">'
            $("#showDatabaseTableForm").html(htmlCode);
        },
        error: function(error){
            alert("ERROR");
            console.log(console.error);
        }
    });
    });
});


function getSkel() {
    console.log("hgjghjjjjjjjjjjjjjjjg")

    // var text = document.getElementById("interface");
    // if (text.style.display === "none"){
    //     text.style.display = "block";
    // } else{
    //     text.style.display = "none";
    // }
    var url = 'http://127.0.0.1:5000/qbe/?query={skeletons(tnames:["'+$("#tnames").val()+'"],user:"'+$("#user").val()+ '",pwd:"'+
    $("#pwd").val()+ '",db:"'+$("#db").val()+ '"){nameAndtype}}'
    $.ajax({
      url: url,
      type: 'POST',
      success: function(response) {
        var skel = response.data.skeletons;
        var htmlCode = '<table class="borderedtables" style="width: 100%;">'+
                   '<tr class="tableheader"><tr class="tableheader">'
        for (var i=0; i<skel.length; i++){
            var item = Object.values(skel[i]);
            htmlCode += '<td class="borderedtables">'+item+'</td>'
            // htmlCode+='<tr class=""><td><input type="text"></td>test</td></tr>';
        }
        htmlCode +='</tr><tr class="borderedtables">'
        for(var i=0; i<skel.length; i++){
            htmlCode+='<td><input type="text" size="24" width=200px></td>'
        }

        htmlCode += '</tr></table>'
        $("#interface").html(htmlCode);
      },
      error: function(error) {
        alert("ERROR");
        console.log(error);
      }
    });
  };
  