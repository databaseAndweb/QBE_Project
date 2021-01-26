$(document).ready(function(){
    
    $("#goBtn").click(function(){
        const user = $("#user").val();
        const pwd = $("#pwd").val();
        const db = $("#db").val();

        $.ajax({url: 'http://127.0.0.1:5000/qbe/?query={login(user:"'+user+ '",pwd:"'+pwd+ '",db:"'+db+ '"){table}}',
        "headers": {
            "accept": "application/json",
            "Access-Control-Allow-Origin":"*"
        }, 
        
        type:'POST',
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
            $("#showDatabaseTableForm").html(htmlCode);
        },
        error: function(error){
            alert("ERROR");
            console.log(console.error);
        }
    });
    });
});


