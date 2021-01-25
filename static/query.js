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
            console.log(JSON.stringify(result))
            data = JSON.stringify(result.data.login)
            // for (let d in data){
            //     for(let k in data[d]){
            //         aa = data[d][k]
            //     }
            // }
            $("#table2").html("<p>"+data+"</p>")
        },
        error: function(error){
            alert("ERROR");
            console.log(console.error);
        }
    });
    });
});


